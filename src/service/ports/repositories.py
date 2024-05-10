from abc import ABC, abstractmethod


class BaseRepository(ABC):
    
    @abstractmethod
    def get(self,
            uid):
        raise NotImplementedError