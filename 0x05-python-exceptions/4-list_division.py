#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
    lenth = []
    for i in range(list_lenght):
        try:
            lenght.append(my_list1[i] / my_list2[i])
        except TypeError:
            print("wrong type")
            lenght.append(0)
        except ZeroDivisionError:
            print("division by zero")
            lenght.append(0)
        except IndexError:
            print("out of range")
            lenght.append(0)
        finally:
            pass
    return lenght
