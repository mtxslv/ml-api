import mlflow
from sklearn.decomposition import PCA
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from ucimlrepo import fetch_ucirepo

from src.service.config.settings import settings


def get_client():
    mlflow.set_tracking_uri(str(settings.MODEL_FILE_PATH))
    client = mlflow.client.MlflowClient(
        tracking_uri=str(settings.MODEL_FILE_PATH)
    )
    return client
    
def get_metrics(y_true, y_preds):
    
    accuracy = accuracy_score(y_true, y_preds)
    f1 = f1_score(y_true, y_preds, average='weighted')
    precision = precision_score(y_true, y_preds, average = 'weighted')
    recall = recall_score(y_true, y_preds, average = 'weighted')

    metrics = {
        'accuracy': accuracy,
        'f1': f1,
        'precision': precision,
        'recall': recall
    }

    return metrics

def main():

    client = get_client()
    iris_experiment = mlflow.set_experiment("IRIS")
    mlflow.autolog()

    # DATA FETCHING
    # fetch dataset 
    iris = fetch_ucirepo(id=53) 
    
    # data (as pandas dataframes) 
    X = iris.data.features 
    y = iris.data.targets 

    # TRAIN-TEST SPLIT
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    with mlflow.start_run() as run:

        # MODEL CREATION AND TRAINING
        model = Pipeline([
            ('scaler', StandardScaler()),
            ('pca', PCA()),
            ('model', GradientBoostingClassifier())
        ])
        model.fit(X_train,y_train)

        # MODEL EVALUATION
        preds = model.predict(X_test)
        metrics = get_metrics(y_test, preds)
        mlflow.log_metrics(metrics)

if __name__ == '__main__':
    main()
    