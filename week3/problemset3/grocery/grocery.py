def main():
  grocery = {}
  while True:
    try:
      item = input().strip().upper()
      if item in grocery:
        grocery[item] += 1
      else:
        grocery[item] = 1
    except EOFError:
      break

  for key in sorted(grocery):
    print(f"{grocery[key]} {key}")



if __name__ == "__main__":
  main()
