while True:
    print("\nWelcome to the Bill Splitter App!")

    billamt = float(input("Enter total bill amount: "))
    ppl = int(input("Enter number of people: "))
    tip = int(input("Enter tip percentage (0/5/10/15/20): "))

    tipamt = (tip / 100) * billamt
    finalbill = billamt + tipamt
    perperson = finalbill / ppl

    print(f"\nTip Amount: Rs{tipamt:}")
    print(f"Total bill (with tip): Rs{finalbill:}")
    print(f"Each person should pay: Rs{perperson:}")

    again = input("\nWould you like to calculate another bill? (y/n): ")
    if again.lower() != 'y':
        break  
