from pathlib import Path

import mlflow
from mlflow.client import MlflowClient

from src.service.adapters.exceptions import ExperimentNotFound, RunNotFound
from src.service.ports.repositories import BaseRepository


class MlflowLocalRepository(BaseRepository):
    def __init__(self, uri: Path) -> None:
        mlflow.set_tracking_uri(str(uri))
        self.uri = uri
        self.client = MlflowClient(
            tracking_uri=str(uri)
        )
        
    def get(self,
            experiment_name,
            run_name):
        # Get IRIS experiment
        experiments = self.client.get_experiment_by_name(experiment_name) # returns a list of mlflow.entities.Experiment
        
        if experiments is None:
            raise ExperimentNotFound

        # Now get its run
        runs = mlflow.search_runs(experiments.experiment_id)

        a_run = runs[runs['tags.mlflow.runName'] == run_name]

        if a_run.shape[0] == 0:
            raise RunNotFound 

        model_uri = Path(a_run.artifact_uri.to_list()[0])
        uri_parts = model_uri.parts[-3:] # experiment-id / run-id / artifacts
        full_uri = self.uri / '/'.join(uri_parts) / 'model'
        model = mlflow.sklearn.load_model(
            str(full_uri)
        )
        return model
