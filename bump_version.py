'''
This is a simple script that bumps version (MAJOR, MINOR, or PATCH) in the
__init__.py file and adds matching git tag to the repository.

Useage:
    python bump_version.py [major|minor|patch]

Example:
    python bump_version.py minor
'''
import argparse
from pathlib import Path
import subprocess

VERSION_FILE_PATH = Path("src/cython_package_build_example/__init__.py")

def main():
    # CHeck for uncommitted changes
    if subprocess.run(["git", "diff-index", "--quiet", "HEAD", "--"]).returncode != 0:
        # --quiet flag implies --exit-code (return 0 if no changes, 1 if changes)
        print("Uncommitted changes detected. Please commit or stash them first.")
        return

    parser = argparse.ArgumentParser()
    parser.add_argument("version", choices=["major", "minor", "patch"])
    args = parser.parse_args()

    with VERSION_FILE_PATH.open("r") as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        if line.startswith("VERSION = "):
            version_line = line
            break
    else:
        raise ValueError("Could not find VERSION line in __init__.py")
    
    version = eval(version_line.split("=")[1])
    if args.version == "major":
        version = (version[0] + 1, 0, 0)
    elif args.version == "minor":
        version = (version[0], version[1] + 1, 0)
    elif args.version == "patch":
        version = (version[0], version[1], version[2] + 1)
    else:
        raise ValueError("Unknown version type")
    
    lines[i] = f"VERSION = {version}\n"

    with VERSION_FILE_PATH.open("w") as f:
        f.writelines(lines)
    # Commit changes
    subprocess.run(["git", "add", VERSION_FILE_PATH.as_posix()])
    subprocess.run([
        "git", "commit", "-m",
        f"Bump version to {version} using bump_version.py"])

    # Add git tag
    tag = f"{'.'.join([str(x) for x in version])}"
    print(f"Adding git tag: {tag}")
    subprocess.run(["git", "tag", tag])

if __name__ == "__main__":
    main()