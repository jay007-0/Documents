#numStudents = int(input("Enter the number of students: "))
#
#roster = []
#for i in range(numStudents):
#    roster.append(input())
#
#print("\nStudent Roster")
#print(str(roster))
#
#reverse = []
#index = 1
#for i in range(10):
#    reverse.append(int(input("Enter number " + str(index) + ": ")))
#    index += 1
#
#print(str(reverse))
#reverse.sort(reverse=True)
#print("\nCountdown\n")
#print(str(reverse))

def celsius_to_fahrenheit(temp):
    temp = (float(temp) * 9 / 5) + 32
    return temp


def fahrenheit_to_celsius(temp):
    temp = (float(temp)-32) * 5 / 9
    return temp

print("Welcome to Temperature Converter!\n")

cont = True

while cont == True: #cont is continue the program
    print("Press \'f\' for celsius to fahrenheit or \'c\' for fahrenheit to celsius.")
    choice = input().lower()
    temp = input("Enter a temperature: ")
    if choice == 'f':
        print(f"{int(celsius_to_fahrenheit(temp))} °F")
    elif choice == 'c':
        print(f"{int(fahrenheit_to_celsius(temp))} °C")
    else:
        print("Invalid choice.")
    answer = input("Do you wish to continue? y/n").lower()
    if answer == "y":
        cont = True
    elif answer == "n":
        cont = False
    else:
        print("Invalid choice.")
