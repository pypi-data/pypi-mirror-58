class Helper:
    """Base Helper"""


class Git(Helper):
    """Create project from GH templates"""

    def create(self) -> None: ...

    def init(self) -> None: ...

    def login(self) -> None: ...


class Terminal(Helper):
    """Terminal Helper"""

    def get_docker_io(self) -> None: ...

    def get_docker_compose(self) -> None: ...
