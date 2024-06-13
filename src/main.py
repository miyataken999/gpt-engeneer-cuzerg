from src.services.user_service import UserService

def main():
    user_service = UserService()
    user_service.greet("John")

if __name__ == "__main__":
    main()