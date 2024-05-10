from pathlib import Path

import mlflow
from mlflow.client import MlflowClient

from src.service.ports.repositories import BaseRepository


class MlflowLocalRepository(BaseRepository):
    def __init__(self, uri: Path) -> None:
        mlflow.set_tracking_uri(str(uri))
        self.client = MlflowClient(
            tracking_uri=str(uri)
        )
        
    def get(self,
            experiment_name,
            run_name):
        # Get IRIS experiment
        experiments = self.client.get_experiment_by_name(experiment_name) # returns a list of mlflow.entities.Experiment

        # Now get its run
        runs = mlflow.search_runs(experiments.experiment_id)

        a_run = runs[runs['tags.mlflow.runName'] == run_name]

        if a_run.shape[0] == 0:
            # raise RunNotFound 
            pass
        else:
            model_uri = a_run.artifact_uri.to_list()[0]
            model = mlflow.sklearn.load_model(
                f'{model_uri}/model'
            )
            return model
