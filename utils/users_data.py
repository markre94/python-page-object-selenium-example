from dataclasses import dataclass


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
    return users[name]
