def CHECKLINES():
    from pathlib import Path
    with open(f"{Path.home() / ".config" / "kitty" / "kitty.conf"}", "r") as f:
        lines = f.readlines()
        if "allow_remote_control yes\n" in lines:
            pass
        else:
            with open(f"{Path.home() / ".config" / "kitty" / "kitty.conf"}", "a") as f:
                f.write("allow_remote_control yes\n")
