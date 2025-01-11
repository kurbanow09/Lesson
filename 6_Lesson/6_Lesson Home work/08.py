def inverted_right_aligned_triangle(height):
    for i in range(height):
        print(" " * i + "*" * (height - i))

inverted_right_aligned_triangle(5)