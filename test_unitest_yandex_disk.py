import unittest
import requests
from unittest.mock import patch

from yandex_disk_creating import Yandex_disk


class TestYandexDiskAPI(unittest.TestCase):

    def setUp(self):
        self.yadisk_token = open("yad_token").read().strip()
        self.base_url = "https://cloud-api.yandex.net/v1/disk/resources"
        #self.folder_path = '/FolderForTests'
        self.yadisk = Yandex_disk(self.yadisk_token)

    def test_create_folder(self):
        # Тест на создание папки (может существовать или не существовать)
        folder_path = '/TestFolder'
        headers = {"Authorization": f"OAuth {self.yadisk_token}"}
        url = f"{self.base_url}?path={folder_path}"

        # Проверяем, существует ли папка перед попыткой создания
        check_existing_response = requests.head(url, headers=headers)

        if check_existing_response.status_code == 409:
            # Папка уже существует, ничего не делаем
            pass
        else:
            # Папка не существует, создаем ее
            response = requests.put(url, headers=headers)
            self.assertIn(response.status_code, [201, 409])  # Ожидаемый код ответа 201 (Created) или 409 (Conflict)

    def test_create_folder_no_authentication(self):
        # Тест на попытку создания папки без аутентификации
        folder_path = '/TestFolder'
        url = f"{self.base_url}?path={folder_path}"

        response = requests.put(url)

        self.assertEqual(response.status_code, 401)  # Ожидаемый код ответа 401 (Unauthorized)

    def test_create_folder_invalid_characters(self):
        # Тест на попытку создания папки с недопустимыми символами в имени
        folder_path = '/Folder*With@Special!Characters'
        headers = {"Authorization": f"OAuth {self.yadisk_token}"}
        url = f"{self.base_url}?path={folder_path}"

        response = requests.put(url, headers=headers)

        if response.status_code == 400:
            # Если папка не создается из-за недопустимых символов, тест считается успешным
            assert response.status_code == 400, "Папка не создана из-за недопустимых символов в имени."
        elif response.status_code == 201:
            # Если папка была создана, это считается ошибкой
            delete_url = f"{self.base_url}?path={folder_path}"
            delete_response = requests.delete(delete_url, headers=headers)
            assert delete_response.status_code == 204, f"Не удалось удалить папку. Код состояния: {delete_response.status_code}"
            print(f"Папка {folder_path} была успешно удалена.")
            assert False, f"Папка была создана, что не допустимо. Код состояния: {response.status_code}"
        else:
            # Если получен другой код состояния (например, 409), это также считается ошибкой
            delete_url = f"{self.base_url}?path={folder_path}"
            delete_response = requests.delete(delete_url, headers=headers)
            assert delete_response.status_code == 204, f"Не удалось удалить папку. Код состояния: {delete_response.status_code}"
            print(f"Папка {folder_path} уже существовала и была успешно удалена.")
            assert False, f"Не удалось создать папку. Код состояния: {response.status_code}"


    def test_create_folder_in_nonexistent_parent(self):
        # Тест на попытку создания папки в несуществующей родительской папке
        folder_path = '/NonexistentParent/TestFolder'
        headers = {"Authorization": f"OAuth {self.yadisk_token}"}
        url = f"{self.base_url}?path={folder_path}"

        response = requests.put(url, headers=headers)
        print(f"Статус кода ответа: {response.status_code}")
        self.assertTrue(response.status_code == 404 or response.status_code == 409, "Ожидалось 404 или 409")

    def test_create_folder_quota_exceeded(self):
        folder_path = '/QuotaExceededFolder'
        headers = {"Authorization": f"OAuth {self.yadisk_token}"}
        url = f"{self.base_url}?path={folder_path}"

        # Попытка создания папки
        response = requests.put(url, headers=headers)

        if response.status_code == 403:
            # Если ожидается код 403 (Forbidden), то тест считается успешным
            self.assertEqual(response.status_code, 403)
        elif response.status_code == 409:
            # Если папка уже существует (код 409 Conflict), также считается успешным
            self.assertEqual(response.status_code, 409)
        else:
            # Если получен другой код состояния, тест завершится неудачно с указанием фактического кода состояния
            self.fail(f"Непредвиденный код состояния: {response.status_code}")

    def test_create_folder_no_name(self):
        # Тест на попытку создания папки без указания имени
        folder_path = '/'
        headers = {"Authorization": f"OAuth {self.yadisk_token}"}
        url = f"{self.base_url}?path={folder_path}"

        response = requests.put(url, headers=headers)

        self.assertEqual(response.status_code, 400)  # Ожидаемый код ответа 400 (Bad Request)

    @patch('requests.put')
    def test_create_folder_server_unavailable(self, mock_put):
        # Тест на попытку создания папки при недоступности сервера
        folder_path = '/TestFolder'
        headers = {"Authorization": f"OAuth {self.yadisk_token}"}
        url = f"{self.base_url}?path={folder_path}"

        # Создаем объект, который будет имитировать ответ от сервера
        response_mock = mock_put.return_value
        response_mock.status_code = 503  # Можете использовать любой код 5xx, например 503 Service Unavailable

        response = requests.put(url, headers=headers)

        self.assertTrue(response.status_code >= 500)  # Ожидаемый код ответа 5xx

