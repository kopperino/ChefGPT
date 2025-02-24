from typing_extensions import TypedDict, Annotated

class State(TypedDict):
    cuisine: str
    time_of_day: str
    dietry_requirements: str

    title: str
    description: str
    ingredients: str
    steps: str
    output: str

