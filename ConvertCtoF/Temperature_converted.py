import numbers

def cToFConverter():
    while True:
        # cTemp = input("Please enter C degree: ")
        # if cTemp:
        #     cTemp = float(cTemp)
        #     ftemp = round(9*cTemp/5+32,1)
        #     print(f"{cTemp}C is converted to {ftemp}F")
        #     break
        # else:
        #     print(cTemp)
        #     print("cTemp input is empty")
        #     continue
        try:
            cTemp = float(input("Please enter C degree: "))
            cTemp = float(cTemp)
            ftemp = round(9 * cTemp / 5 + 32, 1)
            print(f"{cTemp}C is converted to {ftemp}F")
            break
        except:
            print("Ban nhap sai roi moi nhap lai")
            continue

def main():
    cToFConverter()

if __name__ == '__main__':
    main()