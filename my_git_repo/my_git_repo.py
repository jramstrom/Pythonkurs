for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:  # Här kontrollerar vi om talet är delbart med 3 och 5
        print("FizzBuzz")
    elif i % 3 == 0:  # Här kontrollerar vi om talet är delbart med 3
        print("Fizz")
    elif i % 5 == 0:  # Här kontrollerar vi om talet är delbart med 5
        print("Buzz")
    else:
        print(i)  # Om ingen av reglerna gäller, skriver programmet bara ut talet
