import math


def delta(a, b, c):
    delta = (pow(b,2))-(4*a*c)
    return delta

def kwadrat2(a, b, delta):      
    sdelta = math.sqrt(delta)       #sdelta = pierwiastek delty
    
    x1 = (0-b-sdelta)/(2*a)
    x2 = (0-b+sdelta)/(2*a)
    return x1, x2

def kwadrat1(a, b):
    x = (0-b)/(2*a)
    return x

def kwadrat0(a, b, c):
    sdelta = math.sqrt(((4*a*c)-(pow(b,2))))
    sdelta = complex(0, sdelta)     #przeniesienie delty na wartość zespoloną

    x1 = (0-b-sdelta)/(2*a)
    x2 = (0-b+sdelta)/(2*a)
    return x1, x2
    


while 1:
    print("\n\n\n \t\t Kalkulator funkcji kwadratowej \n")
    try:
        a = int(input("podaj a: "))
        b = int(input("podaj b: "))
        c = int(input("podaj c: "))     #wpisywanie danych

        print("\nwynik to:")
    
        d = delta(a, b, c)              #rozpoznanie rozwiązań
        if d>0:
            print(kwadrat2(a, b, d))
    
        elif d==0:
            print(kwadrat1(a, b))
    
        else:
            print(kwadrat0(a, b, c))
            
    except:
        print("złe dane")

    print("n - nowe dane \t\t inny klawisz - wyjdź")    #wychodzenie z programu
    if input()!="n":
        break


