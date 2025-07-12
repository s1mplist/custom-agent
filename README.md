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

supervisor_agent = SupervisorAgent(
    model_name="openai:o4-mini",
    agents=[]
).get_supervisor()
```

See [src/notebooks/langgraph-supervisor.ipynb](src/notebooks/langgraph-supervisor.ipynb) for full examples.

## Project Structure

``` text
.gitignore
poetry.lock
pyproject.toml
README.md
src/
    .env
    langgraph_supervisor_with_agents/
        __init__.py
        main.py
        agents/
            __init__.py
            supervisor.py
        schema/
            __init__.py
            state.py
        utils/
            __init__.py
            logger.py
    notebooks/
        dev-notebook.ipynb
        langgraph-introduction.ipynb
        langgraph-supervisor.ipynb
    tests/
```

## Development

- Clone the repo
- Install dependencies with `poetry install`
- Run tests with `pytest`

## License
