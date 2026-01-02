"""
Utility functions for the todo application.
"""


class IdGenerator:
    """
    Simple ID generator that provides unique sequential IDs.
    """
    def __init__(self):
        self._next_id = 1

    def get_next_id(self) -> int:
        """Get the next unique ID."""
        current_id = self._next_id
        self._next_id += 1
        return current_id

    def reset(self):
        """Reset the ID generator to start from 1 again."""
        self._next_id = 1


# Global ID generator instance
id_generator = IdGenerator()


def get_next_id() -> int:
    """
    Get the next unique ID.
    """
    return id_generator.get_next_id()