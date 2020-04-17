def getmin(*numbers, **params):
    ''' Get min value
    *numbers --> All the numbers
    **params --> All the params
        list --> A list of numbers
            The others numbers would be ignored'''
    if "list" in params:
        list = params["list"]
    else:
        list = []
        for i in range(0, len(numbers)):
            list.append(numbers[i])
    min = list[0]
    for i in range(1, len(list)):
        if list[i] < min:
            min = list[i]
    return min

def getmax(*numbers, **params):
    ''' Get max value
    *numbers --> All the numbers
    **params --> All the params
        list --> A list of numbers
            The others numbers would be ignored'''
    if "list" in params:
        list = params["list"]
    else:
        list = []
        for i in range(0, len(numbers)):
            list.append(numbers[i])
    max = list[0]
    for i in range(1, len(list)):
        if list[i] > max:
            min = list[i]
    return min
