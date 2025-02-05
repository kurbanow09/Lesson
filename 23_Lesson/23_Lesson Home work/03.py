import os
def folders():
    for i in range(1, 11):
        os.mkdir(str(i))

folders()