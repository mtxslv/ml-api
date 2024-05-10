from abc import ABC, abstractmethod


class BaseRepository(ABC):
    
    @abstractmethod
    def get(self,
            experiment_name,
            run_name):
        raise NotImplementedError