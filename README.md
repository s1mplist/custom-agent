# README.md
# langgraph-supervisor-with-agents

A framework for orchestrating and supervising multiple AI agents using LangGraph and LangChain.

## Features

- Supervisor agent to coordinate multiple sub-agents
- Extensible agent and state schema system
- Integration with LangChain and LangGraph
- Example notebooks for research and math agents

## Installation

Install with [Poetry](https://python-poetry.org/):

```sh
poetry install
```

Or with pip:

```sh
pip install .
```

## Usage

Example: Creating a supervisor agent

```python
from langgraph_supervisor_with_agents.agents import SupervisorAgent
from langgraph_supervisor_with_agents.schema.state import AppStateSchema

supervisor_agent = SupervisorAgent(
    model="openai:o4-mini",
    agents=[],
    state_schema=AppStateSchema
).get_supervisor()
```

See [src/notebooks/langgraph-supervisor.ipynb](src/notebooks/langgraph-supervisor.ipynb) for full examples.

## Project Structure

```
src/
    langgraph_supervisor_with_agents/
        agents/
        schema/
        utils/
    notebooks/
        dev-notebook.ipynb
        langgraph-supervisor.ipynb
tests/
pyproject.toml
```

## Development

- Clone the repo
- Install dependencies with `poetry install`
- Run tests with `pytest`

## License

MIT