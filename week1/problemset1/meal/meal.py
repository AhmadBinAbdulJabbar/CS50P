def main():
    time = input("What time it is? ").strip().lower()
    time = convert(time)

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")



# def convert(time):
#     hour, min = time.split(":")
#     hour = float(hour)
#     min = float(min) / 60

#     float_time = hour + min
#     return float_time

# challenge code

def convert(time):
    if "a.m." in time or "p.m." in time:
        time, meridiem = time.split(" ")
        hour, min = time.split(":")
        hour = int(hour)
        min = int(min)

        if meridiem == "p.m." and hour != 12:
            hour += 12
        elif meridiem == "a.m." and hour == 12:
            hour = 0

    else:
        hour, min = time.split(":")
        hour = int(hour)
        min = float(min) / 60

    return hour + min

if __name__ == "__main__":
    main()


# challenge code 1st attempt but we need to convert the 12 hour format into 24 hour format

# def main():
#     time = input("What time it is? ").strip().lower()
#     time_and_meridiem = convert(time)

#     time = time_and_meridiem["time"]
#     meridiem = time_and_meridiem["meridiem"]

#     if 7.0 <= time <= 8.0 and meridiem == "a.m.":
#         print("breakfast time")
#     elif (12.0 <= time or time == 1.0) and meridiem == "p.m.":
#         print("lunch time")
#     elif 6.0 <= time <= 7.0 and meridiem == "p.m.":
#         print("dinner time")


# def convert(time):
#     hour, min = time.split(":")
#     min, meridiem = min.split(" ")

#     hour = float(hour)
#     min = float(min) / 60

#     result = {}

#     result["time"] = hour + min
#     result["meridiem"] = meridiem

#     return result


# if __name__ == "__main__":
#     main()
