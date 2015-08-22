from random import randint

code = '%d%d%d' % (randint(1,9), randint(1,9), randint(1,9))

print code

guess = raw_input("> ")
guesses = 0
cheat = 666

while guess != code and guesses < 9:
    print 'False'
    guess = raw_input("> ")
    guesses += 1
if guess == code or guess == cheat:
    print 'Pass'
else:
    print 'False'
