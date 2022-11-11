'''
Clears *.c files and the *.egg-info directory from the src directory.
'''
from pathlib import Path
import shutil

def main():
    src = Path("src")
    for path in src.rglob("*.c"):
        path.unlink()
    for path in src.glob("*.egg-info"):
        shutil.rmtree(path)

if __name__ == "__main__":
    main()