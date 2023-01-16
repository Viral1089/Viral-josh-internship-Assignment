"""Create a function to division by provided argos: [[1, 0], [1, 2], [6, 3], [1, “a”] handle with specific errors"""

def divide_numbers(data):
    result = []
    for item in data:
        try:
            quotient = item[0] / item[1]
            result.append(quotient)
        except ZeroDivisionError as e:
            print(e)
        except TypeError as t:
            print(t)
    return result

data = [[1, 0], [1, 2], [6, 3], [1, "a"]]
print(divide_numbers(data))
