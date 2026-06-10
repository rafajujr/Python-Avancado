def my_decorator(function):
    def wrapper():
        print("Antes de executar a função")
        function()
        print("Depois de executar a função")
    return wrapper

def uppercase_decorator(function):
    def wrapper():
        result = function()
        return result.upper()
    return wrapper

def split_string_decorator(function):
    def wrapper():
        result = function()
        return result.split()
    return wrapper