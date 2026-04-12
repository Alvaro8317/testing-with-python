import pytest
from src import task_board


@pytest.fixture
def fxt_task() -> task_board.Task:
    return task_board.Task(title="A new task", assignee="Alvaro8317")


@pytest.fixture
def fxt_task_board() -> task_board.TaskBoard:
    return task_board.TaskBoard("A fake task board")


def test_should_add_task_to_a_task_board(
    fxt_task: task_board.Task, fxt_task_board: task_board.TaskBoard
) -> None:
    assert fxt_task_board.is_empty()
    fxt_task_board.add_task(task=fxt_task)
    assert fxt_task_board.count() == 1
    assert not fxt_task_board.is_empty()
    assert fxt_task_board.highest_priority_task() == fxt_task
