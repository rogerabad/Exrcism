def leap_year(year):
    # Funcion que determina si un año es bisiesto
    if year%4 == 0:
        if year%100 != 0:
            return True
        else:
            if year%400 == 0:
                return True 
            return False
    return False
            
