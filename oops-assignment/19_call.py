class Multiplier:
    def __init__ (self, factor):
        self.factor = factor

    def __call__(self, number):
        # this method allows the object to be called like a function
        return number * self.factor
    

    # create an instance of Multiplier with a factor of 5
multiplier = Multiplier(5)

# test the __call__ method
print(callable(multiplier))  # Check if multiplier is callable


#calling the pobject like a function to multiply an input by the factor
result = multiplier(10)  # This will call the __call__ method           
print(result)  # Output: 50  