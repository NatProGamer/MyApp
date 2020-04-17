def getmin(*numbers, **params):
    ''' Get min value
    *numbers --> All the numbers
    **params --> All the params
        list --> A list of numbers
            The others numbers would be ignored
        start --> The research start index
            The list must be specified
        end --> The research end index
            The list must be specified'''
    if "list" in params:
        list = params["list"]
        start = 0
        end = len(list)
        if "start" in params:
            start = params["start"]
        if "end" in params:
            end = params["end"] + 1
    else:
        list = []
        for i in range(0, len(numbers)):
            list.append(numbers[i])
        start = 0
        end = len(numbers)
    min = list[start]
    for i in range(start, end):
        if list[i] < min:
            min = list[i]
    return min

def getmax(*numbers, **params):
    ''' Get max value
    *numbers --> All the numbers
    **params --> All the params
        list --> A list of numbers
            The others numbers would be ignored
        start --> The research start index
            The list must be specified
        end --> The research end index
            The list must be specified'''
    if "list" in params:
        list = params["list"]
        start = 0
        end = len(list)
        if "start" in params:
            start = params["start"]
        if "end" in params:
            end = params["end"] + 1
    else:
        list = []
        for i in range(0, len(numbers)):
            list.append(numbers[i])
        start = 0
        end = len(list)
    max = list[start]
    for i in range(start, end):
        if list[i] > max:
            max = list[i]
    return max
