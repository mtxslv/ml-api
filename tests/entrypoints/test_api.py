import pytest
from src.service.config.logger import get_logger

from src.service.entrypoints.api import app
from tests.fakes import FakeModel, FakeRepo

logger = get_logger()

@pytest.mark.asyncio
async def test_healthcheck(client):
    response = await client.get(
        f"/healthcheck"
    )
    assert response.status_code == 200
    assert response.json() == {'message': 'API is running!'}


@pytest.mark.asyncio
async def test_predict_fake_model(client):
    # Arrange
    val_to_return = ['flower'] # model return an array
    fake_repo = FakeRepo([FakeModel(val_to_return)])

    experiment = 'my-wonderful-experiment'
    run = 'vanity-fair'
    sep_len = 1
    pet_len = 2
    sep_wid = 3
    pet_wid = 4
    url_string = f'/predict/{experiment}/{run}?sep_len={sep_len}&pet_len={pet_len}&sep_wid={sep_wid}&pet_wid={pet_wid}'
    expected_response = {'message': 'Success.','model-response': val_to_return[0]}
    with app.container.model_repo.override(fake_repo):       
        response = await client.get(url_string)
        assert response.status_code == 200
        response = response.json()
        logger.debug(response)
        assert response == expected_response

@pytest.mark.asyncio
async def test_predict(client):
    experiment = 'IRIS'
    run = 'unequaled-turtle-71'
    sep_len = 5.8
    pet_len = 2.8	
    sep_wid = 5.1	
    pet_wid = 2.4
    url_string = f'/predict/{experiment}/{run}?sep_len={sep_len}&pet_len={pet_len}&sep_wid={sep_wid}&pet_wid={pet_wid}'
    expected_response = {'message': 'Success.','model-response': 'Iris-virginica'}
    
    response = await client.get(url_string)
    assert response.status_code == 200
    response = response.json()
    logger.debug(response)
    assert response == expected_response

@pytest.mark.asyncio
async def test_predict_experiment_not_found(client):
    experiment = 'ESCLERA' # play w/ esclera vs iris
    run = 'unequaled-turtle-71'
    sep_len = 5.8
    pet_len = 2.8	
    sep_wid = 5.1	
    pet_wid = 2.4
    url_string = f'/predict/{experiment}/{run}?sep_len={sep_len}&pet_len={pet_len}&sep_wid={sep_wid}&pet_wid={pet_wid}'
    expected_response = {
        'message': 'Experiment not found.',
        'model-response': None
    }
    
    response = await client.get(url_string)
    assert response.status_code == 500
    response = response.json()
    logger.debug(response)
    assert response == expected_response

@pytest.mark.asyncio
async def test_predict_run_not_found(client):
    experiment = 'IRIS' 
    run = 'hare-running'
    sep_len = 5.8
    pet_len = 2.8	
    sep_wid = 5.1	
    pet_wid = 2.4
    url_string = f'/predict/{experiment}/{run}?sep_len={sep_len}&pet_len={pet_len}&sep_wid={sep_wid}&pet_wid={pet_wid}'
    expected_response = {
        'message': 'Run not found.',
        'model-response': None
    }
    
    response = await client.get(url_string)
    assert response.status_code == 500
    response = response.json()
    logger.debug(response)
    assert response == expected_response