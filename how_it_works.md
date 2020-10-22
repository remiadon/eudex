The algorithm itself is fairly simple. It outputs an 8 byte array (an unsigned
64 bit integer):

```
A00BBBBB
||/\___/
||   |
||  Trailing phones
||
|Padding
|
First phone
```

The crucial point here is that all the characters are mapped through a table
carefully derived by their phonetic classification, to make **similar sounding
phones have a low Hamming distance**.

The tables are what makes it interesting. There are four tables:
- one for ASCII letters (not characters, letters) in the first slot ('A')
- one for C1 (Latin Supplement) characters in the first slot,
- one for ASCII letters in the trailing phones
- one for the C1 (Latin Supplement) characters for the trailing phones.

There is a crucial **distinction between consonants and vowels** in Eudex. The
first phone treat vowels as first-class citizens by making distinctions between
all the properties of vowels. The trailing phones only have a distinction
between open and close vowels.


## Trailing phones

Let's start with the tables for the trailing characters. **Consonants' bytes are
treated such that each bit represent a property of the phone** (i.e.,
pronunciation) with the exception of the rightmost bit, which is used for
tagging duplicates (it acts as a discriminant).

Let's look at the classification of IPA consonants
<p align="center">
  <img width="60%" src="https://upload.wikimedia.org/wikipedia/commons/5/5e/IPA_consonants_2005.png">
</p>

As you may notice, characters often represent more than one phone, and
reasoning about which one a given character in a given context represents can
be very hard.

---------------

Now, every good phonetic hasher should be able to segregate important
characters (e.g., hard to mispell, crucial to the pronunciation of the word)
from the rest. Therefore we add a category we call "confident", this will
occupy the most significant bit. In our category of "confident" characters we
put l, r, x, z, and q, since these are either:

1. Crucial to the sound of the word (and thus easier to hear, and harder to
   misspell).
2. Rare to occur, and thus statistically harder to mistake.

So our final trailing consonant table looks like:

| Position | Modifier | Property     | Phones                   |
|----------|---------:|--------------|:------------------------:|
| 1        | 1        | Discriminant | (for tagging duplicates) |
| 2        | 2        | Nasal        | mn                       |
| 3        | 4        | Fricative    | fvsjxzhct                |
| 4        | 8        | Plosive      | pbtdcgqk                 |
| 5        | 16       | Dental       | tdnzs                    |
| 6        | 32       | Liquid       | lr                       |
| 7        | 64       | Labial       | bfpv                     |
| 8        | 128      | Confident¹   | lrxzq                    |

**The more "important" the characteristic is to the phone's sound the higher
place it has.**

Vowels are divided them into two categories: open and close.
Not all vowels fall into these categories, therefore we will simply place it
in the category it is "nearest to", e.g. a, (e), o gets 0 for "open".

So our final ASCII letter table for the trailing phones looks like:

```
                (for consonants)
      +--------- Confident
      |+-------- Labial
      ||+------- Liquid
      |||+------ Dental
      ||||+----- Plosive
      |||||+---- Fricative
      ||||||+--- Nasal
      |||||||+-- Discriminant
      ||||||||
   a* 00000000
   b  01001000
   c  00001100
   d  00011000
   e* 00000001
   f  01000100
   g  00001000
   h  00000100
   i* 00000001
   j  00000101
   k  00001001
   l  10100000
   m  00000010
   n  00010010
   o* 00000000
   p  01001001
   q  10101000
   r  10100001
   s  00010100
   t  00011101
   u* 00000001
   v  01000101
   w  00000000
   x  10000100
   y* 00000001
   z  10010100
             |  (for vowels)
             +-- Close
```

Now, we extend our table to C1 characters by the same method:
```
                (for consonants)
      +--------- Confident
      |+-------- Labial
      ||+------- Liquid
      |||+------ Dental
      ||||+----- Plosive
      |||||+---- Fricative
      ||||||+--- Nasal
      |||||||+-- Discriminant
      ||||||||
   ß  -----s-1  (use 's' from the table above with the last bit flipped)
   à  00000000
   á  00000000
   â  00000000
   ã  00000000
   ä  00000000  [æ]
   å  00000001  [oː]
   æ  00000000  [æ]
   ç  -----z-1  [t͡ʃ]
   è  00000001
   é  00000001
   ê  00000001
   ë  00000001
   ...
   ...
             |  (for vowels)
             +-- Close
```


## First phone
So far we have considered the trailing phones, now we need to look into the
first phone. The first phone needs **a table with minimal collisions, since you
hardly ever misspell the first letter in the word**. Ideally, the table should be
injective, but due to technical limitations it is not possible.

We will use the first bit to distinguish between vowels and consonants.

First: the consonants. To avoid repeating ourselves, we will use a
method for reusing the above tables.

Since the least important property is placed to the left, we will simply shift
it to the right (that is, truncating the rightmost bit). The least significant
bit will then be flipped when encountering a duplicate. This way we preserve
the low Hamming distance, while avoiding collisions.

The vowels are more interesting. We need a way to distinguish between vowels
and their sounds.

Luckily, their classification is quite simple

<p align="center">
  <img width="50%" src="https://upload.wikimedia.org/wikipedia/en/5/5a/IPA_vowel_chart_2005.png">
</p>

If a vowel appears as two phones (e.g., dependent on language), we OR them, and
possibly modify the discriminant if it collides with another phone.

We need to divide each of the axises into more than two categories, to utilize
all our bits, so some properties will have to occupy multiple bits.

| Position | Modifier | Property (vowel)    |
|----------|---------:|---------------------|
| 1        | 1        | Discriminant        |
| 2        | 2        | Is it open-mid?     |
| 3        | 4        | Is it central?      |
| 4        | 8        | Is it close-mid?    |
| 5        | 16       | Is it front?        |
| 6        | 32       | Is it close?        |
| 7        | 64       | More close than [ɜ] |
| 8        | 128      | Vowel?              |


### Computing distances

Now that we have our tables. We now need the distance operator. A naïve
approach would be to simply use Hamming distance. This has the disadvantage of
all the bytes having the same weight, which isn't ideal, since you are more
likely to misspell later characters, than the first ones.

For this reason, we use weighted Hamming distance:

| Byte:   |   1 |   2  |   3  |   4  |  5  |  6  | 7  | 8 |
|:--------|----:|-----:|-----:|-----:|----:|----:|---:|--:|
| Weight: | 128 |  64  |  32  |  16  |  8  |  4  | 2  | 1 |

Namely, we XOR the two values and then add each of the bytes' Hamming weight,
using the coefficients from the table above.

This gives us a high quality word metric.

--------------------

`Credits`: This README was build based on the [ticki/eudex](https://github.com/ticki/eudex) README