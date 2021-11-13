def fill_the_box(height, length, width, *args):

    cube_counts = []
    flag = True
    for _ in args:
        if flag:
            cube_counts.append(_)
        if _ == "Finish":
            flag = False

    cube_counts = list(cube_counts)
    volume = height * length * width
    for i in range(len(cube_counts)-1):
        if cube_counts[i] != "Finish":
            if volume >= int(cube_counts[i]):
                volume -= int(cube_counts[i])
                cube_counts[i] = 0
            else:
                cube_counts[i] = int(cube_counts[i]) - volume
                volume = 0

    cube_counts.pop()
    if volume > 0:
        return f"There is free space in the box. You could put {volume} more cubes."
    return f"No more free space! You have {sum(cube_counts)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))

