from dependency_injector import containers, providers

from src.service.adapters.repositories import MlflowLocalRepository
from src.service.use_cases.prediction import PredictionUseCase
from src.service.config.settings import settings

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules = ['src.service.use_cases.prediction',
                   'src.service.adapters.repositories'],
        packages = ['src.service.entrypoints']
    )

    model_repo = providers.Factory(
        MlflowLocalRepository,
        uri = settings.MODEL_FILE_PATH
    )
    prediction_use_case = providers.Factory(
        PredictionUseCase,
        model_repository = model_repo,
    )