weight = int(input())
height = float(input())

hasil = weight / height**2

if hasil < 18.5:
    print ('Underweight')
elif hasil >= 18.5 and hasil < 25:
    print ('Normal')
elif hasil >= 25 and hasil < 30:
    print ('Overweight')
elif hasil > 30:
    print ('Obesity')
