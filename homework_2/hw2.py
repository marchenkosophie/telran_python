def print_list_reverse(lst):
    if not isinstance(lst, list) or not lst:
        print("Wrong list")
        return
    print(lst[::-1])


print_list_reverse([1, 2, 3, 4, 5, 6])



def is_valid_point(point):
    if point is None or point == ():
        return None
    if not isinstance(point, tuple):
        return False
    if len(point) != 2:
        return False
    if not isinstance(point[0], (int, float)) or not isinstance(point[1], (int, float)):
        return False
    return True



print(is_valid_point((3, 5)))
print(is_valid_point((3, "5")))
print(is_valid_point([3, 5]))
print(is_valid_point((1, 2, 3)))
print(is_valid_point(()))
print(is_valid_point(None))



def print_sublist_reverse(lst, start, finish):
    if lst is None or lst == []:
        print("Wrong args")
        return
    if not isinstance(lst, list) or not isinstance(start, int) or not isinstance(finish, int):
        print("Wrong args")
        return
    if start < 0 or finish > len(lst) or start > finish:
        print("Wrong args")
        return

    before = lst[:start]
    reversed_sub = lst[start:finish + 1][::-1]
    after = lst[finish + 1:]
    result = before + reversed_sub + after
    print(result)


print_sublist_reverse([10, 20, 30, 40, 50, 60],1, 3)


print_sublist_reverse([1, 2, 3], "0", 2)



def get_students_by_grade(students):
    if students is None or students == {} or not isinstance(students, dict):
        return {}
    grades_dict = {}

    for name, grade in students.items():
        if grade not in grades_dict:
            grades_dict[grade] = [name]
        else:
            grades_dict[grade].append(name)

    return grades_dict


print(get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie":85}))