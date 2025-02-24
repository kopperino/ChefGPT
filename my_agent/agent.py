from langgraph.graph import StateGraph, END, START
from utils.state import State
from utils.nodes import generate_ingredients, generate_steps, generate_title_description, finalise_recipe

graph = StateGraph(State)

graph.add_node(generate_title_description)
graph.add_node(generate_steps)
graph.add_node(generate_ingredients)
graph.add_node(finalise_recipe)

graph.add_edge(START, "generate_title_description")
graph.add_edge("generate_title_description", "generate_ingredients")
graph.add_edge("generate_ingredients", "generate_steps")
graph.add_edge("generate_steps", "finalise_recipe")
graph.add_edge("finalise_recipe", END)

compiled_graph = graph.compile()

