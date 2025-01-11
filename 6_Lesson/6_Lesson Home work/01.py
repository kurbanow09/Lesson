def draw_diamond_single_loop(height):
    for i in range(-height + 1, height):
        print(" " * (abs(i)), end="")
        print("*" * (2 * (height - abs(i)) - 1))

draw_diamond_single_loop(5)