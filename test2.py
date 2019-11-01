import file, file_storage, file_already_exist_error
import pytest


class Test2:
    def test_write1(self):
        """
        Проверка на запись с большим количеством символов
        """
        f = file.File("1x.txt", "Письмо")
        fs = file_storage.FileStorage(5)
        assert fs.write(f) is False

    def test_write2(self):
        """
        Проверка на запись с меньшим количеством символов
        """
        f = file.File("1x.txt", "Пис")
        fs = file_storage.FileStorage(5)
        assert fs.write(f) is True

    def test_write3(self):
        """
        Проверка на запись с тем же количеством символов, что и количество памяти
        """
        f = file.File("1x.txt", "Писмо")
        fs = file_storage.FileStorage(5)
        assert fs.write(f) is True

    def test_write4(self):
        """
        Проверка на запись уже имеющегося в списке
        """
        f = file.File("1x.txt", "Пис")
        fs = file_storage.FileStorage(5)
        fs.write(f)
        with pytest.raises(file_already_exist_error.FileAlreadyExistError):
            fs.write(f)

    def test_is_exist1(self):
        """
        Проверка на наличие файла
        """
        f = file.File("1.txt", "Пис")
        fs = file_storage.FileStorage(5)
        fs.write(f)
        assert fs.is_exists("1.txt") is True

    def test_is_exist2(self):
        """
        Проверка списка на наличие файла, которого нет.
        """
        f = file.File("", "Пис")
        fs = file_storage.FileStorage(5)
        fs.write(f)
        assert fs.is_exists("1.txt") is False

    def test_delete(self):
        """
        Проверка на удаление имеющегося файла
        """
        f = file.File("1.txt", "Пис")
        fs = file_storage.FileStorage(5)
        fs.write(f)
        assert fs.delete("1.txt") is True

    def test_delete2(self):
        """
        Проверка на удаление файла, которого нет в списке
        """
        fs = file_storage.FileStorage(5)
        assert fs.delete("1.txt") is False

    def test_get_files(self):
        """
        Проверка на возврат списка в котором есть что-либо
        """
        f = file.File("1.txt", "Пис")
        fs = file_storage.FileStorage(5)
        fs.write(f)
        assert fs.get_files() == fs._files

    def test_get_files2(self):
        """
        Проверка на возврат с более чем 1 экземпляром
        """
        f = file.File("1.txt", "Пис")
        f2 = file.File("2.txt", "Ми")
        fs = file_storage.FileStorage(5)
        fs.write(f)
        fs.write(f2)
        assert fs.get_files() == fs._files

    def test_get_file(self):
        """
        Проверка на возврат имеющегося экземпляра
        """
        f = file.File("1.txt", "Пис")
        fs = file_storage.FileStorage(5)
        fs.write(f)
        assert fs.get_file("1.txt") == f

    def test_get_file2(self):
        """
        Проверка на возврат отсутствуещего экземпляра
        """
        f = file.File("1.txt", "Пис")
        fs = file_storage.FileStorage(5)
        fs.write(f)
        assert fs.get_file("2.txt") is None

    def test_get_file3(self):
        """
        Проверка на возврат если в списке больше 1 экземпляра
        """
        f = file.File("1.txt", "Пис")
        f2 = file.File("2.txt", "Ми")
        fs = file_storage.FileStorage(100)
        fs.write(f)
        fs.write(f2)
        assert fs.get_file("2.txt") == f2

    def test_get_available_size(self):
        """
        Проверка на корректное оторбражение оставшегося места
        """
        f = file.File("1.txt", "Пис")
        fs = file_storage.FileStorage(5)
        fs.write(f)
        assert fs.get_available_size() == 2

    def test_get_max_size(self):
        """
        Проверка на значение максимального размера хранилища
        """
        fs = file_storage.FileStorage(5)
        assert fs.get_max_size() == 5


