from pydantic import BaseModel, Field
from typing import List

class TitleDescription(BaseModel):
    """The title and description of the dish."""
    title: str = Field(description="The title of the dish.")
    description: str = Field(description="The description of the dish.")

class Ingredient(BaseModel):
    """The ingredient of the dish."""
    name: str = Field(description="The name of the ingredient.")
    quantity: str = Field(description="The quantity of the ingredient. For example, 2 cups, 1 tsp, 500g.")

class Ingredients(BaseModel):
    items: List[Ingredient]

class Step(BaseModel):
    step_number: int = Field(description="The step number.")
    instruction: str = Field(description="A clear, step-by-step cooking direction for this stage of the recipe, specifying actions and techniques.")

class Steps(BaseModel):
    steps: List[Step] = Field(description="A sequential list of steps to prepare the recipe.")


