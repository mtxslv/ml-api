from src.service.use_cases.prediction import PredictionUseCase
from tests.fakes import FakeRepo, FakeModel

def test_prediction_use_case_init():
    # Arrange
    fake_repo = FakeRepo()

    # Act
    prediction_use_case = PredictionUseCase(model_repository=fake_repo)

    # Assert
    assert hasattr(prediction_use_case, 'model_repository')

def test_prediction_use_case_predict():
    # Arrange
    val_to_return = 'flower'
    fake_repo = FakeRepo([FakeModel(val_to_return)])

    # Act
    prediction_use_case = PredictionUseCase(model_repository=fake_repo)
    experiment_id = 'exp'
    run_id = 'a-run'
    model_uid = 'my-model'
    model_input = [[1,2,3,4]]
    ans = prediction_use_case.predict(
        experiment_id,
        run_id,
        model_uid,
        model_input
    )
   
    # Assert
    assert ans == val_to_return
