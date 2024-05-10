from pydantic import BaseModel, Field

class IrisData(BaseModel):
    """ Iris flowers information. """
    petal_length: float = Field(..., description="Length of the petal in centimeters")
    petal_width: float = Field(..., description="Width of the petal in centimeters")
    sepal_length: float = Field(..., description="Length of the sepal in centimeters")
    sepal_width: float = Field(..., description="Width of the sepal in centimeters")
