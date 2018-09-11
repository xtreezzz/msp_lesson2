_age = input("Введите возраст: ")
int_age = int(_age)


def chose_destiony(age):
    if age <= 6:
        dest = 'детский сад'
    elif age > 6 and age <= 18:
        dest = 'школа'
    elif age > 18 and age <= 22:
        dest = 'вуз'
    else:
        dest = 'работа'
    return dest


int_age_chose = chose_destiony(int_age)
print(int_age_chose)
