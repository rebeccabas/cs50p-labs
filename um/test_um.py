from um import count

def test_1():
    assert count("um")==1

def test_2():
    assert count("um?")==1

def test_3():
    assert count("Um, thanks for the album.\n")==1

def test_4():
    assert count("Um, thanks, um...\n")==2
