def leap_year():
    print ("TO DO")
    año = int(input ("Ingrese un año: "))
    if año % 100 == 0 and año % 4 == 0:
        if año % 400 == 0:
                print (f"El año {año} es bisiesto") 
        else:
                print (f"El año {año} no es bisiesto")
    
    if año % 4 == 0 and not año % 100 == 0:
       print (f"El año {año} es bisiesto")
