import pytest
from Lyrica import get_permission
from Lyrica import get_url


def test_get_url():
    assert get_url("bellyache","billie")=="https://search.azlyrics.com/search.php?q=bellyache+billie&x=118d989895eeb850cd93fe0be9272cc623bacfe34e9911e23328565e68e5ce79"
    assert get_url("sorry","justin+bieber")=="https://search.azlyrics.com/search.php?q=sorry+justin+bieber&x=118d989895eeb850cd93fe0be9272cc623bacfe34e9911e23328565e68e5ce79"

def test_get_permission():
    assert get_permission("y")=="y"
    assert get_permission("n")=="n"

def test_get_permission():
    with pytest.raises(SystemExit):
        get_permission("sdasshj")
