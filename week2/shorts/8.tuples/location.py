import sys


def main():
    # latitude = 42.376
    # longitude = -71.115

    # coordinates = (42.376, -71.115)
    # latitude, longtitude = coordinates
    # print(f"Latitude: {coordinates[0]}")
    # print(f"Longitude: {coordinates[1]}")
    # print(f"Latitude: {latitude}")
    # print(f"Longitude: {longtitude}")


    coordinate_tuple = (42.376, -71.115)
    coordinate_list = [42.376, -71.115]
    print(f"{sys.getsizeof(coordinate_tuple)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} bytes")

main()
