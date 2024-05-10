from typing import List

from pydantic import BaseModel, Field


class IrisData(BaseModel):
    """ Iris flowers information. """
    petal_length: float = Field(..., description="Length of the petal in centimeters")
    petal_width: float = Field(..., description="Width of the petal in centimeters")
    sepal_length: float = Field(..., description="Length of the sepal in centimeters")
    sepal_width: float = Field(..., description="Width of the sepal in centimeters")

    def to_2D_list(self) -> List[List[float]]:
        """Return data following experiment feature order.
        That is: sepal length, sepal width, petal length, and petal width.

        Returns
        -------
        List[List[float]]
            Iris Data following experiment feature order.
        """
        return [
            [
                self.sepal_length,
                self.sepal_width,                
                self.petal_length,
                self.petal_width,
            ]
        ]