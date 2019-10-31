import file, file_storage, file_already_exist_error
import pytest


def test_write1():
    f = file.File("1x.txt", "Письмо")
    fs = file_storage.FileStorage(5)
    assert fs.write(f) is False


def test_write2():
    f = file.File("1x.txt", "Пис")
    fs = file_storage.FileStorage(5)
    assert fs.write(f) is True


"""def test_write2():
    f = file.File("1x.txt", "Пис")
    fs = file_storage.FileStorage(5)
    fs.write(f)
    assert fs.write(f) == file_already_exist_error.FileAlreadyExistError"""


def test_is_exist1():
    f = file.File("1.txt", "Пис")
    fs = file_storage.FileStorage(5)
    fs.write(f)
    assert fs.is_exists("1.txt") is True


def tets_is_exist2():
    f = file.File("", "Пис")
    fs = file_storage.FileStorage(5)
    fs.write(f)
    assert fs.is_exists("1.txt") is False


def test_delete():
    f = file.File("1.txt", "Пис")
    fs = file_storage.FileStorage(5)
    fs.write(f)
    assert fs.delete("1.txt") is True


def test_delete2():
    fs = file_storage.FileStorage(5)
    assert fs.delete("1.txt") is False


def test_get_files():
    f = file.File("1.txt", "Пис")
    fs = file_storage.FileStorage(5)
    fs.write(f)
    assert fs.get_files == fs._files


def test_get_file():
    f = file.File("1.txt", "Пис")
    fs = file_storage.FileStorage(5)
    fs.write(f)
    assert fs.get_file("1.txt") == f


def test_get_file2():
    f = file.File("1.txt", "Пис")
    fs = file_storage.FileStorage(5)
    fs.write(f)
    assert fs.get_file("2.txt") is None


def test_get_available_size():
    f = file.File("1.txt", "Пис")
    fs = file_storage.FileStorage(5)
    fs.write(f)
    assert fs.get_available_size() == 2


def test_get_max_size():
    fs = file_storage.FileStorage(5)

    assert fs.get_max_size() == 5

