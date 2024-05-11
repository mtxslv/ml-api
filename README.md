# Intro

Hi there! This repository contains a basic machine-learning based system. In summary, it has:
- [a script to train an iris classification model](./src/scripts/train.py);
- [an api to run predictions using trained models](./src/service/).

# How to Run the System (API)?

To run this project, you must have Git installed, as well as Docker.

After cloning this project:

```shell
$ git clone https://github.com/mtxslv/ml-api.git
$ cd ml-api
```
You can build the Docker image:

```shell
$ docker build . -t ml-api
```
and then run it:

```shell
$ docker run -i -p 8080:8080 ml-api
```

This will expose the system at `0.0.0.0:8080`. You can, for instance, check if the API is running by get-requesting the endpoint `0.0.0.0:8080/healthcheck`. This will return the payload:

```json
{"message": "API is running!"}
```

## Some Examples

In order to see the model running correctly, I collected some samples from the dataset, as seen below. 

Moreover, the endpoint path follows the pattern:

```python
/predict/{experiment_name}/{run_name}?sep_len={sep_len}&pet_len={pet_len}&sep_wid={sep_wid}&pet_wid={pet_wid}
```
So far, only one `experiment_name` is available: *IRIS*. Any other name will cause the system to return a payload like

```json
{
    "message": "Experiment not found.",
    "model-response": null
}
```

as well as only two `run_name` are available: *unequaled-turtle-71* and *thundering-doe-122*. Any other name will cause the system to return a payload like:

```json
{
    "message": "Run not found.",
    "model-response": null
}
```

Both runs have the same model with similar metrics. They exist just for testing purposes. That is, to exemplify how would be to change the run name during tests. 

But considering you choose the *IRIS* experiment with a valid run, you can then input the parameters (sepal and petal lengths and widths) to get the results. The column **url** has the full endpoint already filled, and the **class** column indicate the model response you'll likely receive as the answer. Such result comes in the payload

```json
{
    "message": "Success.",
    "model-response": "<a-flower-specie>"
}
```

|sepal length | petal length | sepal width | petal width | class | url |
|---|---|---|---|---|---|
|5.8|5.1 |2.8 |2.4 |IRIS-VIRGINICA | `/predict/IRIS/unequaled-turtle-71?sep_len=5.8&pet_len=5.1&sep_wid=2.8&pet_wid=2.4`|
|6.0 |4.0 |2.2 |1.0 |IRIS-VERSICOLOR | `/predict/IRIS/unequaled-turtle-71?sep_len=6.0&pet_len=4.0&sep_wid=2.2&pet_wid=1.0`|
|5.5 |1.4 |4.2 |0.2 |IRIS-SETOSA | `/predict/IRIS/unequaled-turtle-71?sep_len=5.5&pet_len=1.4&sep_wid=4.2&pet_wid=0.2`|

## See MLFlow UI by running:

If you install the libs by running

```shell
$ pip install -r full-requirements.txt
```

you can see the details discussed above (experiment name and run names) in the mlflow ui by running:

```shell
$ mlflow ui --port 8080 --backend-store-uri ./models
```

## Create a new run under IRIS experiment

In case you want to generate a new run, you can execute the following (after installing the `full-requirements.txt` dependencies):

```shell
$ python src/scripts/train.py
```

# On requirements files
- [`full-requirements.txt`](/full-requirements.txt) are meant to run anything: system, script, or notebooks and tests. It was generated using:
```shell
$ poetry export --without-hashes --with dev,data --format=requirements.txt > ./full-requirements.txt
```
- [`requirements.txt`](/requirements.txt) are meant to run the API alone. Generated with:
```shell
$ poetry export --without-hashes --format=requirements.txt > ./requirements.txt
```