from dataclasses import dataclass
import json


@dataclass
class Client:
    first_name: str
    last_name: str
    zip_code: int


def load_client_data():
    with open("../data/users.json") as user_data:
        data = json.load(user_data)
        return Client(**data['valid_user'])
