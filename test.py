import pytest
import file


class Test:
    def test_get_extension(self):
        """
        Проверка на опредение расширения, если расширение в наличии
        """
        f = file.File("w1.txt", "Поиск")
        assert f.get_extension() == "txt"

    def test_get_extension2(self):
        """
        Проверка на опредение расширения, если расширения нет
        """
        f = file.File("w1", "Поиск")
        assert f.get_extension() == ""

    def test_get_size(self):
        """
        Проверка на корректное определение размера при условии его наличия
        """
        f = file.File("w1.txt", "Поисковик")
        assert f.get_size() == 9

    def test_get_size2(self):
        """
        Проверка на корректное определение размера при условии его отсутсвия
        """
        f = file.File("w1.txt", "")
        assert f.get_size() == 0

    def test_get_content(self):
        """
        Проверка на корректное возвращение содержимого файла
        """
        f = file.File("w1.txt", "Поиск")
        assert f.get_content() == "Поиск"

    def test_get_content2(self):
        """
        Проверка на корректное возвращение содержимого файла после вызова get_extension
        """
        f = file.File("w1.txt", "Поиск")
        f.get_extension()
        assert f.get_content() == "Поиск"

    def test_get_filename(self):
        """
        Проверка на корректное возвращение имени файла
        """
        f = file.File("w1.txt", "Поиск")
        assert f.get_filename() == "w1.txt"
