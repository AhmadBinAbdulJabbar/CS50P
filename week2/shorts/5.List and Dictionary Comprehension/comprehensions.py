from helpers import get_words, save_counts

def main():
    # counts = {}
    words = get_words("address.txt")

    # list comprehension
    lowercase_words = [word.lower() for word in words]
    # lowercase_words = [word.lower() for word in words if len(word) > 4]

    # for word in lowercase_words:
    #     if word in counts:
    #         counts[word] += 1
    #     else:
    #         counts[word] = 1

    # dictionary comprehension
    print("the word was", lowercase_words.count("the"))

    counts = {word: lowercase_words.count(word) for word in lowercase_words}

    save_counts(counts)

main()
