print("Learn your squares and cubes!")
enternum = int(input("Enter an integer: "))

print(" Number        Squared:        Cubed:")
print("========      ==========      =========")

for num in range(1, enternum + 1):
    squared = num ** 2
    cubed = num ** 3
    print(f"{num}                {squared}              1{cubed}")

choice = input("Continue? (y/n): ")

while choice == 'y':
    enternum = int(input("Enter an integer: "))
    print(" Number        Squared:        Cubed:")
    print("========      ==========      =========")

    for num in range(1, enternum + 1):
        squared = num ** 2
        cubed = num ** 3
        print(f"{num}                 {squared}              {cubed}")
    choice = input("Continue? (y/n): ")

if choice == 'n':
    print("See you later!")