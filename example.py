#!/usr/bin/python3

from derivator import Derivator


def main():

    s = "they allegedly love pseudoscience"

    derivator = Derivator()
    print(derivator.tokenize(s.split()))

    derivator = Derivator(n_stems=5000)
    print(derivator.tokenize(s.split(), mode='bundles'))


if __name__ == '__main__':
    main()
