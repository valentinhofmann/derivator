#!/usr/bin/python3

from derivator import Derivator


def main():

    derivator = Derivator()
    print(derivator.derive("pseudoscience"))

    s = "they allegedly love pseudoscience"

    derivator = Derivator()
    print(derivator.tokenize(s))

    derivator = Derivator(n_stems=5000)
    print(derivator.tokenize(s))


if __name__ == '__main__':
    main()
