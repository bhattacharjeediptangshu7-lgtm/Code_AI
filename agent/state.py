from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field

@dataclass
class AgentState:
    """
    Holds the agent's context and memory throughout the workflow.
    - context: stores key-value pairs for project info, execution results, etc.
    - memory: stores sequential events, logs, or previous actions.
    """
    def __init__(self) -> None:
        self.context: Dict[str, Any] = {}
        self.memory: List[Any] = []

    # --------------------
    # Context Methods
    # --------------------
    def update_context(self, key: str, value: Any) -> None:
        """Update or add a key-value pair in context."""
        self.context[key] = value

    def get_context(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieve a value from context, return default if not present."""
        return self.context.get(key, default)

    def remove_context(self, key: str) -> None:
        """Remove a key from context if it exists."""
        self.context.pop(key, None)

    # --------------------
    # Memory Methods
    # --------------------
    def add_memory(self, item: Any) -> None:
        """Append an item to memory list."""
        self.memory.append(item)

    def get_memory(self) -> List[Any]:
        """Return full memory."""
        return self.memory

    def clear_memory(self) -> None:
        """Clear memory list."""
        self.memory.clear()

    # --------------------
    # Utilities
    # --------------------
    def as_dict(self) -> Dict[str, Any]:
        """Return a dictionary representation of the state."""
        return {
            "context": self.context.copy(),
            "memory": self.memory.copy(),
        }
    
    prompt: str = ""

    plan: dict = field(default_factory=dict)

    generated_code: str = ""

    stage: str = "Idle"