import time
print("1-ADDİTİON")
print("2-EXTRACTİON")
print("3-MULTIPLICATION")
print("4-DIVISION")
print("__________")
while True:
    x = input("Select Transaction...")
    y = input("Enter First Number...")
    z = input("Enter Second Number...")

    if x =="1":
        print(int(y) + int(z))
        time.sleep(2.0)
        quit()
    if x =="2":
        print(int(y) - int(z))
        time.sleep(2.0)
        quit()
    if x =="3":
        print(int(y) * int(z))
        time.sleep(2.0)
        quit()
    if x =="4":
        print(int(y) / int(z))
        time.sleep(2.0)
        quit()