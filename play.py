#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Runs hangman.ook using the bundled EsCo interpreter."
    )
    parser.parse_args()

    os.chdir(sys.path[0])
    subprocess.run(
        ["./esco", "--quiet", "--type", "ook", "hangman.ook"],
        encoding="ascii"
    )


if __name__ == "__main__":
    main()
