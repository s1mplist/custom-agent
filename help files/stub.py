"""This is an automatically generated file. Do not modify it.

This file was generated using `langgraph-gen` version 0.0.3.
To regenerate this file, run `langgraph-gen` with the source `yaml` file as an argument.

Usage:

1. Add the generated file to your project.
2. Create a new agent using the stub.

Below is a sample implementation of the generated stub:

```python
from typing_extensions import TypedDict

from stub import CustomAgent

class SomeState(TypedDict):
    # define your attributes here
    foo: str

# Define stand-alone functions
def SupervisorDomain(state: SomeState) -> dict:
    print("In node: SupervisorDomain")
    return {
        # Add your state update logic here
    }


def SupervisorFunctions(state: SomeState) -> dict:
    print("In node: SupervisorFunctions")
    return {
        # Add your state update logic here
    }


def Incidentes(state: SomeState) -> dict:
    print("In node: Incidentes")
    return {
        # Add your state update logic here
    }


def Fornecedores(state: SomeState) -> dict:
    print("In node: Fornecedores")
    return {
        # Add your state update logic here
    }


def Contingencias(state: SomeState) -> dict:
    print("In node: Contingencias")
    return {
        # Add your state update logic here
    }


def RAG(state: SomeState) -> dict:
    print("In node: RAG")
    return {
        # Add your state update logic here
    }


def Dataframe(state: SomeState) -> dict:
    print("In node: Dataframe")
    return {
        # Add your state update logic here
    }


def conditional_edge_1(state: SomeState) -> str:
    print("In condition: conditional_edge_1")
    raise NotImplementedError("Implement me.")


def conditional_edge_3(state: SomeState) -> str:
    print("In condition: conditional_edge_3")
    raise NotImplementedError("Implement me.")


def conditional_edge_3(state: SomeState) -> str:
    print("In condition: conditional_edge_3")
    raise NotImplementedError("Implement me.")


agent = CustomAgent(
    state_schema=SomeState,
    impl=[
        ("SupervisorDomain", SupervisorDomain),
        ("SupervisorFunctions", SupervisorFunctions),
        ("Incidentes", Incidentes),
        ("Fornecedores", Fornecedores),
        ("Contingencias", Contingencias),
        ("RAG", RAG),
        ("Dataframe", Dataframe),
        ("conditional_edge_1", conditional_edge_1),
        ("conditional_edge_3", conditional_edge_3),
        ("conditional_edge_3", conditional_edge_3),
    ]
)

compiled_agent = agent.compile()

print(compiled_agent.invoke({"foo": "bar"}))
"""

from typing import Callable, Any, Optional, Type

from langgraph.constants import START, END
from langgraph.graph import StateGraph


def CustomAgent(
    *,
    state_schema: Optional[Type[Any]] = None,
    config_schema: Optional[Type[Any]] = None,
    input: Optional[Type[Any]] = None,
    output: Optional[Type[Any]] = None,
    impl: list[tuple[str, Callable]],
) -> StateGraph:
    """Create the state graph for CustomAgent."""
    # Declare the state graph
    builder = StateGraph(
        state_schema, config_schema=config_schema, input=input, output=output
    )

    nodes_by_name = {name: imp for name, imp in impl}

    all_names = set(nodes_by_name)

    expected_implementations = {
        "SupervisorDomain",
        "SupervisorFunctions",
        "Incidentes",
        "Fornecedores",
        "Contingencias",
        "RAG",
        "Dataframe",
        "conditional_edge_1",
        "conditional_edge_3",
        "conditional_edge_3",
    }

    missing_nodes = expected_implementations - all_names
    if missing_nodes:
        raise ValueError(f"Missing implementations for: {missing_nodes}")

    extra_nodes = all_names - expected_implementations

    if extra_nodes:
        raise ValueError(
            f"Extra implementations for: {extra_nodes}. Please regenerate the stub."
        )

    # Add nodes
    builder.add_node("SupervisorDomain", nodes_by_name["SupervisorDomain"])
    builder.add_node("SupervisorFunctions", nodes_by_name["SupervisorFunctions"])
    builder.add_node("Incidentes", nodes_by_name["Incidentes"])
    builder.add_node("Fornecedores", nodes_by_name["Fornecedores"])
    builder.add_node("Contingencias", nodes_by_name["Contingencias"])
    builder.add_node("RAG", nodes_by_name["RAG"])
    builder.add_node("Dataframe", nodes_by_name["Dataframe"])

    # Add edges
    builder.add_edge("Incidentes", "SupervisorDomain")
    builder.add_edge("Fornecedores", "SupervisorDomain")
    builder.add_edge("Contingencias", "SupervisorDomain")
    builder.add_edge("RAG", "SupervisorFunctions")
    builder.add_edge("Dataframe", "SupervisorFunctions")
    builder.add_conditional_edges(
        START,
        nodes_by_name["conditional_edge_1"],
        [
            "SupervisorDomain",
            "SupervisorFunctions",
        ],
    )
    builder.add_conditional_edges(
        "SupervisorFunctions",
        nodes_by_name["conditional_edge_3"],
        [
            "SupervisorDomain",
            "RAG",
            "Dataframe",
        ],
    )
    builder.add_conditional_edges(
        "SupervisorDomain",
        nodes_by_name["conditional_edge_3"],
        [
            "SupervisorFunctions",
            "Incidentes",
            "Fornecedores",
            "Contingencias",
            END,
        ],
    )
    return builder
