import pytest
from src.service.domain.objects import IrisData

def test_iris_data_attributes():
    # Create an instance of IrisData
    iris = IrisData(
        petal_length=1.5,
        petal_width=0.5,
        sepal_length=5.1,
        sepal_width=3.5
    )
    
    # Check if the instance has the expected attributes
    assert hasattr(iris, 'petal_length')
    assert hasattr(iris, 'petal_width')
    assert hasattr(iris, 'sepal_length')
    assert hasattr(iris, 'sepal_width')
    
def test_iris_data_values():
    # Create an instance of IrisData
    iris = IrisData(
        petal_length=1.5,
        petal_width=0.5,
        sepal_length=5.1,
        sepal_width=3.5
    )
    
    # Check if the values of attributes are correct
    assert iris.petal_length == 1.5
    assert iris.petal_width == 0.5
    assert iris.sepal_length == 5.1
    assert iris.sepal_width == 3.5

def test_iris_data_to_list():
    # Create an instance of IrisData
    iris = IrisData(
        petal_length=1.5,
        petal_width=0.5,
        sepal_length=5.1,
        sepal_width=3.5
    )

    assert iris.to_2D_list() == [[5.1, 3.5, 1.5, 0.5]]