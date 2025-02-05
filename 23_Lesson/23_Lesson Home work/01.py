import os

def ochurmek():
    time = int(input("Nace minutdan: "))
    os.system(f"shutdown/s/t {time}")
    print(f"kompiyuter {time} minutdan son ocer!")

def restart():
    time = int(input("Nace minutdan: "))
    os.system(f"shutdown/r/t {time}")
    print(f"kompiyuter {time} minutdan son restart bolar!")

def buyrugy_yzyna_almak():
    os.system("shutdown/a")
    print("Buyruk yzyna alyndy!")


def main():
    while True:
        choice = input("saylan: ")
        if choice == "1":
            ochurmek()
        elif choice == "2":
            restart()
        elif choice == "3":
            buyrugy_yzyna_almak()
        elif choice == "4":
            print("Programmany ulanu-ynyz ucin sagbolun!")
            break
        else:
            print("Yalnys buyruk!")

main()