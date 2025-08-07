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


class VarWatcher:
    def __init__(self, ip: InteractiveShell):
        self.shell = ip

    def post_run_cell_if_flagged(self, result: ExecutionResult):
        """If the '_notify_on_next_cell' flag is set, send a notification."""
        # Part required to turn off VS-jupyter-extension that pseudo-run cells
        info = result.info
        if info.cell_id is None:
            return

        if result.error_in_exec is not None:
            run_failed_keybinding()
        elif result.info:
            run_success_keybinding()


def load_ipython_extension(ip: InteractiveShell):
    """
    Load the extension in IPython.
    """
    vw = VarWatcher(ip)
    ip.events.register("post_run_cell", vw.post_run_cell_if_flagged)
