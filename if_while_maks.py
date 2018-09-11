five_school = [{'school_class': '4a', 'scores': [2, 4, 4, 5, 2]},
               {'school_class': '4b', 'scores': [3, 4, 2, 5, 1]},
               {'school_class': '5a', 'scores': [3, 4, 4, 5, 2]},
               {'school_class': '3a', 'scores': [3, 1, 2, 5, 2]},
               {'school_class': '3b', 'scores': [2, 4, 4, 3, 2]},
               {'school_class': '6a', 'scores': [3, 2, 4, 5, 2]},
               {'school_class': '3c', 'scores': [5, 4, 1, 5, 2]},
               {'school_class': '6c', 'scores': [3, 5, 1]},
               ]

school_sum = list()
school_count = list()
for classes in five_school:
    print(f"Класс {classes['school_class']}:"
          f" средний бал {sum(classes['scores'])/len(classes['scores'])}")
    school_sum.append(sum(classes['scores']))
    school_count.append(len(classes['scores']))

print(f"Общий средний бал по школе: {sum(school_sum)/sum(school_count)}")
