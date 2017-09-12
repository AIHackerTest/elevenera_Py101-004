def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print ("You have %d cheese!" % cheese_count)
    print ("You have %d boxes of crackers!" % boxes_of_crackers)
    print ("Man that's enough for a party!")
    print ("Get a blanket.\n")


print ("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print ("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print ("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print ("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def icecream_and_cole(icecream_count, cups_of_cole):
    print ("I have %d icecream." % icecream_count)
    print ("I have %d cole." % cups_of_cole)


icecream_and_cole(8, 11)


icecream_and_cole(8+10, 11+10)


x = 10
y = 20

icecream_and_cole(x, y)


icecream_and_cole(x+10, y+10)
