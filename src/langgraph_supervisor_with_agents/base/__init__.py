from abc import ABC, abstractmethod


from typing import Dict

class BaseAgent(ABC):
    agent_name: str
    agent_description: str
    
    @abstractmethod
    def run(self):
        """
        Run the agent's main logic.
        This method should be implemented by subclasses.
        """
        pass