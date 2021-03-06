import pytest


# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_task_stdout(capsys):
    """
    Task check
    """
    import task_4_5

    out, err = capsys.readouterr()
    correct_stdout = "['1', '3', '8']"
    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using print"
    assert (
        out.strip() == correct_stdout
    ), "Wrong line is printed to stdout"


def test_task_variables():
    """
    Checking that the required variable has been created
    in the task and contains the correct result
    """
    import task_4_5

    # variables created in the task:
    task_vars = [var for var in dir(task_4_5) if not var.startswith("_")]

    correct_result = ["1", "3", "8"]
    assert (
        "result" in task_vars
    ), "List should be written to the result variable"
    assert (
        type(task_4_5.result) == list
    ), f"The result variable must contain a list, not a {type(task_4_5.result).__name__}"
    assert (
        task_4_5.result == correct_result
    ), f"The result variable must be a list {correct_result}"
