# hangman

A simple digital version of the classic pen-and-paper
[Hangman word game](https://en.wikipedia.org/wiki/Hangman_(game)),
implemented in the
[esoteric](https://en.wikipedia.org/wiki/Esoteric_programming_language)
programming language
[Ook!](http://www.dangermouse.net/esoteric/ook.html).

## Overview

Apart from the Ook! program itself, this repo also includes an Ook! interpreter
and two Python scripts that can be used to run the game:
* [hangman.ook](hangman.ook) – This is the actual implementation of the game.
  It is about as readable as Ook! code can be – it is structured, commented
  (unfortunately not in English, sorry), and each section of the code is
  accompanied with its translation to
  [brainfuck](https://esolangs.org/wiki/Brainfuck) (I found this very helpful,
  if not essential, to keep track of what is going on).
  At the top of the file, there is also a description (in English) of how the
  program works from a user's perspective (usage instructions, game rules).
* [hangman_minified.ook](hangman_minified.ook) – The same program, in
  a "minified" form. No unnecessary comments or structuring, just the "Ook"s.
  You should find this version more readable, in the case you are an orangutan.
* [esco](esco) – The
  [EsCo (Esoteric Combine) interpreter](http://esco.sourceforge.net), in the
  form of a statically compiled x86-64 binary. It is able to interpret several
  esoteric languages, including Ook!.
* [play.py](play.py) – Python script that uses the EsCo interpreter to run
  hangman.ook. Nothing more, nothing less.
* [play_against_words_file.py](play_against_words_file.py) – Another Python
  script that runs hangman.ook using EsCo, but this one also selects a random
  word from a [words file](https://en.wikipedia.org/wiki/Words_(Unix))
  (/usr/share/dict/words by default) and provides it to the program as the word
  to guess. This results in an actual playable single-player Hangman game.

## Demonstration

This is how playing a game looks (using the script play.py):

[![play.py demonstration](demonstration.gif)](https://asciinema.org/a/258474)

## A note about Ook!

The author of the language says that "Ook! is a programming language designed
for orang-utans" [[1](http://www.dangermouse.net/esoteric/ook.html)].
An unfortunate consequence of this, as I have found out, is that it probably
shouldn't be used by humans. (It's just brainfuck, but with more masochism.)
