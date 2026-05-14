"""A simple greeter module that provides a function to greet a user by name."""
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    username = input("Enter your name: ")
    print(greet(username))
