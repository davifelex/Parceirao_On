import sys
import os
from cx_Freeze import setup, Executable

# add files
files = {'Parceirao_Icon.ico', 'graphic dependencies', r"C:\Users\davif\OneDrive\Área de Trabalho\programas\Parceirão_On\venv\Lib\site-packages\PySide6\plugins"}

# target
target = Executable(
    script="Parceirao_On.py",
    base="Win32GUI",
    icon="Parceirao_Icon.ico"
)

# setup cx freeze
setup(
    name="Parceirão On",
    vercion="1.0",
    description="Programa auxiliar em setores de logistica e ou administrativos",
    author="Davi Felex Tobias",
    options= {'build_exe': {'include_files': files}},
    executables = [target]
)