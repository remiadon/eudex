
Eudex: A blazingly fast phonetic reduction/hashing algorithm.
=============================================================

This is the Python port of `ticki/eudex <https://github.com/ticki/eudex>`_\ , you can install it via

.. code-block:: bash

   pip install eudex

Eudex (\ *[juːˈdɛks]*\ ) is a phonetic reduction/hashing algorithm,
providing locality sensitive "hashes" of words, based on the spelling and
pronunciation.

It is derived from the classification of the `pulmonic consonants <https://en.wikipedia.org/wiki/Pulmonic_consonant>`_.

Eudex is about two orders of magnitude faster than Soundex, and several orders
of magnitude faster than Levenshtein distance, making it feasible to run on
large sets of strings in very short time.

Example
-------

.. code-block:: python

   >>> from eudex import eudex
   >>> eudex('Jesus'), eudex('Yesus')
   (216172782115094804, 16429131440648880404)  # values in base 10 are very different
   >>> sum(1 for _ in bin(eudex('Jesus') ^ eudex('Yesus')) if _ == '1') # number of one after xoring hashes
   6  # very low distance, so words are similar !

Features
--------


* High quality locality-sensitive **hashing based on pronunciation**.
* Works with, but not limited to, English, Catalan, German, Spanish, Italian,
  and Swedish.
* Sophisticated phonetic mapping.
* Better quality than Soundex.
* Takes non-english letters into account.
* **Extremely fast**.
* Vowel sensitive.

FAQ
---

**Why aren't Rupert and Robert mapped to the same value, like in Soundex?**

Eudex is not a phonetic classifier, it is a phonetic hasher. It maps words in a
manner that exposes the difference.

**The results seems completely random. What is wrong?**

It is likely because you assume that the hashes of similar sounding words are mapped near to each
other, while they don't. Instead, their Hamming distance (i.e. XOR the values
and sum their bits) will be low.

**Does it support non-English letters?**

Yes, it supports all the C1 letters (e.g., ü, ö, æ, ß, é and so on), and it takes their respective sound into
account.

**Is it English-only?**

No, it works on most European languages as well. However, it is limited to the Latin alphabet.

**Does it take digraphs into account?**

The table is designed to encapsulate digraphs as well, though there is no separate table for these (like in
Metaphone).

**Does it replace Levenshtein?**

It is *not* a replacement for Levenshtein distance, it is a replacement for Levenshtein distance in certain use cases,
e.g. searching for spell check suggestions.

**What languages is it tested for?**

It is tested on the English, Catalan, German, Spanish, Swedish, and Italian dictionaries, and has been confirmed to have decent to good quality on all of them.

Implementations
---------------


* Python: this repository
* Rust: `ticki/eudex <https://github.com/ticki/eudex>`_
* Java: `jprante/elasticsearch-analysis-phonetic-eudex <https://github.com/jprante/elasticsearch-analysis-phonetic-eudex>`_
* JavaScript: `Yomguithereal/talisman <https://github.com/Yomguithereal/talisman/blob/master/src/phonetics/eudex.js>`_

How does Eudex work ?
---------------------

see `how_it_works.md <how_it_works.md>`_

----

`Credits`: This README was build based on the [ticki/eudex](https://github.com/ticki/eudex) README
