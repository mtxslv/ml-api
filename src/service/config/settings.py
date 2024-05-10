from pathlib import Path


class Settings: 
    API_VERSION: str = "0.1.0"
    FASTAPI_DEBUG: str = "False"
    FASTAPI_DESCRIPTION: str = "Prediction service."
    FASTAPI_TITLE: str = "Model Service"
    LOG_FORMAT: str = (
        '%(asctime)s %(levelname)s %(filename)s::%(lineno)d::%(message)s'
    ) 
    MODEL_FILE_PATH: Path = Path(__name__).resolve().parents[0] / 'models'

settings = Settings()