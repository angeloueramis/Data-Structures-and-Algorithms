import matplotlib.pyplot as plt
import math as m

print("1. x^2 + 7x + 2")
print("2. 3x + 2")
print("3. x^2")
print("4. x^3")
print("5. x^5")
print("6. x^3 + 2x^2 + x + 10")
print("7. x^4 - 3x^3 + 2x^2 + 100")
print("8. sin(x)")
print("9. cos(x)")
print("10. x^5 + 4x^4 + x^3 - 2x^2 + 100")
print()
prob = int(input("Choose a number (1-10) to perform the equation."))

vx = list(range(1,51))

def p1():
    result = []
    for x in vx:
        numx = x
        result.append((numx*numx)+(7*numx)+2)
    return result
def p2():
        result = []
        for x in vx:
            numx = x
            result.append((3*numx)+2)
        return result
def p3():
        result = []
        for x in vx:
            numx = x
            result.append(numx*numx)
        return result
def p4():
        result = []
        for x in vx:
            numx = x
            result.append(numx*numx*numx)
        return result
def p5():
        result = []
        for x in vx:
            numx = x
            result.append(numx*numx*numx*numx*numx)
        return result
def p6():
        result = []
        for x in vx:
            numx = x
            result.append((numx*numx*numx)+2*(numx*numx)+numx+13)
        return result
def p7():
        result = []
        for x in vx:
            numx = x
            result.append((numx*numx*numx*numx)-3*(numx*numx*numx)+2*(numx*numx)-numx+11)
        return result
def p8():
        result = []
        for x in vx:
            numx = x
            result.append(m.sin(numx))
        return result
def p9():
        result = []
        for x in vx:
            numx = x
            result.append(m.cos(numx))
        return result
def p10():
        result = []
        for x in vx:
            numx = x
            result.append((numx*numx*numx*numx*numx)+4*(numx*numx*numx*numx)+(numx*numx*numx)-2*(numx*numx)+100)
        return result

with open("input.txt", 'w') as file:
    if 1<=prob<=10:
        if prob==1:
            results = p1()
            file.write(str(p1()))
            plt.figure(1)
            plt.plot(vx, results, 'g', label="Equation 1")

        elif prob==2:
            file.write(str(p2()))
            plt.figure(1)
            plt.plot(vx, p2(), 'b', label="Equation 2")

        elif prob==3:
            file.write(str(p3()))
            plt.figure(1)
            plt.plot(vx, p3(), 'r', label="Equation 3")

        elif prob==4:
            file.write(str(p4()))
            plt.figure(1)
            plt.plot(vx, p4(), 'g', label="Equation 4")

        elif prob==5:
            file.write(str(p5()))
            plt.figure(1)
            plt.plot(vx, p5(), 'b', label="Equation 5")

        elif prob==6:
            file.write(str(p6()))
            plt.figure(1)
            plt.plot(vx, p6(), 'r', label="Equation 6")

        elif prob==7:
            file.write(str(p7()))
            plt.figure(1)
            plt.plot(vx, p7(), 'g', label="Equation 7")

        elif prob==8:
            file.write(str(p8()))
            plt.figure(1)
            plt.plot(vx, p8(), 'b', label="Equation 8")

        elif prob==9:
            file.write(str(p9()))
            plt.figure(1)
            plt.plot(vx, p9(), 'r', label="Equation 9")

        elif prob==10:
            file.write(str(p10()))
            plt.figure(1)
            plt.plot(vx, p10(), 'b', label="Equation 10")

        plt.ylabel('Result')  
        plt.xlabel('x-value')
        plt.legend() 
        plt.show()

    else:
        print("Number is incorrect. Choose between 1-10.")
