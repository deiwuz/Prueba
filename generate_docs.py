#!/usr/bin/env python3
"""Utility for generating CV, cover letter and LinkedIn profile documents.

This script ingests one or more candidate definitions from a JSON file and
produces Markdown, DOCX and PDF artefacts for each candidate.  The
implementation is intentionally self-contained so that it can be executed from
the command line or imported from other modules if desired.

The original version of this script had a few rough edges that manifested when
candidate data contained optional fields or characters that are unsuitable for
file names.  The current implementation smooths out those issues and performs a
bit of additional validation to keep the output predictable.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field, fields
from datetime import date
from pathlib import Path
from typing import Any, Dict, Iterable, List


@dataclass
class Experience:
    """Represents a single professional experience entry."""

    title: str
    company: str
    location: str = ""
    dates: str = ""
    responsibilities: List[str] = field(default_factory=list)


@dataclass
class Education:
    """Represents a single education entry."""

    degree: str
    institution: str
    date: str


@dataclass
class Candidate:
    """Stores all necessary information for a candidate."""

    name: str
    location: str
    email: str
    phones: List[str]
    summary: str
    skills: List[str]
    experiences: List[Experience]
    education: List[Education]
    eligibility: str
    highlights: List[str]
    dob: str | None = None
    linkedin_about: str | None = None
    linkedin_contact_label: str | None = None
    linkedin_contact: List[str] | None = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Candidate":
        """Create a :class:`Candidate` instance from a dictionary.

        The JSON input provided to this project has evolved over time.  Some
        documents include auxiliary keys that are not represented in the data
        classes.  Instantiating the dataclasses with those keys would raise a
        :class:`TypeError`.  To make the loader more tolerant we only forward
        fields that the target dataclass actually understands.  Missing optional
        values fall back to their defaults.
        """

        experiences = [
            _coerce_dataclass(Experience, exp)
            for exp in data.get("experiences", [])
            if isinstance(exp, dict)
        ]
        education = [
            _coerce_dataclass(Education, edu)
            for edu in data.get("education", [])
            if isinstance(edu, dict)
        ]

        return cls(
            name=data["name"],
            location=data["location"],
            email=data["email"],
            phones=list(data.get("phones", [])),
            summary=data["summary"],
            skills=list(data.get("skills", [])),
            experiences=experiences,
            education=education,
            eligibility=data.get("eligibility", ""),
            highlights=list(data.get("highlights", [])),
            dob=data.get("dob"),
            linkedin_about=data.get("linkedin_about"),
            linkedin_contact_label=data.get("linkedin_contact_label"),
            linkedin_contact=list(data.get("linkedin_contact", []) or []),
        )

    def format_phones(self) -> str:
        """Return a formatted string of phone numbers separated by slashes."""

        return " / ".join(self.phones)

    def md_contact_header(self) -> str:
        """Construct the contact header line in Markdown."""

        parts: List[str] = []
        if self.location:
            parts.append(f"**{self.location}**")
        if self.email:
            parts.append(f"**{self.email}**")
        if self.phones:
            parts.append(f"**{' / '.join(self.phones)}**")
        return " | ".join(parts)


def _coerce_dataclass(cls, payload: Dict[str, Any]):
    """Filter *payload* to the known fields of ``cls`` and instantiate it."""

    valid_fields = {field_.name for field_ in fields(cls)}
    filtered: Dict[str, Any] = {k: payload[k] for k in payload.keys() & valid_fields}
    return cls(**filtered)


def write_markdown_file(path: Path, content: str) -> None:
    """Write *content* to *path*, creating parent directories as required."""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def make_safe_filename(value: str) -> str:
    """Create a filesystem-friendly slug based on ``value``."""

    safe = re.sub(r"[^A-Za-z0-9]+", "_", value.strip())
    return safe.strip("_") or "document"


def format_display_date(value: date) -> str:
    """Return a locale-aware day-month-year string that works cross-platform."""

    for fmt in ("%-d %B %Y", "%#d %B %Y", "%d %B %Y"):
        try:
            return value.strftime(fmt)
        except ValueError:
            continue
    return value.isoformat()


def _first_sentence(text: str) -> str:
    """Extract the first sentence from a block of text."""

    stripped = text.strip()
    if not stripped:
        return ""
    first = stripped.split(".", 1)[0].strip()
    return first or stripped


def generate_cv_markdown(candidate: Candidate) -> str:
    """Generate the Markdown content for a candidate's CV."""

    lines = [f"# {candidate.name} CV", "", candidate.md_contact_header()]

    if candidate.dob:
        try:
            dob_date = date.fromisoformat(candidate.dob)
            dob_str = format_display_date(dob_date)
        except ValueError:
            # ``fromisoformat`` only accepts the ISO standard; fall back to the
            # verbatim string if the value is already formatted.
            dob_str = candidate.dob
        lines.extend(["", f"**Date of Birth:** {dob_str}"])

    lines.extend(["", "## Professional Summary", "", candidate.summary.strip(), ""])

    if candidate.skills:
        lines.extend(["## Core Skills", ""])
        lines.extend(f"- {skill.strip()}  " for skill in candidate.skills if skill.strip())
        lines.append("")

    if candidate.experiences:
        lines.extend(["## Professional Experience", ""])
        for experience in candidate.experiences:
            header = f"**{experience.title} – {experience.company}".rstrip()
            if experience.dates:
                header += f" ({experience.dates})"
            header += "**"
            lines.extend([header, ""])
            lines.extend(
                f"- {resp.strip()}  " for resp in experience.responsibilities if resp.strip()
            )
            lines.append("")

    if candidate.education:
        lines.extend(["## Education", ""])
        lines.extend(
            f"- **{edu.degree}** – {edu.institution} ({edu.date})  "
            for edu in candidate.education
        )
        lines.append("")

    if candidate.eligibility:
        lines.extend(["## Work Eligibility", "", candidate.eligibility.strip(), ""])

    return "\n".join(lines).strip() + "\n"


