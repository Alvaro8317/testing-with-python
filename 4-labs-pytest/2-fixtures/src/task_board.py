from enum import Enum


class Status(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class Task:
    def __init__(self, title: str, assignee: str, priority: int = 1):
        if not (1 <= priority <= 5):
            raise ValueError("La prioridad debe estar entre 1 y 5")
        self.title = title
        self.assignee = assignee
        self.priority = priority
        self.status = Status.TODO

    def __repr__(self) -> str:
        return f"Task(title={self.title!r}, status={self.status.value})"


class TaskBoard:
    """
    Tablero Kanban mínimo con tres columnas: TODO / IN_PROGRESS / DONE.
    """

    def __init__(self, name: str):
        self.name = name
        self._tasks: list[Task] = []

    # ------------------------------------------------------------------
    # Mutaciones
    # ------------------------------------------------------------------

    def add_task(self, task: Task) -> None:
        """Agrega una tarea al tablero."""
        self._tasks.append(task)

    def move(self, task: Task, new_status: Status) -> None:
        """
        Cambia el estado de una tarea.
        Lanza ValueError si la tarea no pertenece al tablero.
        """
        if task not in self._tasks:
            raise ValueError("La tarea no pertenece a este tablero")
        task.status = new_status

    def remove_done(self) -> int:
        """
        Elimina todas las tareas con estado DONE.
        Retorna la cantidad de tareas eliminadas.
        """
        before = len(self._tasks)
        self._tasks = [t for t in self._tasks if t.status != Status.DONE]
        return before - len(self._tasks)

    # ------------------------------------------------------------------
    # Consultas
    # ------------------------------------------------------------------

    def get_by_status(self, status: Status) -> list[Task]:
        return [t for t in self._tasks if t.status == status]

    def get_by_assignee(self, assignee: str) -> list[Task]:
        return [t for t in self._tasks if t.assignee == assignee]

    def count(self) -> int:
        return len(self._tasks)

    def is_empty(self) -> bool:
        return len(self._tasks) == 0

    def highest_priority_task(self) -> Task | None:
        """Retorna la tarea con mayor prioridad (número más alto). None si está vacío."""
        if not self._tasks:
            return None
        return max(self._tasks, key=lambda t: t.priority)
