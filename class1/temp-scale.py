#!/usr/bin/env python3
def convert_temp(scale=None, source_temp=None):
    if scale == "F":
        return 'C', (source_temp - 32.0) * (5.0/9.0)
    elif scale == "C":
        return 'F', (source_temp * (9.0/5.0)) + 32.0
    else:
        print("Needs to be (F) or (C)!")

scale = input("Select (F) or (C): " )
source_temp = int(input("What is the temperature: " ))
newScale, newTemp = convert_temp(scale, source_temp)
print(source_temp, "degrees", scale, "is", newTemp, "degrees", newScale)