#Connor Schoonbee 20231473
dozen = int(12)
#1.1). Prompt the user for the number of eggs.
eggs = int(input("How many eggs would you like to order? :"))

dozEggsPrice = 3.25
eggPrice = 0.45
#1.2). Calculate the number of dozens and loose eggs.
dozEggs =eggs//dozen
looseEggs = eggs % dozen
#1.3 and 1.4) calculate final price/print the final amount
dozEggsPriceTotal = dozEggs*dozEggsPrice
print("You ordered",eggs,"eggs.","Thats",dozEggs,"dozen eggs at R3.25 per dozen and",\
    looseEggs ,"loose eggs at 45c for a total of:  R",dozEggsPriceTotal + looseEggs*eggPrice)



