from dataclasses import dataclass
from utils.log import setup_custom_logger


logger = setup_custom_logger()


@dataclass
class User:
    name: str
    password: str = 'secret_sauce'


users = {
    "standard": User('standard_user'),
    "locked_out": User('locked_out_user'),
    "problem": User(name='problem_user'),
    "performance_glitch": User('performance_glitch_user')
}


def get_user(name: str) -> User:
    user = users[name]
    logger.info(f"Selected {user} from {users.keys()}")
    return users[name]
