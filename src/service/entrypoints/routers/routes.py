from dependency_injector.wiring import Provide, inject

from fastapi import (APIRouter, Depends, Header, HTTPException, Query,
                     responses, status)

from src.service.use_cases.prediction import PredictionUseCase
from src.service.config.settings import settings

router = APIRouter()

@router.get('/healthcheck')
def healthcheck():
    return responses.JSONResponse(
        status_code = status.HTTP_200_OK,
        content = {'message': 'API is running!'}
    )

@router.get('/predict/{experiment_name}/{model_name}')
@inject
def predict(experiment_name : str,
            model_name : str, 
            predict_use_case = Depends(Provide["prediction_use_case"])):

    # preds = predict_use_case.predict()
    
    
    return responses.JSONResponse(
        status_code = status.HTTP_200_OK,
        content = {} #preds.model_dump(mode="json")
    ) 