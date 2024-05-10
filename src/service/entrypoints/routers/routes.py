from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, responses, status

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

    preds = predict_use_case.predict(
        experiment_name,
        run_name,
        iris.to_2D_list()
    )
    
    return responses.JSONResponse(
        status_code = status.HTTP_200_OK,
        content = {'model-response':preds} 
    ) 