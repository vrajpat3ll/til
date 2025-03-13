# _Compression_: Byte Pair Encoding

> Wiki [here](https://en.wikipedia.org/wiki/Byte_pair_encoding)!

- Original version of the algorithm is focused on compression
- Slightly modified algorithm is used in _language modeling_, especially for LLMs

## Original algorithm taken from Wikipedia

Suppose the data to be encoded is

```
aaabdaaabac
```

The byte pair `aa` occurs most often, so it will be replaced by a byte that is not used in the data, such as `Z`. Now, there is the following data and replacement table:

```
ZabdZabac
Z=aa
```

Then the process is repeated with byte pair `ab`, replacing it with `Y`:

```
ZYdZYac
Y=ab
Z=aa
```

The only literal byte pair left occurs only once, and the encoding might stop here. Alternatively, the process could continue with recursive byte pair encoding, replacing `ZY` with `X`:

```
XdXac
X=ZY
Y=ab
Z=aa
```

This data cannot be compressed further by byte pair encoding because there are no pairs of bytes that occur more than once.

> [!NOTE]
> To decompress the data, simply perform the replacements in the reverse order.

## Modified algorithm

- The modified algorithm does not aim to maximally compress the text.
- It aims to encode plaintext into `tokens`, which are just natural numbers.
- All unique tokens found in a corpus (i.e. plaintext) are listed in a _token vocab_, whose size is pre-determined (100256 for GPT-3.5 and GPT-4).
- The algorithm initially treats the set of unique characters as _1-character-long n-grams_ (the initial tokens). Then, successively, the most frequent pair of adjacent tokens is merged into a new, longer n-gram and _all_ instances of the pair are replaced by this new token. This is repeated until a vocabulary of prescribed size is obtained. Note that new words can always be constructed from final vocabulary tokens and initial-set characters.

## Example for the modified algo

Suppose we are encoding the previous example of `aaabdaaabac`, with a specified vocabulary size of **6**, then it would first be encoded as `0, 0, 0, 1, 2, 0, 0, 0, 1, 0, 3` with a vocab:

```python
vocabulary = {
    "a": 0,
    "b": 1,
    "d": 2,
    "c": 3
}
```

Then it would proceed as before, and obtain `4, 5, 2, 4, 5, 0, 3` with a vocab:

```python
vocabulary = {
     "a": 0,
     "b": 1,
     "d": 2,
     "c": 3,
    "aa": 4,
    "ab": 5
}
```

So far this is essentially the same as before.

However, if we only had specified a vocabulary size of **5**, then the process would stop at

```python
vocabulary = {
     "a": 0,
     "b": 1,
     "d": 2,
     "c": 3,
    "aa": 4
}
```

so that the example would be encoded as `4, 0, 1, 2, 4, 0, 1, 0, 3`.

Conversely, if we had specified a vocabulary size of **8**, then it would be encoded as `7, 6, 0, 3`, with:

```python
vocabulary = {
        "a": 0,
        "b": 1,
        "d": 2,
        "c": 3,
       "aa": 4,
       "ab": 5,
     "aaab": 6,
    "aaabd": 7
}
```

This is not _maximally efficient_, but modified BPE **does not aim** to maximally compress a dataset, but aim to encode it efficiently for language model training.
