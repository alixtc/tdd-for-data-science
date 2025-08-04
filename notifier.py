from textwrap import dedent, indent

from IPython.core.interactiveshell import ExecutionResult, InteractiveShell
from pynput.keyboard import Controller, Key

keyboard = Controller()


def run_success_keybinding(keyboard: Controller = keyboard):
    keyboard.press(Key.cmd)
    keyboard.press(Key.shift)
    keyboard.press(Key.alt)
    keyboard.press("g")

    keyboard.release(Key.cmd)
    keyboard.release(Key.shift)
    keyboard.release(Key.alt)
    keyboard.release("g")


def run_failed_keybinding(keyboard: Controller = keyboard):
    keyboard.press(Key.cmd)
    keyboard.press(Key.shift)
    keyboard.press(Key.alt)
    keyboard.press("b")

    keyboard.release(Key.cmd)
    keyboard.release(Key.shift)
    keyboard.release(Key.alt)
    keyboard.release("b")


def wrap_in_custom_try_except(lines: list[str]) -> list[str]:

    beginning, end = dedent(
        """
    from notifier import (\n
        keyboard,\n
        run_failed_keybinding,\n
        run_success_keybinding,\n
    )\n
    try:\n
    {{placeholder}}
    except Exception as e:\n
        run_failed_keybinding(keyboard)\n
        raise e\n
    else:\n
        run_success_keybinding(keyboard)\n
    """
    ).split("{{placeholder}}")

    wrapped_lines = [
        *[s + "\n" for s in beginning.splitlines()],
        *[indent(line, "\t") for line in lines],
        *[s + "\n" for s in end.splitlines()],
    ]

    return wrapped_lines


class VarWatcher:
    def __init__(self, ip: InteractiveShell):
        self.shell = ip

    def post_run_cell(self, result: ExecutionResult):

        if result.error_in_exec is not None:
            run_failed_keybinding()
        else:
            run_success_keybinding()


def load_ipython_extension(ip: InteractiveShell):
    vw = VarWatcher(ip)
    ip.events.register("post_run_cell", vw.post_run_cell)
