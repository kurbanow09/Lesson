import os
import random

folders = [f"folder_{i}" for i in range(1, 11)]

folders_to_delete = random.sample(folders, 8)

for folder in folders_to_delete:
    if os.path.exists(folder):
        os.rmdir(folder) 
        print(f"{folder} pozuldy.")
    else:
        print(f"{folder} ýok, şonuň üçin pozulmady.")