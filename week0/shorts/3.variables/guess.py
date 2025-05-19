# def get_guess():
#     guess = int(input("Enter a guess: "))
#     return guess

# def main():
#     guess = get_guess()
#     if guess == 50:
#         print("Correct!")
#     else:
#         print("Incorrect!")

# other way could be

def get_guess():
    guess = input("Enter a guess: ")
    return guess

def main():
    guess = get_guess()
    if guess == "fifty":
        print("Correct!")
    else:
        print("Incorrect!")

main()
