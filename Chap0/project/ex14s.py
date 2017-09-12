from sys import argv

script, user_name, user_age = argv
prompt = '>>>>please type here: >>>>'

print ("Hi, %s, I'm the %s script. You are %s years old." % (user_name, script, user_age))
print ("I'd like to ask you a few questions.")


print ("Do you like me %s?" % user_name)
likes = input(prompt)

print ("Where do you live %s?" % user_name)
lives = input(prompt)

print ("What kind of computer do you have?")
computer = input(prompt)

print ("How old will be you next year?")
age = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
You will be %r years old next year.
""" % (likes, lives, computer, age))
