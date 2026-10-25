#Khaile Vallejo
#Module 1.3 Assignment
#10/25/2026

print("Welcome to Bottles on the Wall!")

def countdown(bottles):
    while bottles >1:
        print(f"{bottles} bottles of beer on the wall,")
        print(f"{bottles} bottles of beer.")
        print("Take one down, pass it around,")
        bottles -= 1

        if bottles == 1:
            print("1 bottle of beer on the wall!\n")
        else:
            print(f"{bottles} bottles of beer on the wall!\n")

    if bottles == 1:
        print("1 bottle of beer on the wall,")
        print("1 bottle of beer.")
        print("Take one down, pass it around,")
        print("No more bottles of beer on the wall!\n")

def main():
    bottles = int(input("How many bottles of beer on the wall? "))
    countdown(bottles)
    print("Time to buy more bottles of beer!")

main()
