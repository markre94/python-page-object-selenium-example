import requests
from utils.log import setup_custom_logger

logger = setup_custom_logger()


class LinkResponse:
    def __init__(self, url):
        self.url = url
        self.response = None

    @property
    def status_code(self):
        if self.response:
            return self.response.status_code

    def request_head(self):
        self.response = requests.head(self.url)

    def is_link_broken(self):
        result = self.response.status_code != 200
        if result:
            logger.error(f"Link {self.url} is broken. Status code of the response is {self.response.status_code}")
        else:
            logger.info(f"Link {self.url} is OK.")

        return result

    def get_link_response(self):
        return requests.head(self.url).status_code
