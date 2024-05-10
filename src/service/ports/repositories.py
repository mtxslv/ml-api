from abc import ABC, abstractmethod


class BaseRepository(ABC):
    
    @abstractmethod
    def get(self,
            experiment_name,
            model_name):
        raise NotImplementedError