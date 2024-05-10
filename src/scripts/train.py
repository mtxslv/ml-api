import mlflow
from sklearn.decomposition import PCA
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import f1_score
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
    
def main():
    client = get_client()
    iris_experiment = mlflow.set_experiment("IRIS")

    # DATA FETCHING
    # fetch dataset 
    iris = fetch_ucirepo(id=53) 
    
    # data (as pandas dataframes) 
    X = iris.data.features 
    y = iris.data.targets 

    # TRAIN-TEST SPLIT
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    # MODEL CREATION AND TRAINING
    model = Pipeline([
        ('scaler', StandardScaler()),
        ('pca', PCA()),
        ('model', GradientBoostingClassifier())
    ])
    model.fit(X_train,y_train)

    # MODEL EVALUATION
    preds = model.predict(X_test)
    f1_score(y_test, preds, average='weighted')    

if __name__ == '__main__':
    main()
    