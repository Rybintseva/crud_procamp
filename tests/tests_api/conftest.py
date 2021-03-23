import json
from os.path import sep

import pytest

from core import config


@pytest.fixture(scope='session')
def data():
    with open(config.HOME_PATH + sep + 'data' + sep + 'test_data.json',
              encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data
