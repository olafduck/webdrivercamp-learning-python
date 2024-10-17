#!/usr/bin/python3

def divide_list_safe(list_1, list_2, list_len):

    list_3 = []

    for ind in range(list_len):
        try:
            list_3.append(list_1[ind] / list_2[ind])
        except TypeError:
            list_3.append(0)
            print("wrong type") 
        except ZeroDivisionError:
            list_3.append(0)
            print("division by 0")
        except IndexError:
            list_3.append(0)
            print("out of range")
        finally:
            continue

    return list_3

if __name__ == "__main__":
    list_1 = [9, 2, 6]
    list_2 = [3, 2, 2]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
    print(10*"_")
    print()

    list_1 = [9, 2, 6, 10]
    list_2 = ["one", 0, 1, 2, 7]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
