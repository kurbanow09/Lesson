def okuwcy_hasapla(students_count):
    passed_count = 0
    total = 0

    for i in range(students_count):
        point = int(input(f'{i+1}. okuwcy bally: '))

        if point >= 50:
            passed_count += 1

        total += point

    gecenler = passed_count
    gecmedikler = students_count - passed_count
    ortaca = total // students_count

    print(f'gecenler: {gecenler}')
    print(f'gecmedikler: {gecmedikler}')
    print(f'ortaca bal: {ortaca}')

students_count = int(input('okuwcylaryn sany: '))


okuwcy_hasapla(students_count)