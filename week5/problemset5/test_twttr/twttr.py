def main():
    tweet = input("Input: ").strip()
    twt = shorten(tweet)
    print(f"Output: {twt}")


def isvowel(ch):
    if ch.lower() in ("a", "e", "i", "o", "u"):
        return True
    else:
        return False


def shorten(word):
    short = ""
    for w in word:
        if isvowel(w):
            continue
        else:
            short += w

    return short


if __name__ == "__main__":
    main()