def generate_cover_markdown(candidate: Candidate, current_date: str) -> str:
    """Generate the Markdown content for a candidate's cover letter."""

    header = [
        f"# {candidate.name} Cover Letter",
        "",
        candidate.md_contact_header(),
        "",
        current_date,
        "",
        "[Company Name]  ",
        "[City, Province]",
        "",
        "Dear Hiring Manager,",
        "",
    ]

    summary_sentence = _first_sentence(candidate.summary)
    intro = (
        "I am writing to express my interest in the **[Job Title]** role at "
        "**[Company Name]**."
    )
    if summary_sentence:
        if not summary_sentence.endswith("."):
            summary_sentence += "."
        intro += f" {summary_sentence}"
    lines = header + [intro, ""]

    if candidate.highlights:
        lines.extend(["**Highlights that I would bring to your team include:**", ""])
        lines.extend(
            f"- {highlight.strip()}  "
            for highlight in candidate.highlights
            if highlight.strip()
        )
        lines.append("")

    conclusion = (
        "I am open to relocating and available to discuss work authorization options. "
        "Thank you for your time and consideration – I look forward to the opportunity to "
        "contribute to your team."
    )
    lines.extend([conclusion, "", "Sincerely,", "", candidate.name, ""])
    return "\n".join(lines).strip() + "\n"


def generate_linkedin_markdown(candidate: Candidate) -> str:
    """Generate Markdown content for a candidate's LinkedIn profile."""

    lines = [f"# LinkedIn Profile – {candidate.name}", ""]

    about_text = (candidate.linkedin_about or candidate.summary).strip()
    lines.extend(["## About", "", about_text, ""])

    if candidate.experiences:
        lines.extend(["## Experience", ""])
        for experience in candidate.experiences:
            header = f"**{experience.title} – {experience.company}"
            if experience.dates:
                header += f" ({experience.dates})"
            header += "**"
            lines.extend([header, ""])
            lines.extend(
                f"- {resp.strip()}  " for resp in experience.responsibilities if resp.strip()
            )
            lines.append("")

    if candidate.education:
        lines.extend(["## Education", ""])
        lines.extend(
            f"- **{edu.degree}** – {edu.institution} ({edu.date})  "
            for edu in candidate.education
        )
        lines.append("")

    if candidate.skills:
        lines.extend(["## Skills", ""])
        lines.extend(
            f"- {skill.strip()}  " for skill in candidate.skills if skill.strip()
        )
        lines.append("")

    lines.extend(["## Contact", "", f"**Location:** {candidate.location}  "])
    lines.append(f"**Email:** {candidate.email}  ")
    if candidate.linkedin_contact:
        label = candidate.linkedin_contact_label or "Phones"
        contact = " / ".join(candidate.linkedin_contact)
        lines.append(f"**{label}:** {contact}  ")
    lines.append("")
    return "\n".join(lines).strip() + "\n"


