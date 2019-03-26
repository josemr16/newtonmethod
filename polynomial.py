#Author: Jose Rodriguez
#CSI 33 Final Project
#Newton Method

class polynomial:

    #------------------------------------------------------------
    
    def __init__(self, fx):
        """Pre: fx is a polinomial funtion in the following form, for 3x^2+5x
        enter 3 x 2 + 5 x, for 33x^3-7x enter 33 x 3 - 7 x. the variable x
        can be represented with any other letter"""

        for item in fx: 
            if item != '+' and item != '-' and item !=" " and not(item.isdigit()):
                fx = fx.replace(item,'x') # Change any other variable to x

        self.fx = fx

    #------------------------------------------------------------

    def __str__ (self):
        """Post: returns the value of fx"""
        
        return self.fx 
    

    #------------------------------------------------------------

    def derivative(self):
        """Pre: self is a polynomial funtion separated by space.
           Post: return an instance of the class polynomial with the
           derivative of self as the value."""
        
        # if self is a string convert it to a list set it to il
        # otherwise leave it like that and set it to il
        try:
            il = self.fx.split()
        except AttributeError:
            il= [i for i in self.fx]

        l=[] # list for strigs and integers separation
        ol=[] # list where derivative will be stored
        
        for item in il:
            if item.isdigit(): 
                l.append(int(item)) #coverting digits to integers and appending
                                        # them to list l
            else:   # just appending if the item is not digit
                l.append(item)

        if l[-1] == 'x':  # if last element is x, append a 1 to make it easier
                               # to find derivative
           l.append(1)
           
        if l[0] == 'x': # if first element is x, insert a 1 to make it easier
                            # to find derivative
            l.insert(0,1)


        for item in l: # for loop to determine what to append to de list
                        # containing the derivative
            if item == 'x':
                i=l.index('x') # get the index of the first x
                l[i]=None  # set that x to none in order to find the index of next x
                a=l[i-1]  # set the item left to the x to a
                b=l[i+1]  # set the item right to the x to b

                # Handle all possible cases
                #Case 1; a and b are numbers
                if (a != '-' and a != '+') and (b != "+" and b != '-'):
        
                    ol.append(a*b)
                    if b > 1:
                        ol.append('x')
                    if b > 2:
                        ol.append(b-1)
                
                #Case 2; a and b are not numbers
                elif (a == '-' or a == '+') and (b == "+" or b == '-'):
                    ol.append(1)

                #Case 3; a is a number and b is not
                elif (a != '+' or a !=  '-') and (b == '+' or b == '-'):
                    ol.append(a)

                #Case 4; b is a number and a is not
                elif (b != '+' or b != '-') and (a == '-' or a == '+'):
                    ol.append(b)
                    ol.append('x')
                    if b > 2:
                        ol.append(b-1)
            # if the item is + or - just append it to the list containig derivative                   
            elif item == "+" or item == "-":
                ol.append(item)

        if ol[0] == '+':  # Deleting unnecessary items from list 
            del ol[0]

        if ol[-1] == '+' or ol[-1] == '-':
            del ol[-1]
    
        #return ol
        s=" ".join(str(i) for i in ol)

        return polynomial(s)
            
    

    #------------------------------------------------------------


    def evaluate(self, x):
        """Pre:x is the number where the funtion will be evaluated.
           Post: returns the value of the funtion evaluated at x."""
        

        nl=[]  # list containing the funtion and operations signs to evaluate 
        
        try:  # if self.fx is a string, make it a list. Else, leave it as it is
            self.fx = self.fx.split()
        except AttributeError:
            pass

        # create a copy of self.fx to avoid mutuation of it    
        copy=[i for i in self.fx] 

        if copy[-1] == 'x': 
        
            copy.append(1)
            
        if copy[0] == 'x':
        
            copy.insert(0,1)
    
        #iterate in the items to determine what to do
        for i in copy: 

            if i == 'x':
                i=copy.index('x')  # get the index of the first x
                copy[i]=None # set that x to none in order to find the index of next x
                a=copy[i-1] # set the item left to the x to a
                b=copy[i+1]  # set the item right to the x to b

                #case 1: Both a and b are numbers
                if (a != '-' and a != '+') and (b != "+" and b != '-'):
                
                    nl.append('*')
                    nl.append(x)
                    nl.append('**')

                #Case 2: a and b are not numbers
                elif (a == '-' or a == '+') and (b == "+" or b == '-'):
                    nl.append(x)

                #Case 3: a is a number and b is not
                elif (a != '+' or a !=  '-') and (b == '+' or b == '-'):
        
                    nl.append('*')
                    nl.append(x)
                
                #Case 4; b is a number and a is not
                elif (b != '+' or b != '-') and (a == '-' or a == '+'):
                    nl.append(x)
                    nl.append('**')

            else: 
                nl.append(i)

        #coverting list to string for easy evaluation               
        s="".join(str(i) for i in nl)
    
        # set result to evaluation and return it
        result =eval(s)
    
        return result



        

        
        
