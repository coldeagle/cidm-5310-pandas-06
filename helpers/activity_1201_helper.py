# Checks if the passed string is a float
def is_float(val: str):
    returnVal = False
    val = '0'+val if val.startswith('.') else val
    splitStr = val.strip().replace(' ','').replace('-', '', 1).replace(',', '').split('.')
    if len(splitStr) == 2:
        returnVal = True
        for s in splitStr:
            if not s.isnumeric():
                returnVal = False
            if not returnVal:
                break

    return returnVal


# Checks if the passed string is an int
def is_int(val: str):
    returnVal = False
    splitStr = val.strip().replace(' ','').replace('-', '', 1).replace(',', '').split('.')

    if len(splitStr) == 1:
        returnVal = splitStr[0].isnumeric()

    return returnVal


def is_date(val: str):
    splitStr = val.strip().replace(' ','').split('-')
    returnVal = False
    if len(splitStr) != 3:
        splitStr = val.strip().replace(' ', '').split('/')
    if len(splitStr) == 3:
        if ((len(splitStr[0]) == 4 and len(splitStr[2]) <= 2) or (len(splitStr[2]) == 4 and len(splitStr[0]) <= 2)) and len(splitStr[1]) <= 2:
            for s in splitStr:
                returnVal = s.isnumeric()
                if not returnVal:
                    break

    return returnVal


def is_time(val: str):
    splitStr = val.strip().replace(' ', '').split(':')
    returnVal = len(splitStr) == 3 or len(splitStr) == 2
    if (returnVal):
        returnVal = len(splitStr[0]) == 2 and splitStr[0].isnumeric() and len(splitStr[1]) == 2 and splitStr[1].isnumeric()

    return returnVal


def is_datetime(val: str):
    returnVal = False
    splitStr = val.strip().split(' ')
    if len(splitStr) == 1:
        splitStr = val.strip().split('T')
    if (len(splitStr) == 2):
        returnVal = is_date(splitStr[0]) and is_time(splitStr[1])

    return returnVal


# Gets the type
def get_type(val: str):
    print(f'get_type, val:{val}')
    type = 'str'
    type = 'int' if is_int(val) else type
    type = 'float' if is_float(val) else type
    type = 'date' if is_date(val) else type
    type = 'time' if is_time(val) else type
    type = 'date_time' if is_datetime(val) else type
    print(f'type:{type}')
    return type
