import requests


class UsersCRUD:
    @staticmethod
    def get_user_data(source_url, user_id):
        user_data = requests.get(f'{source_url}/{user_id}').json()['data']
        return user_data
