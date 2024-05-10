from dependency_injector import containers, providers

from src.service.adapters.repositories import MlflowLocalRepository
from src.service.use_cases.prediction import PredictionUseCase


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules = ['src.service.use_cases.prediction',
                   'src.service.adapters.repositories'],
        packages = ['src.service.entrypoints']
    )

    model_repo = providers.Factory(MlflowLocalRepository)
    prediction_use_case = providers.Factory(
        PredictionUseCase,
        model_repository = model_repo,
    )