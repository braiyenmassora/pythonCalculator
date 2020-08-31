import sys

class Calculator:
    consNumber = 1 / 2

    def __init__(self, numberOne, numberTwo):
        self.numberOne = numberOne
        self.numberTwo = numberTwo

    def add(self):
        return self.numberOne + self.numberTwo

    def sub(self):
        return self.numberOne - self.numberTwo

    def div(self):
        return self.numberOne / self.numberTwo

    def mul(self):
        return self.numberOne * self.numberTwo

    def rightTriangle(self):
        return self.consNumber * self.numberOne * self.numberTwo

    def exit(self):
        return sys.exit()


final = Calculator(int(input('Masukan Angka pertama:  ')),
                   int(input('Masukan Angka ke dua: ')))
print("__________Choose your Operator__________")
print("1. Add")
print("1. Sub")
print("3. Div")
print("4. Mul")
print("5. Triangle")
print("6. Exit")

choice = int(input("Enter Choice: "))
if choice == 1:
    print("Hasilnya adalah: ", final.add())
elif choice == 2:
    print("Hasilnya adalah: ", final.sub())
elif choice == 3:
    print("Hasilnya adalah: ", final.div())
elif choice == 4:
    print("Hasilnya adalah: ", final.mul())
elif choice == 5:
    print("Luas Segitiga adalah: ", final.rightTriangle())
elif choice == 6:
    print("Goodbye My Friend")
else:
    print("Pilihan yang anda masukan tidak ada ")
