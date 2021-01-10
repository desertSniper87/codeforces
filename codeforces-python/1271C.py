import math
from collections import Counter


class House:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def get_distance(self, point):
        return abs(point.x-self.x) + abs(point.y-self.y)

    def get_relative_distance(self, point):
        if self.x > point.x:
            x_position = 1
        elif self.x < point.x:
            x_position =  -1
        else:
            x_position = 0

        if self.y > point.y:
            y_position = 1
        elif self.y < point.y:
            y_position =  -1
        else:
            y_position = 0

        return (x_position, y_position)


if __name__ == '__main__':
    n_students, school_x, school_y = map(int, input().split())
    school = House(school_x, school_y)
    houses = []
    for i in range(n_students):
        x, y = map(int, input().split())
        houses.append(House(x, y))

    x_relative_list, y_relative_list = zip(*[house.get_relative_distance(school) for house in houses])

    relative_list = [house.get_relative_distance(school) for house in houses]

    x_axis_occurance = Counter(elem[0] for elem in relative_list)
    y_axis_occurance = Counter(elem[1] for elem in relative_list)

    # print("LINE:49 -- (x_axis_occurance, y_axis_occurance) = " + str((x_axis_occurance, y_axis_occurance)))

    # most_common = (x_axis_occurance + y_axis_occurance).most_common(2)
    #
    # if most_common[0][0] == 0:
    #     most_common = most_common[1][0]
    # else:
    #     most_common = most_common[0][0]

    x_axis_mst_cmn = x_axis_occurance.most_common(1)[0]
    y_axis_mst_cmn = y_axis_occurance.most_common(1)[0]

    most_common = max(x_axis_mst_cmn[1], y_axis_mst_cmn[1])


    print(most_common)
    if x_axis_mst_cmn[1] > y_axis_mst_cmn[1]:
        # most_common = 'LEFT' if x_axis_mst_cmn[0] == -1 else 'RIGHT'
        print(str(school_x + x_axis_mst_cmn[0]) + ' ' + str(school_y))
    else:
        print(str(school_x) + ' ' + str(school_y + y_axis_mst_cmn[0]))
        # most_common = 'DOWN' if x_axis_mst_cmn[0] == -1 else 'UP'

    # print("LINE:66 -- most_common = " + str(most_common))




    # print("LINE:43 -- (x_relative_list, y_relative_list) = " + str((x_relative_list, y_relative_list)))

    # def most_common(lst):
    #     return max(set(lst), key=lst.count)
    #
    # for h in houses:
    #     print("LINE:47 -- (h.x, h.y)) + str(h.get_relative_distance(school) = " + str((h.x, h.y)) + str(h.get_relative_distance(school)))
    #
    # most_common_x = most_common(x_relative_list)
    # most_common_y = most_common(y_relative_list)
    #
    # print("LINE:52 -- (most_common_x, most_common_y) = " + str((most_common_x, most_common_y)))
    #
    # # left = []
    #
    # def applicable_house(house, most_common):
    #     hr_x, hr_y = house.get_relative_distance(school)
    #     if most_common == 'LEFT' and hr_x == -1:
    #         return True
    #     if most_common == 'RIGHT' and hr_x == 1:
    #         return True
    #     if most_common == 'UP' and hr_y == 1:
    #         return True
    #     if most_common == 'DOWN' and hr_y == -1:
    #         return True
    #     return False

    # print("LINE:53 -- house.x, house.y = " + str(house.x) +' '+ str(house.y))
        # print("LINE:54 -- cmn_x, cmn_y = " + str(cmn_x) +' '+  str(cmn_y))
        # hr_x, hr_y = house.get_relative_distance(school)
        # print("LINE:56 -- hr_x, hr_y = " + str((hr_x, hr_y)))
        # if hr_x != cmn_x and hr_x != 0:
        #     print('hr_x != cmn_x and hr_x != 0')
        #     return False
        # if hr_y != cmn_y and hr_y != 0:
        #     print('hr_x != cmn_y and hr_y != 0')
        #     return False
        #
        # return True
    #
    #
    # houses = list(filter(lambda house: applicable_house(house, most_common), houses))
    # for house in houses:
    #     print(house)

