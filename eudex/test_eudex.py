from .core import eudex

EUDEX_EXACT = [
    ("JAva", "jAva"),
    ("co!mputer", "computer"),
    ("comp-uter", "computer"),
    ("comp@u#te?r", "computer"),
    ("lal", "lel"),
    ("rindom", "ryndom"),
    ("riiiindom", "ryyyyyndom"),
    ("riyiyiiindom", "ryyyyyndom"),
    ("triggered", "TRIGGERED"),
    ("repert", "ropert"),
]

EUDEX_MISMATCH = [
    ("reddit", "eddit"),
    ("lol", "lulz"),
    ("ijava", "java"),
    ("jesus", "iesus"),
    ("aesus", "iesus"),
    ("iesus", "yesus"),
    ("rupirt", "ropert"),
    ("ripert", "ropyrt"),
    ("rrr", "rraaaa"),
    ("randomal", "randomai"),
]


def test_eudex_exact():
    for a, b in EUDEX_EXACT:
        assert eudex(a) == eudex(b)


def test_eudex_mismatch():
    for a, b in EUDEX_MISMATCH:
        assert eudex(a) != eudex(b)


def test_eudex_hash():
    assert eudex("Guillaume") == 288230378836066816
    assert eudex("Antoine") == 9511602490802442752
    assert eudex("Carole") == 432345566928740352
