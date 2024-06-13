from src.models.user import User
from src.utils.string_utils import capitalize

class UserService:
    """Provides user-related services."""
    def greet(self, name: str) -> None:
        """Greets a user."""
        user = User(name)
        print(f"Hello, {capitalize(user.name)}!")