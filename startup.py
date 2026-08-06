import os
import shutil


file_path = os.path.abspath(
    "main.py"
)


startup_folder = os.path.join(
    os.getenv("APPDATA"),
    r"Microsoft\Windows\Start Menu\Programs\Startup"
)


shortcut = os.path.join(
    startup_folder,
    "Reven_AI.bat"
)


with open(shortcut,"w") as f:

    f.write(
        f'python "{file_path}"'
    )


print(
    "K AI added to startup"
)