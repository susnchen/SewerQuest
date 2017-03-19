from cx_Freeze import setup, Executable

setup(
    name = "Cat Game Meow",
    description = "a cat game.",
    executables = [Executable("main.py", base="Win32GUI")],
)