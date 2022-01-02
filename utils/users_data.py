from dataclasses import dataclass
from enum import Enum

from utils.log import setup_custom_logger

logger = setup_custom_logger()


class UserTypes(Enum):
    STANDARD = "standard"
    LOCKED_OUT = 'locked_out'
    PROBLEM = 'problem'
    PERFORMANCE_GLITCH = 'performance_glitch'
    INVALID_DATA = "wrong"
    NO_DATA = "no_data"


@dataclass
class User:
    name: str
    password: str = 'secret_sauce'


users = {
    UserTypes.STANDARD: User('standard_user'),
    UserTypes.LOCKED_OUT: User('locked_out_user'),
    UserTypes.PROBLEM: User('problem_user'),
    UserTypes.PERFORMANCE_GLITCH: User('performance_glitch_user'),
    UserTypes.INVALID_DATA: User('wrong', 'wrong'),
    UserTypes.NO_DATA: User('', '')
}


def get_user(name: UserTypes) -> User:
    user = users[name]
    logger.info(f"Selected {user} from {list(users.keys())}")
    return user
