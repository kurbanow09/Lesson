while True:
    username = input("Please type username: ")
    if 3 <= len(username) <= 15:
        print(f"Hi {username}:)")
        break
    else:
        print("3-15 aralykda bolmaly")