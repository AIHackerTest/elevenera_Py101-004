print ("How old are you?",end="")
age = int(input())
print ("How tall are you?",end="")
height = int(input())
print ("How much do you weight?",end="")
weight = int(input())

print ("So, you're %r old, %r tall and %r heavy." % (
      age, height, weight))
print ("If I add %r, %r and %r I get %r." % (
      age, height, weight, age+height+weight))
