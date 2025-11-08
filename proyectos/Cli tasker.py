#// ================================
#// 🟢 MODELO DE DATOS (POO)
#// ================================

class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
        self.projects: list[Project] = []
    
    def add_project(self, project: "Project"): # type: ignore
        self.projects.append(project)
    def get_project_by_name(self, name: str):
        name_l = name.strip().lower()
        for p in self.projects:
            if p.name.strip().lower() == name_l:
                return p
        return None
    def get_project_by_id(self, pid: int):
        for p in self.projects:
            if p.id == pid:
                return p.id
        return None

class Project:
    def __init__(self, id: int, name:str, owner: User): # type: ignore class User
        self.id = id
        self.name = name
        self.owner = owner
        self.tasks: list[Task] = [] # type: ignore
    
    def add_task(self, task: "Task"): # type: ignore
        self.task.append(self, task)
    
    def list_tasks(self, filtro: dict): # filter: status//priority//text
        res = list[self.tasks]
        status = filtro.get("status")
        priority = filtro.get("priority")
        text = (filtro.get("text") or "").strip().lower()
        
        if status in filtro:
            res = [t for t in res if t.status == status]
        if priority in filtro:
            res = [t for t in res if t.priority == priority]
        if text in filtro:
            res = [t for t in res if text in t.title.lower() or text in t.description.lower()]
        return res
    def get_task_by_id(self, task_id: int):
        for t in self.tasks:
            if t.id == task_id:
                return t.id
        return None
class Task:
    def __init__(self, id: int, tile: str, description: str, priority: str, status: str):
        self.id = id
        self.title = tile
        self.description = description
        self.priority = priority # valid prioritys = "low" // "mid" // "high"
        self.status = "todo" # valid status = "todo" // "doing" // "done"
        # created at fecha - hora
        self.history: list[str] = [] # Registro de cambios
    
    def start(self):
        if self.status == "todo":
            Task.change_status("doing")
    def complete(self):
        Task.change_status("done")
    def change_status(self, new_status : str):
        valid_status = ["todo", "doing", "done"]
        if new_status in valid_status:
            if self.status == "todo" and new_status == "done":
                raise ValueError(f"No puedes saltar de {self.status} a {new_status} directamente")
            
        else:
            raise ValueError(f"El estado {new_status} no es un estado valido (todo, doing, done)")
        
        old_status = self.status
        self.status = new_status

        self.add_history(f"El estado ha cambiado de {old_status} a {new_status}")

    def add_history(self, entry: str):
        self.history.append(entry)