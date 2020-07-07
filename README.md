# Derivator

This repository contains **Derivator**, a simple algorithm for segmenting English derivatives into stem and affixes.

## Usage

You can use Derivator to segment individual words into prefixes, stem, and suffixes:

```
derivator = Derivator()
print(derivator.derive('pseudoscience'))

>> ('pseudo_', 'science', '')
``` 

You can also use Derivator to tokenize sentences:

```
derivator = Derivator()
print(derivator.tokenize('they allegedly love pseudoscience'))

>> ['they', 'allegedly', 'love', 'pseudo_', 'science']
``` 

If you are interested in specific morphological families, you can easily add them to `data/stems.txt`. 
The included list of stems is a filtered version of the BERT vocabulary,
which contains many morphologically complex words.
For a more aggressive segmentation, you can specify that Derivator should only use the `n_stems` most frequent stems:
```
derivator = Derivator(n_stems=5000)
print(derivator.tokenize('they allegedly love pseudoscience'))

>> ['they', 'alleged _ly', 'love', 'pseudo_', 'science']
``` 