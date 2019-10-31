import pytest
import file


def test_get_extension():
    f = file.File("w1.txt", "Поиск")
    assert f.get_extension() == "txt"


def test_get_size():
    f = file.File("w1.txt", "Поиск")
    assert f.get_size() == 5


def test_get_content():
    f = file.File("w1.txt", "Поиск")
    assert f.get_content() == "Поиск"


def test_get_filename():
    f = file.File("w1.txt", "Поиск")
    assert f.get_filename() == "w1.txt"
