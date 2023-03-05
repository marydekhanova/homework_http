import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token
 

    def upload(self, files: str):
        files_list = files.split(', ')
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}
        for file in files_list:
            params = {'path': f'app:/{os.path.basename(file)}', 'overwrite': 'true'}
            resp_url = requests.get(upload_url, params=params, headers=headers)
            resp_url_json = resp_url.json()
            if resp_url.status_code == 200:
                href = resp_url_json['href']
                resp_upload = requests.put(href, data=open(file, 'rb'))
                if resp_upload.status_code == 201:
                    print(f'Файл {os.path.basename(file)} был загружен без ошибок.')
                else:
                    resp_upload_json = resp_upload.json()
                    print(f'Файл {os.path.basename(file)} невозможно загрузить.\nКод ошибки: {resp_upload.status_code}.\n{resp_upload_json["message"]}')
            else:
                print(f'Файл {os.path.basename(file)} невозможно загрузить.\nКод ошибки: {resp_url.status_code}.\n{resp_url_json["message"]}')


if __name__ == '__main__':
    files = (input('Добавьте список файлов через запятую, которые необходимо загрузить: '))
    token = input('Введите ваш индивидуальный токен: ')
    uploader = YaUploader(token)
    result = uploader.upload(files)


