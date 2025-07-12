from abc import ABC, abstractmethod
from langchain_core.runnables import RunnableConfig

from langgraph_supervisor_with_agents.schema import AppStateSchema
from langgraph_supervisor_with_agents.schema.chatbot import Request, GenerativeResult

class BaseAgent(ABC):
    agent_name: str
    agent_description: str
    runnable_config: RunnableConfig
    
    def check_schema(self, state: AppStateSchema) -> bool:
        """
        Check if the provided state matches the expected schema.
        
        Args:
            state (AppStateSchema): The state to check.
        
        Returns:
            bool: True if the state matches the schema, False otherwise.
        """
        return isinstance(state, AppStateSchema)
    
    @abstractmethod
    def run(self, request: Request) -> GenerativeResult:
        """
        Run the agent's main logic.
        This method should be implemented by subclasses.
        """
        pass