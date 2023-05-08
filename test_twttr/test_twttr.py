from twttr import shorten

def test_shorten():
    assert shorten("wrd") == "wrd"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50!") == "CS50!"
    assert shorten("PYTHON") == "PYTHN"
    assert shorten("CS50") == "CS50"
    assert shorten("twitter") == "twttr"
    assert shorten("Twitter") == "Twttr"

