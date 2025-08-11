from twttr import shorten

def test_shorten_no_vowels():
    assert shorten("rhythm") == "rhythm"
    assert shorten("crypt") == "crypt"

def test_shorten_all_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""

def test_shorten_mixed():
    assert shorten("Hello World") == "Hll Wrld"
    assert shorten("CS50") == "CS50"
    assert shorten("Python") == "Pythn"

def test_shorten_empty():
    assert shorten("") == ""

def test_shorten_punctuation():
    assert shorten("What's up?") == "Wht's p?"
