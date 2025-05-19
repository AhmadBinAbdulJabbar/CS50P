from datetime import date
import inflect
import sys

def main():
    dob = input("Enter Birthday in format YYYY-MM-DD: ")
    print(get_minutes_since(dob))

# 2001-04-21

def get_minutes_since(date_str: str) -> int:
    try:
         birth_day = date.fromisoformat(date_str)
    except:
        sys.exit(1)

    days_diff = (date.today() - birth_day).days
    minutes = days_diff * 24 * 60

    p = inflect.engine()
    minutes_in_words = p.number_to_words(minutes, andword="")
    return minutes_in_words.capitalize() + " minutes"


if __name__ == "__main__":
    main()
