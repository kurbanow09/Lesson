def inverted_triangle(h):
  for i in range(h):
    print(" " * i + "*" * (2*(h-i)-1))

inverted_triangle(5) 