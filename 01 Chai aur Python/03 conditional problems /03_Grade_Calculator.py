grade = int(input("Enter your grade: "))

if 100>= grade >=80 :
    print('A')
elif 69 < grade < 80:
    print('B')
elif 59 < grade < 70:
    print('C')
elif 49 < grade < 60:
    print('D')
elif 0 < grade < 50:
    print('F')
else: 
    print('Invalid Input')