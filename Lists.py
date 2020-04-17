def getindex(value, *values, **params):
    '''Get the index of the first occurence
    value --> The value to search  
    *values --> All the values in whiches to search
    **params --> The params of the research
        list --> The list in which to seach
            If precised, the other values would be ignored
        start --> The start index of the research
            The list must be precised
        end --> The end index of the resarch
            The list must be precised
    Example: valuefound, index = getindex(valuetosearch, value1, value2, value3)'''
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
        for i in range(0, len(values)):
            list.append(values[i])
        start = 0
        end = len(list)
    i = start
    while  i < end:
        if list[i] == value:
            return True, i
        i += 1
    return False, 0
