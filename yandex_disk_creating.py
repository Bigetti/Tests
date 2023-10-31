import requests
import logging

class Yandex_disk:

    def __init__(self, yadisk_token):
        self.token = yadisk_token
        self.base_url = "https://cloud-api.yandex.net/v1/disk"
        self.folder_url = f"{self.base_url}/resources"

    def check_yadisk_token(self):
        headers = {
            "Authorization": f"OAuth {self.token}"
        }
        response = requests.get(self.base_url, headers=headers)

        return response.status_code

    def create_yadisk_folder(self, folder_path):
        #base_url = "https://cloud-api.yandex.net/v1/disk/resources"
        url = f'{self.folder_url}?path={folder_path}'

        headers = {
            'Authorization': f'OAuth {self.token}',
            'Content-Type': 'application/json',
        }

        # Проверить наличие папки перед созданием
        # check_folder_url = f'{base_url}?path={folder_path}'
        # check_response = requests.get(check_folder_url, headers=headers)

        response = requests.put(url, headers=headers)

        if response.status_code == 201:
            logging.info(f'Папка {folder_path} успешно создана.')
            print(f'Папка {folder_path} успешно создана.')
        elif response.status_code == 409:
            logging.info(f'Папка {folder_path} уже существует.')
            print(f'Папка {folder_path} уже существует.')
        else:
            logging.error(f'Не удалось создать папку. Код состояния: {response.status_code}')

        # print(F"--------------Проверяем не создана ли уже папка на Ядиске  ")
        # print(f" Смотрим какой ответ от адреса: {check_folder_url} --  {check_response.status_code}")

        # if check_response.status_code == 200:
        #     print(f'Папка {folder_path} уже существует.')
        #     return  # Папка уже существует, не нужно создавать новую
        #
        # # Если папки нет, создать её
        # response = requests.put(url, headers=headers)
        # if response.status_code == 201:
        #     print(response.status_code)
        #     print(f'Папка {folder_path} успешно создана.')
        # else:
        #     print(f'Не удалось создать папку. Код состояния: {response.status_code}')

def main():
    yadisk_token = open("yad_token").read().strip()
    yad1 = Yandex_disk(yadisk_token)
    folder_path = '/FolderForTests'

    # Проверяем работоспособность токена
    token_status = yad1.check_yadisk_token()
    if token_status == 200:
        logging.info("Токен действителен.")
    else:
        logging.error("Токен недействителен.")

    yad1.create_yadisk_folder(folder_path)

if __name__ == '__main__':
    main()