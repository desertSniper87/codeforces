if __name__ == '__main__':
    n_students, school_x, school_y = map(int, input().split())
    houses = []

    dict = {
        'RIGHT' : 0,
        'LEFT' : 0,
        'UP' : 0,
        'DOWN' : 0
    }

    for i in range(n_students):
        x, y = map(int, input().split())
        if x > school_x:
            dict['RIGHT'] += 1
        elif x < school_x:
            dict['LEFT'] += 1


        if y > school_y:
            dict['UP'] += 1
        elif y < school_y:
            dict['DOWN'] += 1

    max_direction = max(dict, key=dict.get)
    max_elem = dict[max_direction]


    print(max_elem)
    if max_direction == 'LEFT':
        print(str(school_x - 1) + ' ' + str(school_y))
    if max_direction == 'RIGHT':
        print(str(school_x + 1) + ' ' + str(school_y))
    if max_direction == 'UP':
        print(str(school_x) + ' ' + str(school_y + 1))
    if max_direction == 'DOWN':
        print(str(school_x) + ' ' + str(school_y - 1))


