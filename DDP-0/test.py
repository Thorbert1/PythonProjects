bin1 = input("Binary number 1: ")
bin2 = input("Binary number 2: ")

if len(bin1) == len(bin2):
    print(sum([True if bin1[i] != bin2[i] else False for i in range(len(bin1))]))
