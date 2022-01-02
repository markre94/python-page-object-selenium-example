import json
import os
from dataclasses import dataclass
from enum import Enum


class ClientTypes(Enum):
    VALID_CLIENT = 'valid_user'
    NO_DATA_CLIENT = 'no_data_user'


@dataclass
class Client:
    first_name: str
    last_name: str
    zip_code: str


def load_client_data(client_type: ClientTypes):
    with open(os.path.join('/Users/marcin94/PycharmProjects/sauce_demo_ui_tests', "data/users.json")) as user_data:
        data = json.load(user_data)
        return Client(**data[client_type.value])
