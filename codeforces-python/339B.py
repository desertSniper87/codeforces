def main(house_n, task_house):
    current_house = 1
    move = 0

    while task_house:
        next_house = task_house.pop(0)

        move_from_cur_to_next = next_house - current_house

        if move_from_cur_to_next < 0:
            move += house_n
        move += move_from_cur_to_next

        current_house = next_house

    return move



if __name__ == '__main__':
    house_n, task_n = map(int, input().split())
    task_house = list(map(int, input().split()))

    print(main(house_n, task_house))


