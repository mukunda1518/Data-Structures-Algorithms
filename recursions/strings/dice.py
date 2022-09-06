def dice(p_str, target, face):
    if target == 0:
        print(p_str)
        return
    for i in range(1, target + 1):
        dice(p_str + str(i), target - i, face)


def dice_list(p_str, target, face):
    if target == 0:
        return [p_str]
    arr = []
    for i in range(1, target + 1):
        arr.extend(dice_list(p_str + str(i), target - i, face))
    return arr


if __name__ == "__main__":
    dice("", 4, 6)
    print(dice_list("", 4, 8))
