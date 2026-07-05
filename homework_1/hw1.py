def print_string_reverse(s):
    if s.strip() == "":
        print('Wrong String')
        return
    else:
        print(s[::-1])


print_string_reverse('Shalom')
print_string_reverse('')
print_string_reverse('        ')



def is_isr_phone_number(phone):
    if phone.strip() == "":
        return None
    if phone[0] == "0" and len(phone) == 10:
        return True
    return False


print(is_isr_phone_number("0547824067"))
print(is_isr_phone_number("1221312337"))
print(is_isr_phone_number(""))



def print_substring_reverse(s, start, finish):
    if s.strip() == "":
        print("Wrong args")
        return

    if start < 0 or finish < 0 or start > finish or finish >= len(s):
        print("Wrong args")
        return

    before = s[:start]
    substring = s[start:finish + 1]
    after = s[finish + 1:]

    reversed_substring = substring[::-1]

    result = before + reversed_substring + after
    print(result)


print_substring_reverse("Shalom", 1, 3)
print_substring_reverse("Shalom", 3, 1)
print_substring_reverse("   ", 0, 1)



def get_words_reverse(s):
    words = s.split(" ")
    reversed_words = words[::-1]
    return " ".join(reversed_words)


print(get_words_reverse("Shalom my nice world"))



def get_words_reverse_letters_and_lines(s):
    words = s.split(" ")
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return "\n".join(reversed_words)


print(get_words_reverse_letters_and_lines("Shalom my nice world"))