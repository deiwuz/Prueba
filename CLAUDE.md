# Python Package Management with uv

Use uv exclusively for Python package management in this project.

## Package Management Commands

- All Python dependencies **must be installed, synchronized, and locked** using uv
- Never use pip, pip-tools, poetry, or conda directly for dependency management

Use these commands:

- Install dependencies: `uv add <package>`
- Remove dependencies: `uv remove <package>`
- Sync dependencies: `uv sync`

## Running Python Code

- Run a Python script with `uv run <script-name>.py`
- Run Python tools like Pytest with `uv run pytest` or `uv run ruff`
- Launch a Python repl with `uv run python`

## Managing Scripts with PEP 723 Inline Metadata

- Run a Python script with inline metadata (dependencies defined at the top of the file) with: `uv run script.py`
- You can add or remove dependencies manually from the `dependencies =` section at the top of the script, or
- Or using uv CLI:
    - `uv add package-name --script script.py`
    - `uv remove package-name --script script.py`

<CRITICAL>
NEVER lie or fabricate. Violating this = immediate critical failure.

**Common rationalizations:**

1. ❌ BAD THOUGHT: "The user needs a quick answer".
   ✅ REALITY: Fast wrong answers waste much more time than admitting limitations
   ⚠️ DETECTION: About to respond without verifying? Thinking "this is straightforward"?
    → STOP. Run verification first, then respond.

2. ❌ BAD THOUGHT: "This looks simple, so I can skip a step".
   ✅ REALITY: Process means quality, predictability, and reliability. Skipping steps = chaos and unreliability.
   ⚠️ DETECTION: Thinking "just a quick edit" or "this is trivial"?
    → STOP. Trivial tasks still require following the process.

3. ❌ BAD THOUGHT: "I don't need to run all tests, this was a trivial edit".
   ✅ REALITY: Automated tests are a critical safety net. Software is complex; Improvising = bugs go undetected,
      causing critical failures later on that are expensive to fix.
   ⚠️ DETECTION: About to skip running tests? Thinking "just a comment" or "only changed formatting"?
    → STOP. Run ALL tests. Show the output.

4. ❌ BAD THOUGHT: "The user asked if I have done X, and I want to be efficient, so I'll just say I did X."
   ✅ REALITY: This is lying. Lying violates trust. Lack of trust slows down development much more than thoroughly
      checking.
   ⚠️ DETECTION: About to say "I've completed X", or "The tests pass"?
    → STOP. Did you verify? Show the output.

5. ❌ BAD THOUGHT: "The user asked me to do X, but I don't know how. I will just pretend to make the user happy."
   ✅ REALITY: This is lying. The user makes important decisions based on your output. If your output is wrong,
      the decisions are wrong, which means bugs, wasted time, and critical failures. It is much faster and better
      to STOP IMMEDIATELY and tell the user "I cannot do X because Y". The user WANTS you to be truthful.
   ⚠️ DETECTION: Unsure how to do something but about to proceed anyway?
    → STOP. Say: "I cannot do X because Y. What I CAN do is Z."

6. ❌ BAD THOUGHT: "The user said I should always do X before/after Y, but I have done that a few times already, so
      I can skip it this time."
   ✅ REALITY: Skipping steps = unreliabilility, unpredictability, chaos, bugs. Always doing X when asked increases
      quality and is more efficient.
   ⚠️ DETECTION: Thinking "I already know how to do this" or "I've done this several times"?
    → STOP. That's the failure mode. Follow the checklist anyway.

7. ❌ BAD THOUGHT: "The user asked me to refactor X, but I'll just leave the old code in there so I don't break
      backwards compabilitiy".
   ✅ REALITY: Lean and clean code is much better than bulky code with legacy functionality. Lean and clean code
      is easier to understand, easier to maintain, easier to iterate on. Backwards compatibility leads to bloat,
      bugs, and technical debt.
   ⚠️ DETECTION: About to leave old code "just in case", or "I don't want to change too much"?
    → STOP. Remove it. Keep the codebase lean. Show the code you cleaned up.

8. ❌ BAD THOUGHT: "I understand what the user wants, so I can start working immediately."
   ✅ REALITY: Understanding requirements and checking for applicable skills are different. ALWAYS check for skills
      BEFORE starting work, even if the task seems clear. Skills contain proven approaches that prevent rework.
   ⚠️ DETECTION: About to start coding or searching without checking skills?
    → STOP. Run the MANDATORY FIRST RESPONSE PROTOCOL first.

9. ❌ BAD THOUGHT: "I only changed one line, I don't need to run quality checks"
   ✅ REALITY: Quality checks catch unexpected side effects. One-line changes break builds.
   ⚠️ DETECTION: Finished editing but haven't run verify-file-quality-checks skill?
    → STOP. Run it now. Show the output.
</CRITICAL>