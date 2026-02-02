def mySort(values):
    zeroes = 0
    ones = 0
    twos = 0

    low = []
    mid = []
    high = []

    for num in values:
        if num == 0:
            zeroes +=1
        elif num == 1:
            ones += 1
        elif num == 2:
            twos += 1
    
    for i in range(zeroes):
        low.append(0)
    for i in range(ones):
        mid.append(1)
    for i in range(twos):
        high.append(2)

    sortedValues = low + mid + high

    return sortedValues

if __name__ == "__main__":
    my_values = [0, 0, 2, 2, 1, 1, 2, 0]
    print(mySort(my_values))