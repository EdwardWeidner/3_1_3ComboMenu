print("Menu:\nSandwiches:\n Chicken $5.25\n Beef $6.25\n Tofu $5.75\nDrinks:\n Small $1.00\n Medium $1.50\n Large $2.00\nFries:\n Small $1.00\n Medium $1.50\n Large $2.00")
sandwich = input("What sandwhich would you like?")
if sandwich == "Chicken":
  price = 5.25
elif sandwich == "Beef":
  price = 6.25
elif sandwich == "Tofu":
  price = 5.75
else:
  print("Please answer the question")
beverage = (input("Would you like a drink?"))
if beverage == "No":
  beverage = False
elif beverage == "Yes":
  beverage = True
else:
  print("Please answer the question.")
if beverage == True:
  beveragesize = input("What size would you like?")
  if beveragesize == "Small":
      beverage = "Small Drink"
      price = price + 1.00
  elif beveragesize == "Medium":
    beverage = "Medium Drink"
    price = price + 1.50
  elif beveragesize == "Large":
    beverage = "Large Drink"
    price = price + 2.00
  else:
    print("Please answer the question.")
fries = input("Would you like french fries?")
if fries == "Yes":
   fries = True
elif fries == "No":
  fries = False
if fries == True:
  friessize = input("What size would you like?")
  if friessize == "Small":
    megasize = input("Would you like to mega-size the fries?")
    if megasize == "Yes":
      fries = "Large Fries"
      price = price + 2.00
    elif megasize == "No":
      fries = "Small Fries"
      price = price + 1.00
    else:
      print("Please answer the question.")
  elif friessize == "Medium":
    fires = ("Medium Fries")
    price = price + 1.50
  elif friessize == "Large":
    fries = "Large"
    price = price + 2.00
  else:
    print("Please answer the question.")
ketchup = int(input("How many ketchup packets would you like?"))
price = price + abs(ketchup)* .25
if beverage and fries ==True:
  price = price - 1.00
price = "$" + str(price)
print(sandwich, beverage, fries)
print(price)