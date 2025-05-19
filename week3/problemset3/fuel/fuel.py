def main():
     result = get_fuel_percentage("Fraction: ")
     if result >= 99:
          print("F")
     elif result <= 1:
          print("E")
     else:
          print(f"{result}%")



def get_fuel_percentage(prompt):
    while True:
         try:
              fraction = input(prompt).strip()
              x, y = fraction.split("/")
              x, y = int(x), int(y)
              if x > y:
                   raise ValueError
              if y == 0:
                   raise ZeroDivisionError

              percent = round((x / y) * 100)
         except (ValueError, ZeroDivisionError):
              pass
         else:
              return percent


main()
