from textwrap import dedent, indent

from pynput.keyboard import Controller, Key

keyboard = Controller()


def run_success_keybinding(keyboard: Controller):
    keyboard.press(Key.cmd)
    keyboard.press(Key.shift)
    keyboard.press(Key.alt)
    keyboard.press("g")

    keyboard.release(Key.cmd)
    keyboard.release(Key.shift)
    keyboard.release(Key.alt)
    keyboard.release("g")


def run_failed_keybinding(keyboard: Controller):
    keyboard.press(Key.cmd)
    keyboard.press(Key.shift)
    keyboard.press(Key.alt)
    keyboard.press("b")

    keyboard.release(Key.cmd)
    keyboard.release(Key.shift)
    keyboard.release(Key.alt)
    keyboard.release("b")



def wrap_in_custom_try_except(lines :list[str]) -> list[str]:

    exception_handling = dedent(
    """
    except Exception as e:\n
        run_failed_keybinding(keyboard)\n
    else:\n
        run_success_keybinding(keyboard)\n
    """
    ).split("\n")
    wrapped_lines = [
        "try:\n",
        *[indent(line, "\t") for line in lines],
        *[s + "\n" for s in exception_handling],
    ]

    return wrapped_lines
