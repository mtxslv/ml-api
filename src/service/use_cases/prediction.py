import typing
from src.service.ports.repositories import BaseRepository


class PredictionUseCase:
    def __init__(self,
                 model_repository: BaseRepository):
        """Initialize the PredictionUseCase with a model repository.

        Parameters
        ----------
        model_repository : BaseRepository
            The repository containing the ML models.
        """
        self.model_repository = model_repository

    def predict(self,
                model_uid: str,
                input: typing.Any) -> typing.Any:
        """Make a prediction using the specified model.

        Parameters
        ----------
        model_uid : str
            The unique identifier of the model to use for prediction.
        input : typing.Any
            The input data for making the prediction.

        Returns
        -------
        typing.Any
            The prediction result.
        """
        model = self.model_repository.get(model_uid)
        result = model.predict(input)
        return result
