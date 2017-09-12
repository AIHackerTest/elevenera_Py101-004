# coding: utf-8

from sys import exit
from random import randint

number = randint(0,20)
guess = int(input("请输入数字："))
guesses = 0
times = 10 - guesses

while guess != number and guesses < 10:
    if guess > number:
        print("比正确答案大了")
        guesses += 1
        times -= 1
        print("你还有%d次机会" % times)
        guess = int(input("请输入数字："))
    elif guess < number:
        print("比正确答案小了")
        guesses += 1
        times -= 1
        print("你还有%d次机会" % times)
        guess = int(input("请输入数字："))
    else:
        print("请确保输入的数字")

if guess == number:
    print("答案正确，答案就是%s" % guess)
    exit(1)

else:
    print("sorry,wrong")
    exit(1)