def run_subprocess(cmd: Iterable[str]) -> None:
    """Run ``cmd`` and raise :class:`RuntimeError` on failure."""

    try:
        subprocess.run(list(cmd), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as exc:  # pragma: no cover - exercised in integration
        sys.stderr.write(f"Command failed: {' '.join(cmd)}\n")
        sys.stderr.write(exc.stdout.decode(errors="ignore"))
        sys.stderr.write(exc.stderr.decode(errors="ignore"))
        raise RuntimeError("Document conversion command failed") from exc


def convert_md_to_docx(md_path: Path, docx_path: Path) -> None:
    """Convert Markdown to DOCX using pandoc."""

    run_subprocess(["pandoc", str(md_path), "-o", str(docx_path)])


def convert_docx_to_pdf(docx_path: Path, pdf_path: Path) -> None:
    """Convert DOCX to PDF using LibreOffice in headless mode."""

    run_subprocess(
        [
            "libreoffice",
            "--headless",
            "--convert-to",
            "pdf",
            "--outdir",
            str(pdf_path.parent),
            str(docx_path),
        ]
    )
    generated_pdf = docx_path.with_suffix(".pdf")
    if generated_pdf != pdf_path and generated_pdf.exists():
        generated_pdf.replace(pdf_path)


def generate_documents_for_candidate(
    candidate: Candidate, output_dir: Path, current_date: str
) -> Dict[str, Path]:
    """Generate all document formats for ``candidate``."""

    safe_name = make_safe_filename(candidate.name)
    base_paths = {
        "cv": safe_name + "_cv",
        "cover": safe_name + "_cover_letter",
        "linkedin": safe_name + "_linkedin_profile",
    }

    cv_md = output_dir / f"{base_paths['cv']}.md"
    cv_docx = output_dir / f"{base_paths['cv']}.docx"
    cv_pdf = output_dir / f"{base_paths['cv']}.pdf"

    cover_md = output_dir / f"{base_paths['cover']}.md"
    cover_docx = output_dir / f"{base_paths['cover']}.docx"
    cover_pdf = output_dir / f"{base_paths['cover']}.pdf"

    linkedin_md = output_dir / f"{base_paths['linkedin']}.md"
    linkedin_docx = output_dir / f"{base_paths['linkedin']}.docx"
    linkedin_pdf = output_dir / f"{base_paths['linkedin']}.pdf"

    write_markdown_file(cv_md, generate_cv_markdown(candidate))
    write_markdown_file(cover_md, generate_cover_markdown(candidate, current_date))
    write_markdown_file(linkedin_md, generate_linkedin_markdown(candidate))

    convert_md_to_docx(cv_md, cv_docx)
    convert_md_to_docx(cover_md, cover_docx)
    convert_md_to_docx(linkedin_md, linkedin_docx)

    convert_docx_to_pdf(cv_docx, cv_pdf)
    convert_docx_to_pdf(cover_docx, cover_pdf)
    convert_docx_to_pdf(linkedin_docx, linkedin_pdf)

    return {
        "cv_md": cv_md,
        "cv_docx": cv_docx,
        "cv_pdf": cv_pdf,
        "cover_md": cover_md,
        "cover_docx": cover_docx,
        "cover_pdf": cover_pdf,
        "linkedin_md": linkedin_md,
        "linkedin_docx": linkedin_docx,
        "linkedin_pdf": linkedin_pdf,
    }


def load_candidates(json_path: Path) -> List[Candidate]:
    """Load candidate definitions from ``json_path``."""

    payload = json.loads(json_path.read_text(encoding="utf-8"))
    if isinstance(payload, dict):
        return [Candidate.from_dict(payload)]
    if isinstance(payload, list):
        return [Candidate.from_dict(item) for item in payload if isinstance(item, dict)]
    raise ValueError("Invalid JSON format. Must be an object or list of objects.")


def main(argv: List[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Generate CV, cover letter and LinkedIn documents from JSON data."
    )
    parser.add_argument("input", help="Path to JSON file containing candidate data.")
    parser.add_argument(
        "--output-dir", default="./output", help="Directory to write generated files."
    )
    parser.add_argument(
        "--date",
        default=format_display_date(date.today()),
        help="Date to insert in cover letters (default: today).",
    )

    args = parser.parse_args(argv)

    input_path = Path(args.input)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    candidates = load_candidates(input_path)

    results: Dict[str, Dict[str, Path]] = {}
    for candidate in candidates:
        result = generate_documents_for_candidate(candidate, output_dir, args.date)
        results[candidate.name] = result
        print(f"Generated documents for {candidate.name}:")
        for label, path in result.items():
            print(f"  {label}: {path}")

    print("\nAll documents generated successfully.")


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    main()

