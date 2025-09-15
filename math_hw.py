def get_mean():
    print("Let's find the Mean")
    values_inp = input("Enter your values: ")
    values = [float(x) for x in values_inp.split()]
    mean = sum(values) / len(values)
    print("Mean:" , get_mean())
    return mean

def get_median():
    print("Let's find the Median")
    values_inp = input("Enter your values: ")
    values = [float(x) for x in values_inp.split()]
    values.sort()
    n = len(values)
    if n % 2 == 0:
        median = (values[n//2 - 1] + values[n//2]) / 2
    else: median = values[n//2]
    print("Median: ", median)
    return median

def get_mode():
    print("Let's find the Mode")
    values_inp = input("What are your values: ")
    values = [float(x) for x in values_inp.split()]
    frequency = {}
    for value in values:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1
    max_count = 0
    mode = None
    for value, count in frequency.items():
        if count > max_count:
            max_count = count
            mode = value
    print("Mode:", mode)
    return mode


choice = input("What do you need?\n" "Mean\n" "Median\n" "Mode\n" ":")
if choice == "mean":
    get_mean()
elif choice == "median":
    get_median()
elif choice == "mode":
    get_mode()