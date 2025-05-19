def main():
    userInput = input()
    print(convert(userInput))


def convert(text : str):
    text = text.replace(':)', '🙂')
    text = text.replace(':(', "🙁")
    return text
    # return text.replace(":)", "🙂").replace(":(", "🙁")


main()
