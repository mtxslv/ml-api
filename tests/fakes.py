from src.service.ports.repositories import BaseRepository

class FakeRepo(BaseRepository):
    def __init__(self,models=[]) -> None:
        self.models = models

    def get(self,
            experiment_name,
            run_name):
        return self.models[0]
    
class FakeModel():
    def __init__(self, val_to_return) -> None:
        self.val_to_return = val_to_return

    def predict(self, X):
        return self.val_to_return