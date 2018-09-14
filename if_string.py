def string_checker(_s1, _s2):
    if isinstance(_s1, str) and isinstance(_s2, str):
        if _s1 == _s2:
            return 1
        elif len(_s1) > len(_s2):
            return 2
        elif _s2 == 'learn':
            return 3
        else:
            # Недостоющиее условие
            return 4
    else:
        return 0


s1 = input('Строчка 1 ')
s2 = input('Строчка 2 ')


output_result = string_checker(s1, s2)

print(output_result)
