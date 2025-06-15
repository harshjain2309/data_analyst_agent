# tools.py
from langchain.agents import Tool
import pandas as pd
import matplotlib.pyplot as plt

# Global placeholder to hold uploaded DataFrame
DATAFRAMES = {}

def inspect_dataframe(query: str) -> str:
    if not DATAFRAMES:
        return "No DataFrame uploaded yet."
    
    df = list(DATAFRAMES.values())[0]  # assume one DataFrame for simplicity
    try:
        if "describe" in query.lower():
            return str(df.describe())
        elif "columns" in query.lower():
            return str(df.columns.tolist())
        elif "head" in query.lower():
            return str(df.head())
        else:
            return "Question not recognized. Try 'describe', 'columns', or 'head'."
    except Exception as e:
        return f"Error: {e}"

def generate_plot(x_col, y_col) -> str:
    if not DATAFRAMES:
        return "No DataFrame uploaded yet."

    df = list(DATAFRAMES.values())[0]
    try:
        plt.figure(figsize=(8, 5))
        plt.plot(df[x_col], df[y_col])
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f"{y_col} vs {x_col}")
        plt.grid()
        plot_path = "plot.png"
        plt.savefig(plot_path)
        return plot_path
    except Exception as e:
        return f"Plotting error: {e}"

# Register as LangChain tools
tools = [
    Tool(
        name="dataframe_inspector",
        func=inspect_dataframe,
        description="Use this to get basic stats, columns, head of the DataFrame."
    ),
    Tool(
        name="plot_generator",
        func=lambda q: generate_plot(*q.split(",")),
        description="Use this to generate a line plot. Pass as: x_column,y_column"
    )
]