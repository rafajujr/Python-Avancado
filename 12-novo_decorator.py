from decorator import my_decorator, uppercase_decorator, split_string_decorator

@my_decorator
def minha_funcao():
    print("Minha função")

minha_funcao()

@uppercase_decorator
def text():
    return "Ola, seja bem vindo ao curso de python"

print(text())

@split_string_decorator
@uppercase_decorator
def text():
    return "Ola, seja bem vindo ao curso de python"

print(text())