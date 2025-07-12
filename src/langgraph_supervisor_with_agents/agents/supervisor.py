# langgraph_supervisor_with_agents/agents/supervisor.py
# Self imports
from langgraph_supervisor_with_agents.utils import setup_logger
from langgraph_supervisor_with_agents.schema import AppStateSchema

# Langgraph imports
from langgraph_supervisor import create_supervisor
from langgraph.pregel import Pregel

# Langchain imports
from langchain.chat_models import init_chat_model

# Typing imports
from typing import Dict, Optional, Any

class SupervisorAgent:
    """
    SupervisorAgent is responsible for managing and coordinating multiple agents.
    It can handle tasks such as delegating work, aggregating results, and ensuring
    that the overall process runs smoothly.
    """
    def __init__(self,
                 model_name: str,
                 agents: Optional[list[Pregel]] = None,
                 model_kwargs: Optional[Dict[str, Any]] = None
                 ):
        
        """
        Initialize the SupervisorAgent with a language model and a list of agents.
        Args:
            model_name (str): The name of the language model to be used.
            agents (list[Pregel]): A list of agents that this supervisor will manage.
            kwargs (Optional[Dict[str, Any]]): Additional keyword arguments for configuration.
        """

        self.model_name = model_name
        self.agents = agents if agents is not None else []

        self.model_kwargs = model_kwargs or {}
        
        self.model = self._get_model()
    
    def _get_model(self):
        """
        Initialize the language model based on the provided model name and kwargs.
        
        Returns:
            LanguageModelLike: An instance of the language model.
        """
        model = init_chat_model(
            model=self.model_name,
            **self.model_kwargs)
        if isinstance(model, str):
            raise ValueError("model must be a LanguageModelLike instance, not a string. Please provide a valid model object.")
        return model
    
    
    def get_supervisor(self):
        """
        Create a supervisor agent that manages multiple agents.
        
        Returns:
            Runnable: A runnable supervisor agent.
        """
        return create_supervisor(
            model=self.model,
            agents=self.agents,
            state_schema=AppStateSchema
        )   
    