def right_aligned_triangle(height):
    for i in range(height):  
        spaces = " " * (height - 1 - i)  
        asterisks = "*" * (i + 1)     
        print(spaces + asterisks)     
right_aligned_triangle(5) 