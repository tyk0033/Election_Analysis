#What is the score?
score= int(input("What is your test scpore? "))

#Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 60:
            print('Your sgrade is a C.')
        else:
            print('Your grade is an F.')