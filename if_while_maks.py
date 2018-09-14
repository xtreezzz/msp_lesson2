print('********IMPORTED FROM https://github.com/hronikum/lesson2/blob/master/homework/task_3.py**********')
#:1: E402 module level import not at top of file --знаю но так нужно
import task3

print('********CASE1**********')
school_sum = list()
school_count = list()
for classes in task3.school_scores:
    print(f"Класс {classes['school_class']}:"
          f" средний бал {sum(classes['scores'])/len(classes['scores'])}")
    school_sum.append(sum(classes['scores']))
    school_count.append(len(classes['scores']))

print(f"Общий средний бал по школе: {sum(school_sum)/sum(school_count)}")

print('********CASE2**********')

school_sum = list()
school_count = list()
for classes in task3.school_scores:
    school_count.append(len(classes['scores']))
    print(f"Класс {classes['school_class']}:"
          f" средний бал {sum(classes['scores'])/len(classes['scores'])}")
    for marks in classes['scores']:
        school_sum.append(marks)

print(f"Общий средний бал по школе: {sum(school_sum)/sum(school_count)}")
