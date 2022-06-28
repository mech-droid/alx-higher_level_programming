#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
    result = []
    for i in range(list_lenght):
        try:
            result.append(my_list1[i] / my_list2[i])
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by zero")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass
    return result