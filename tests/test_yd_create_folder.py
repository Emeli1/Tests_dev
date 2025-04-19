import requests
import pytest

class TestYandexCreateFolder:
    def setup_method(self) -> None:
        self.headers = {
            'Authorization': 'токен'
        }

    @pytest.mark.parametrize(
        'path, folder_name, status',
        (
            ('path', 'New_folder', 201),
            ('path', 'New_folder', 409),
            ('patth', 'Music', 400)

        )
    )
    def test_create_folder(self, path, folder_name, status):
        params = {
            path: folder_name,
        }

        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)

        assert response.status_code == status

