from langchain_openai import ChatOpenAI
from utils.state import State
from dotenv import load_dotenv
from utils.schema import Steps, Ingredients, TitleDescription

load_dotenv()
llm = ChatOpenAI(model='gpt-4')

def generate_title_description(state: State):
    output = llm.with_structured_output(TitleDescription).invoke(
        f"""Generate a catchy, descriptive title and a short, 
        engaging description for a unique and delicious recipe. Use 
        {state['time_of_day']} and {state['cuisine']} and {state['dietry_requirements']} as reference"""
    )

    return {"title": output.title, "description": output.description}

def generate_ingredients(state: State):
    output = llm.with_structured_output(Ingredients).invoke(
        f"""Generate a structured list of ingredients with 
        appropriate quantities for the recipe titled '{state['title']}'. 
        Take into account the dietry requirements: {state['dietry_requirements']}
        Ensure the list includes essential ingredients needed to prepare the dish."""
    )

    return {"ingredients": output.items}

def generate_steps(state: State):
    output = llm.with_structured_output(Steps).invoke(
        f"""Generate a detailed, step-by-step guide to prepare the recipe titled '{state['title']}'. 
        You can only use the ingredients: {state['ingredients']}
        Include clear instructions for each step, specifying techniques and timing as needed."""
    )

    return {"steps": output.steps}

def finalise_recipe(state: State):

    ingredients_list = [f"{ingredient.name}: {ingredient.quantity}" for ingredient in state['ingredients']]
    step_list = [f"{step.step_number}: {step.instruction}" for step in state['steps']]

    output = f"{state['title']}\n\n{state['description']}\n\nIngredients:\n\n{'\n'.join(ingredients_list)}\n\nSteps:\n\n{'\n'.join(step_list)}"

    return {"output": output}

