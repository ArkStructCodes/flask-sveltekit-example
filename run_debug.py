from pathlib import Path
from subprocess import Popen, DEVNULL

from app import create_app


def main():
    Popen(
        ["npm", "run", "build", "--", "--watch"],
        cwd=Path(__file__).absolute().parent / "frontend",
        stdout=DEVNULL,
    )
    create_app().run(debug=True)


if __name__ == "__main__":
    main()
