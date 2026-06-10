try:
    import os
    from pynput import keyboard
    import threading
    import subprocess
    import sys
    import KITTYCONTROLCHECKER
    import asciiart
    import time
    from rich.console import Console, Group
    from rich.panel import Panel
    from pathlib import Path

    KITTYCONTROLCHECKER.CHECKLINES()
    console = Console()
    home_dir = Path.home()
    ui_lock = threading.Lock()
    home_dir_items = os.listdir(home_dir)
    currentchoice = 0
    start_view = 0
    helptoggled = False

    selection_mode = False
    selected_items = []

    def upd(e=""):
        os.system("clear")
        with ui_lock:
            global currentchoice, home_dir_items, start_view, helptoggled, selection_mode

            if not home_dir_items:
                home_dir_items = os.listdir(home_dir)

            if home_dir_items:
                currentchoice = currentchoice % len(home_dir_items)
            else:
                currentchoice = 0

            if e == "up":
                currentchoice = (currentchoice - 1) % len(home_dir_items) if home_dir_items else 0
            elif e == "down":
                currentchoice = (currentchoice + 1) % len(home_dir_items) if home_dir_items else 0

            console.clear()
            if not home_dir_items:
                console.print(Panel("Empty Directory", title=f"Directory: {home_dir}"))
            else:
                term_height = os.get_terminal_size().lines
                max_visible = max(3, term_height - (13 if helptoggled else 6))

                if currentchoice < start_view:
                    start_view = currentchoice
                elif currentchoice >= start_view + max_visible:
                    start_view = currentchoice - max_visible + 1

                items = home_dir_items[start_view: start_view + max_visible]
                display = []
                for idx, i in enumerate(items):
                    actual_idx = start_view + idx
                    target_path = home_dir / i
                    prefix = "> " if actual_idx == currentchoice else "  "
                    # Visual indicator for selected files
                    if target_path in selected_items:
                        prefix = "[*]" + prefix[2:]
                    icon = "🗁 " if target_path.is_dir() else "🗎 "
                    display.append(f"{prefix}{icon}{i}")

                console.print(Panel(Group(*display), title=f"Directory: {home_dir}"))

            if helptoggled:
                console.print(
                    Panel(Group("Up/Down - Nav", "Space - Toggle Select", "Enter - Open/Edit", "Ctrl+Enter - Parent",
                                "Ctrl+N - New File", "Ctrl+D - Delete", "Ctrl+S - Copy", "Ctrl+M - Move",
                                "Ctrl+R - Rename", "Ctrl+T - Open terminal", "Shift+H - Open readme"), title="Help"))


    def toggle_selection():
        global selection_mode, selected_items
        selection_mode = True
        target = home_dir / home_dir_items[currentchoice]
        if target in selected_items:
            selected_items.remove(target)
        else:
            selected_items.append(target)
        upd()


    def godown(e):
        with ui_lock:
            global home_dir, home_dir_items, currentchoice
            if not home_dir_items: return
            target = home_dir / home_dir_items[currentchoice]
            if target.is_dir():
                home_dir = target
                home_dir_items = os.listdir(home_dir)
                currentchoice = 0
            else:
                subprocess.run(["nano", str(target)])
        upd()


    def goup():
        with ui_lock:
            global home_dir, home_dir_items, currentchoice
            home_dir = home_dir.parent
            home_dir_items = os.listdir(home_dir)
            currentchoice = 0
        upd()


    def deletefile():
        global selected_items
        targets = selected_items if selected_items else [home_dir / home_dir_items[currentchoice]]
        for target in targets:
            if target.is_file():
                target.unlink()
            elif target.is_dir():
                target.rmdir()
        selected_items.clear()
        home_dir_items[:] = os.listdir(home_dir)
        upd()


    def triggeraction(acname, scriptpth):
        global selected_items
        targets = selected_items if selected_items else [home_dir / home_dir_items[currentchoice]]
        pythondir = Path(__file__).parent / ".venv" / "bin" / "python"
        scriptdir = Path(__file__).parent / f"{scriptpth}"

        # Process targets one by one
        for target in targets:
            command = ["kitty", "@", "launch", "--type=tab", "--tab-title", f"{acname}",
                       str(pythondir), str(scriptdir), str(target)]
            subprocess.run(command)
        selected_items.clear()
        os.system("clear")


    def mkfile(): triggeraction("Creating file", "creators.py")


    def movefile(): triggeraction("Moving file", "mover.py")


    def copyfile(): triggeraction("Copying file", "spreader.py")


    def renamefile():
        if not selected_items: triggeraction("Renaming file", "renamer.py")


    def findfiles():
        if not selection_mode: triggeraction("Finding files", "finder.py")


    def openterminal(): triggeraction("Terminal emulator", "termemulator.py")


    def viewreadme(): os.system(f"nano {Path(__file__).parent / 'README.md'}")


    def exit_app(): sys.exit(0)


    def toggle_help():
        global helptoggled
        helptoggled = not helptoggled
        upd()


    # Define hotkey handlers (some wrapped for compatibility)
    hotkeys = {
        '<up>': lambda: upd("up"),
        '<down>': lambda: upd("down"),
        '<space>': toggle_selection,
        '<enter>': lambda: godown(None),  # e param not really used
        '<ctrl>+<enter>': goup,
        '<ctrl>+d': deletefile,
        '<ctrl>+n': mkfile,
        '<ctrl>+s': copyfile,
        '<ctrl>+r': renamefile,
        '<ctrl>+m': movefile,
        '<ctrl>+f': findfiles,
        '<ctrl>+t': openterminal,
        '<ctrl>+h': toggle_help,
        '<shift>+h': viewreadme,
        '<shift>+<enter>': lambda: upd(),
        '<ctrl>+q': exit_app,
    }

    os.system("clear")
    asciiart.printart()
    print("Welcome to VaultTUI-v1.2!\nPress shift+enter to begin.")

    with keyboard.GlobalHotKeys(hotkeys) as listener:
        listener.join()

except KeyboardInterrupt:
    sys.exit(0)
except Exception as e:
    print(e)
    while True:
        pass