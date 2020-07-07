# Derivator

This repository contains **Derivator**, a simple algorithm for segmenting English derivatives into stem and affixes.

## Usage

You can use Derivator to segment individual words into prefixes, stems, and suffixes:

```
derivator = Derivator()
print(derivator.derive('pseudoscience'))

>> ('pseudo_', 'science', '')
``` 

You can also use Derivator to tokenize sentences:

```
derivator = Derivator()
print(derivator.derive('they allegedly love pseudoscience'))

>> ['they', 'allegedly', 'love', 'pseudo_', 'science']
``` 

