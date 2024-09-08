from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def cost(self):
        pass
