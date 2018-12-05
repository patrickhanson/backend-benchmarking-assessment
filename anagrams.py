#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "patrickhanson"

import sys


def alphabetize(string):
    return "".join(sorted(string.lower()))


def find_anagrams(words):

    anagrams = {}
    for word in words:
        a_word = alphabetize(word)
        if a_word not in anagrams:
            anagrams[a_word] = [word]
        else:
            anagrams[a_word].append(word)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Please specify a word file!"
        sys.exit(1)
    else:
        with open(sys.argv[1], 'r') as handle:
            words = handle.read().split()
            print find_anagrams(words)
