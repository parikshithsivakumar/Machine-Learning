from re import I
input_string = input("Enter a string: ")
count = {}

for i in input_string:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

# Find the character with the highest count
highest_char = max(count, key=count.get)
highest_count = count[highest_char]

print(f" highest occur character is '{highest_char}' with count of {highest_count}.")