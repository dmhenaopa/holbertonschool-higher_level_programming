#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    division = 0
    new_list = []

    for index in range(0, list_length):
        try:
            division = my_list_1[index] / my_list_2[index]

        except IndexError as err:
            print("{}".format("out of range"))
            division = 0
            continue

        except TypeError as err:
            print("{}".format("wrong type"))
            division = 0
            continue

        except ZeroDivisionError as err:
            print("{}".format("division by 0"))
            division = 0
            continue

        finally:
            new_list.append(division)

    return new_list
