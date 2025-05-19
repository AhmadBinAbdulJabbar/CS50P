# def greet(input):
#     if "hello" in input:
#         print("hello, there")
#     else:
#         print("I'm not sure what you mean")

def greet(input):
    if "hello" in input:
        return "hello, there"
    else:
        return "I'm not sure what you mean"


greeting = greet("hello, computer")
# greeting = greet("How's the weather?")
print("Hm, " + greeting)
print(greeting + " Ahmad")
