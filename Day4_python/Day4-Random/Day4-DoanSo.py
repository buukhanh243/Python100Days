import random 

while True:
        soMay = random.randint(1,3)
        count = 0
        Win = False
        while count < 7:
                count += 1
                soNguoi = float(input("Máy đoán từ 1 đến 100 mời bạn đoán: "))
                if soMay == soNguoi:
                    print("Chúc mừng bạn đã đoán đúng, số máy là= ",soMay)
                    Win = True
                    break
                if soMay > soNguoi:
                    print("Bạn đã đoán sai, số máy > số người")
                elif soMay < soNguoi:
                    print("Bạn đoán sai, số máy < số bạn")
        if Win:
            print("Game Over!")
        hoi = input("Tiep khong? ")
        if hoi == "k":
            break
print("Cảm ơn bạn đã chơi game")

