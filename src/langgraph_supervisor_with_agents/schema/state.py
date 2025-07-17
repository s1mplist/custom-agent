try:
    # Try importing Pydantic v2
    from pydantic import BaseModel, Field
    from pydantic.version import VERSION as PYDANTIC_VERSION
    if not PYDANTIC_VERSION.startswith("2."):
        raise ImportError("Not Pydantic v2")
except ImportError:
    # Fallback to Pydantic v1
    from pydantic import BaseModel, Field

from langchain_core.messages import BaseMessage
from typing import List, Optional, Dict, Any

from langgraph_supervisor_with_agents.schema.chatbot import Request, GenerativeResult

class AppStateSchema(BaseModel):
    request: Request = Field(description="The request made to the agent.")
    input: str = Field(description="The input provided to the agent.")
    messages: List[BaseMessage] = Field(description="A history of interactions with the agent.")
    topics: Optional[List[str]] = Field(description="The topics relevant to the agent's task.")
    is_last_step: bool = Field(description="Flag indicating if this is the last step in the process.")
    remaining_steps: List[str] = Field(description="A list of calls that are pending execution.")
    executed_steps: List[str] = Field( description="A list of calls that have been executed.")
    global_context: Optional[Dict[str, Any]] = Field(description="Global context information for the agent.")
    result: Optional[GenerativeResult] = Field(description="The result of the agent's processing.")
    errors: Optional[str] = Field(description="Any errors encountered during processing.")