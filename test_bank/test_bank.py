from bank import value

def test_return_0():
    assert value("Hello")==0
    assert value("Hello, Newman")==0
def test_return_20():
    assert value("How you doing?")==20
def test_return_100():
    assert value("What's happening?")==100
    assert value("What's up?")==100