def main():
    tweet = input("Input: ").strip()
    twt = ""
    for t in tweet:
        if isvowel(t):
            continue
        else:
            twt += t
    print(f"Output: {twt}")


def isvowel(ch):
    if ch.lower() in ("a", "e", "i", "o", "u"):
        return True
    else:
        return False

main()
