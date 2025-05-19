import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(?P<start_time>[1-9]([0-2]?(:[0-5][0-9])?)) (?P<start_meridiem>AM|PM) to (?P<end_time>[1-9]([0-2]?(:[0-5][0-9])?)) (?P<end_meridiem>AM|PM)$"

    match = re.search(pattern, s)

    if match:
        start_meridiem = match.group("start_meridiem")
        end_meridiem = match.group("end_meridiem")
        start_time = match.group("start_time")
        end_time = match.group("end_time")
        # print(start_meridiem, end_meridiem, start_time, end_time)
        start = time_converter(start_meridiem, start_time)
        end = time_converter(end_meridiem, end_time)
        # print(f"{start} to {end}")
        return f"{start} to {end}"
    else:
        raise ValueError("Invalid")




def time_converter(meridiem, time):
    if ":" in time:
        hours, mins = time.split(":")
        hours = f"{int(hours):02}"
    else:
        hours = f"{int(time):02}"
        mins = "00"

    if meridiem == "AM":
        if hours == "12":
            hours = "00"
    else:
        if hours != "12":
            hours = str(int(hours) + 12)


    return f"{hours}:{mins}"


if __name__ == "__main__":
    main()
