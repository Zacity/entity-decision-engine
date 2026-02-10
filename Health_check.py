name = input("What is your name? ")


while True:
    age_input = input("What is your age? ")

    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Please enter valid number.")  

print("\n--- Health Check Results ---")

if age < 18:
    print("status: Minor")
elif age < 40:
    print("Staus : Adult")
elif age < 65:
    print("Staus: Middle-aged")
else:
    print("Status: Senior")

print("Assesment complete for", name)



