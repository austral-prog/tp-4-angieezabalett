def leap_year():
    año = int(input ("Ingrese un año: "))
        if año % 4 == 0 or año % 400 == 0:
            print ("El año es bisiesto")
        else:
            print ("El año no es bisiesto")
