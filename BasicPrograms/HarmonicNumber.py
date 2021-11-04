try:
    number = int(input("Enter A Number: "))
    assert number!=0
except:
    print("Number Is Zero")
else:    
    harmonic=0
    for i in range(1,number+1):
        harmonic=harmonic+1/i
        print(harmonic)