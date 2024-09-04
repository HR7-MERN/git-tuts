# python functions


def greet(word):
    res = "Hello " + word
    return res


name = input()
greeting = greet(word=name)
print(greeting)
