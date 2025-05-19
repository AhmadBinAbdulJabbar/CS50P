def main():
     result = get_fuel_percentage("Fraction: ")
     print(gauge(result))


def get_fuel_percentage(prompt):
    while True:
         try:
              fraction = input(prompt).strip()
              percent = convert(fraction)
         except (ValueError, ZeroDivisionError):
              pass
         else:
              return percent


def convert(fraction):
     x, y = fraction.split("/")
     x, y = int(x), int(y)
     if y == 0:
          raise ZeroDivisionError
     if x > y:
          raise ValueError

     percent = round((x / y) * 100)
     return percent


def gauge(percentage):
     if percentage >= 99:
          return "F"
     elif percentage <= 1:
         return "E"
     else:
          return f"{percentage}%"


if __name__ == "__main__":
    main()
