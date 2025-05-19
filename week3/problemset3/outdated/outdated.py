def main():
  months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
  ]

  while True:
    try:
      date = input("Date: ").strip()

      if "/" in date:
        month, day, year = date.split("/")

      elif "," in date:
        month_day, year = date.split(",")
        month, day = month_day.split(" ")

        if month in months:
          month = months.index(month) + 1
        else:
          raise ValueError

      else:
        raise ValueError

      month, day, year = int(month), int(day), int(year)
      if day < 1 or day > 31 or year < 0 or month < 0 or month > 12:
        raise ValueError

      print(f"{year}-{month:02}-{day:02}")
      break

    except ValueError:
      pass


if __name__ == "__main__":
  main()
