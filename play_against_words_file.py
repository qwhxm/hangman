#!/usr/bin/env python3

import argparse
import os
import random
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Runs hangman.ook using the bundled EsCo interpreter "
                    "and passes it a random* word from the specified words "
                    "file as the word to guess. (*Only chooses words that "
                    "consist exclusively of lower-case letters.)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--words-file",
        default="/usr/share/dict/words",
        help="words file to use")
    args = parser.parse_args()

    words = open(args.words_file).read().splitlines()
    lowercase_words = [w for w in words if w.isalpha() and w.islower()]
    word_to_guess = random.choice(lowercase_words)

    os.chdir(sys.path[0])
    subprocess.run(
        f"(echo {word_to_guess}; cat) | ./esco --quiet --type ook hangman.ook",
        shell=True,
        encoding="ascii"
    )


if __name__ == "__main__":
    main()
