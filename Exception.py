
a = 5
b = 5

try:
    n = int(input('enter value '))
    print(a/b)
except ZeroDivisionError as e:
    print('Exception ', e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print('bye')

