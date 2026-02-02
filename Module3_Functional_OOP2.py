my_list = [1, 2, 3, 4, 5, 6, 7]

num = int(input("Please enter a number to search for: "))

guess = "Not found"

for i in range(len(my_list)):
    if num == my_list[i]:
        guess = i
        break

if guess == "Not found":
    print("Could not find your number in the list.")
else:
    print(f"Number {num} is found at index {guess}")