from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, responses, status

from src.service.adapters.exceptions import ExperimentNotFound, RunNotFound
from src.service.domain.objects import IrisData
from src.service.config.logger import get_logger

router = APIRouter()
logger = get_logger()

@router.get('/healthcheck')
def healthcheck():
    return responses.JSONResponse(
        status_code = status.HTTP_200_OK,
        content = {'message': 'API is running!'}
    )

@router.get('/predict/{experiment_name}/{run_name}')
@inject
def predict(experiment_name : str,
            run_name : str, 
            sep_len : float,            
            pet_len : float,            
            sep_wid : float,
            pet_wid : float,
            predict_use_case = Depends(Provide["prediction_use_case"])):

    iris = IrisData(
        petal_length = pet_len,
        petal_width = pet_wid,
        sepal_length = sep_len,
        sepal_width = sep_wid
    )
    try:
       logger.info('Running model')
       preds = predict_use_case.predict(
           experiment_name,
           run_name,
           iris.to_2D_list()
       )
    except ExperimentNotFound:
        logger.exception(ExperimentNotFound)
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        content = {
            'message': 'Experiment not found.',
            'model-response': None
        }
    except RunNotFound:
        logger.exception(RunNotFound)
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        content = {
            'message': 'Run not found.',
            'model-response': None
        }
    except Exception as e:
        logger.exception(e)
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        content = {
            'message': 'Unexpected behaviour.',
            'model-response': None
        }
    else:
        logger.info('Prediction sucessfully.')
        status_code = status.HTTP_200_OK
        content = {
            'message': 'Success.',
            'model-response': preds[0]
        }
    finally:
        logger.info('Returning response.')
        return responses.JSONResponse(
            status_code = status_code,
            content = content
        ) 