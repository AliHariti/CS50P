"""
Create and write in a file
name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
 """

# Read an existing file, method1
"""
with open("names.txt","r") as file:
     lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())
 """

# Read an existing file, method2
"""
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
 """

# Sorting file: method 1
# read is the default parameter of open()
names = []

with open("names.txt") as file:
     for line in file:
         names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")


# Sorting file: method 2
"""
with open("names.txt", "r") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())
 """
 