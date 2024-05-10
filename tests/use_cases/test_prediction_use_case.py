from src.service.use_cases.prediction import PredictionUseCase
from tests.fakes import FakeRepo, FakeModel

def test_prediction_use_case_init():
    # Arrange
    fake_repo = FakeRepo()

    # Act
    prediction_use_case = PredictionUseCase(model_repository=fake_repo)

    # Assert
    assert hasattr(prediction_use_case, 'model_repository')
