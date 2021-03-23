import allure

from core.logger import LOGGER
from core.settings import SOURCE_URL
from methods.methods_api import UsersCRUD


class TestCRUD:
    @allure.story('Users: Get existing user data')
    def test_get_existing_user_data(self, data):
        LOGGER.info('Users: Get existing user data')
        api = UsersCRUD()
        user_data = api.get_user_data(SOURCE_URL, 86)
        assert user_data == data, \
            f'Actual user data: {user_data}\nExpected user data: {data}'
