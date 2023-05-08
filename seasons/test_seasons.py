from seasons import convert
import pytest

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("January 18, 2000")

def test4():
    with pytest.raises(SystemExit):
        convert("2029-10-24")
cd
def test3():
    with pytest.raises(ValueError):
        convert("2000-24-10")