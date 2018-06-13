name = input("What is the name of the order")
print("hello " +name+ ".")
print("What pizza would you like to order")

def Pizza():
     print("1:    Beef & Onion")
     print("2:    Hawaiian")
     print("3:    Meat Lovers")
     print("4:    Pepperoni")
     print("5:    Ham & Cheese")
     print("6:    Classic Cheese")
     print("7:    Veg Hot 'n' Spicy")
     print("8:    Gluten Free")
     print("9:    Seafood Deluxe")
     print("10:   Italiano")
Pizza();
def PizzaCost(totalpizza, hourlyWage):

    if totalPizzas<= 30:
        totalCosts = hourlyWage*totalPizzas
    else:
        overtime = totalHours - 30
        totalWages = hourlyWage*30 + (1.5*hourlyWage)*overtime
    return PizzaCost

def main():
    hours = float(input('What pizza would you like to order?'))
    wage = 1
    total = calcWeeklyWages(hours, wage)
    print('Total pizza costs - ${total:.2f}.'
           .format(**locals()))
main()

print ("Would you like to order another pizza?")


print("")
answer = str(input("Would you like to  have you pizza delivered Yes/No"))
proceed = "Yes" or "yes" or "Y" or "YES" or "y"

dontProceed = "no" or "No" or "NO" or "n"

if answer + proceed:
    adress = input("what is your current adress")
    print("The pizza will be sent this adress - " +adress+ ".")




elif dontProceed:

    print("well shit")




class MyClass:
        varrible = "blah"

        def function(self):
            print("yo wat op")









"""
num = 1
if num <2:
    print(num, "is a good choice")
    print ("this is always printed")

num = 1
if num > 0:
    print(num, "is a positive number")
    print ("this is always printed")
"""
