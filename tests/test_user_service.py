from src.services.user_service import UserService
import pytest

def test_greet():
    """Tests the greet method."""
    user_service = UserService()
    user_service.greet("john")