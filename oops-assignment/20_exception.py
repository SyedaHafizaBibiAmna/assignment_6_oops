class InvalidAgeError(Exception):
    """Custom exception for invalid age input."""
    def __init__(self, message="Age must be a positive integer."):
        self.message = message
        super().__init__(self.message)


# funtion to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("You must be at least 18 years old.")
    else:
        print(f"A ge {age} is valid")



# handling the exception using try-except block
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print(f"Error: {e}")
except ValueError:
    print("Please enter a valid integer for age.")    
