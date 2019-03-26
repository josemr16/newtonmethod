from polynomial import*

def intro():
    """Intro of the program"""
    
    print("This program computes the approximated solution of a given equation")
    print("in the form f(x)=0 and an initial solution using Newton's method.\n")        
    print("The equation can either be given by the user using the keyboard or")
    print("by a file. When using a file please make sure that the equation")
    print("is on the first line of the file and the intial solution is in the second line.")
    print("Also know that each element must be separated by a space.\n")
          
def keyboard():
    """Uses the keyboard as input method for computing the Newton method."""

    fx = polynomial(input("Enter f(x),separated by space Ex for (10x^2+5x) enter (10 x 2 + 5 x): "))
    x1 = float(input("\nEnter the first approximation of the equation: "))
    iterations = int(input("Enter which approximation would you like to compute(ex: 2 for second):" ))

    for i in range(iterations-1):
        a = fx.evaluate(x1)
        b = fx.derivative().evaluate(x1)

        x1 = x1 -(a/b)

    print("\nBy the newton method your approximated solution is", round(x1,4))

def file():
    """Uses the keyboard as input method for computing the Newton method."""

    infilename = input("Please enter the name of the file: ")
    infile = open(infilename,'r')

    q = infile.readline()
    q = q.split()
    q = " ".join(i for i in q)
    print()
    print(q, "<< Equation found in the file.")
    z = infile.readline()
    print(z, "<< First approximation found in the file.\n")
    
    fx = polynomial(q)
    x1 = float(z)
    infile.close()
    iterations = int(input("Enter which approximation would you like to compute(ex: 2 for second):" ))

    for i in range(iterations-1):
        a = fx.evaluate(x1)
        b = fx.derivative().evaluate(x1)

        x1 = x1 -(a/b)

    print("\nBy the newton method your approximated solution is", round(x1,4))
    
def main():
    """Main funtion to do neccesary calls for computing Newton's method."""

    intro()
    print("How would you like to input your equation?")
    kborfile = input("Enter K for keyboard or F for file: ")
    kborfile = kborfile.lower()
    
    
    if kborfile == ("k"):
        keyboard()

    elif kborfile == ("f"):
        file()

    else:
        print("\nYour input was invalid. Please try again.\n")
        main()

main()
            


    
