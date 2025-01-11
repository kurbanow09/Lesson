def reversed_triangle_slicing(height):
    rows = []
    for i in range(height):
        rows.append("*" * (i + 1))
    for row in rows[::-1]:  
        print(row)

reversed_triangle_slicing(5)