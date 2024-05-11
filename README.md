# Docker

## Build Docker

```shell
$ docker build . -t ml-api
```

## Run Docker

```shell
$ docker run -i -p 8080:8080 ml-api
```

## See MLFlow UI by running:

```shell
$ mlflow ui --port 8080 --backend-store-uri ./models
```

## On requirements files
- [`full-requirements.txt`](/full-requirements.txt) are meant to run anything: system, script, or notebooks and tests. It was generated using:
```shell
$ poetry export --without-hashes --with dev,data --format=requirements.txt > ./full-requirements.txt
```
- [`requirements.txt`](/requirements.txt) are meant to run the API alone. Generated with:
```shell
$ poetry export --without-hashes --format=requirements.txt > ./requirements.txt
```