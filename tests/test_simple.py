import pytest
from pyTaguchi.taguchi import Taguchi

var1 = {
    "name": "Variable n.1",
    "values": [
        30,
        35,
        40,
    ]
}

var2 = {
    "name": "Variable n.2",
    "values": [
        20,
        30,
        40,
    ]
}

var3 = {
    "name": "Variable n.3",
    "values": [
        10,
        27,
        50,
    ]
}

var4 = {
    "name": "Variable n.4",
    "values": [
        0.2,
        0.5,
        0.7,
    ]
}


def test_4factor():
    tg = Taguchi()
    tg.add(var1)
    tg.add(var2)
    tg.add(var3)
    tg.add(var4)

    tg.run(randomize=True)
    print(tg.df)
    assert tg.FACTORS == 4
    assert len(tg.df) == 9


def test_2factor():
    tg = Taguchi()
    var1["values"].append(50)
    var2["values"].append(50)
    tg.add(var1)
    tg.add(var2)

    tg.run(randomize=True)
    print(tg.df)
    assert tg.FACTORS == 2
    assert len(tg.df) == 16
