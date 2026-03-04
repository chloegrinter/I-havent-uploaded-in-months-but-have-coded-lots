print("1...animals")
print(" ")
print("2...birds")
print("")

choice = int(input("Press 1 or 2 "))
print("")

if choice == 1:
    with open("animals.txt", mode="r") as my_file:
        for line in my_file:
            print(line.rstrip("\n"))
        myfile.close()
elif choice == 2:
    with open("birds.txt", mode="r") as my_file:
        for line in my_file:
            print(line.rstrip("\n"))
        myfile.close()
