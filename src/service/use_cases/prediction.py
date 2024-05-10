import typing
from src.service.ports.repositories import BaseRepository


class PredictionUseCase:
    def __init__(self,
                 model_repository: BaseRepository) -> None:
        self.model_repository = model_repository

    def predict(self,
                model_uid: str,
                input: typing.Any) -> typing.Any:
        model = self.model_repository.get(model_uid)
        ans = model.predict(input)
        return ans