def get_mean():
    values_inp=input("Enter your values: ")
    values = [float(x) for x in values_inp.split()]
    mean = sum(values) / len(values)
    print("Mean:" , mean)
get_mean()