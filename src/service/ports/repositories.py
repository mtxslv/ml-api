from abc import ABC, abstractmethod


class BaseRepository(ABC):
    
    @abstractmethod
    def get(self,
            experiment_id,
            run_id,
            model_id):
        raise NotImplementedError