from abc import ABC, abstractmethod


class FastAPIControllerInterface(ABC):
    @abstractmethod
    def execute(self) -> dict:
        pass
