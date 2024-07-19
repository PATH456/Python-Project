import os
size = os.stat("hai").st_size
if size == 0:
    print("File is empty")
else:
    print("File is not empty")









