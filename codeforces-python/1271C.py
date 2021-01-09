import math


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

    def most_common(lst):
        return max(set(lst), key=lst.count)

    for h in houses:
        print(h.get_relative_distance(school))

    most_common_x = most_common(x_relative_list)
    most_common_y = most_common(y_relative_list)

    def applicable_house(house, school, cmn_x, cmn_y):
        print("LINE:53 -- house.x, house.y = " + str(house.x) +' '+ str(house.y))
        print("LINE:54 -- cmn_x, cmn_y = " + str(cmn_x) +' '+  str(cmn_y))
        hr_x, hr_y = house.get_relative_distance(school)
        print("LINE:56 -- hr_x, hr_y = " + str((hr_x, hr_y)))
        if hr_x != cmn_x and hr_x != 0:
            print('hr_x != cmn_x and hr_x != 0')
            return False
        if hr_y != cmn_y and hr_y != 0:
            print('hr_x != cmn_y and hr_y != 0')
            return False

        return True


    houses = list(filter(lambda house: applicable_house(house, school, most_common_x, most_common_y), houses))
    for house in houses:
        print(house)

