from abc import ABC, abstractmethod

class AARepo(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def aa_method(self):
        pass
