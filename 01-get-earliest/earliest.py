#%%
def parse_date(stringdate):
    """
    E.g. "03/11/2018" parses to 03 month (March), 11 day, 2018 year
    """
    MM, DD, YYYY=stringdate.split('/')
    return int(DD),int(MM),int(YYYY)

#%%
#parse_date("03/11/2018")
def get_earliest(firstdate,seconddate):
    """
    Compare 2 dates (string input) and return the earlier date
    """
    first_d,first_m,first_y=parse_date(firstdate)
    second_d,second_m,second_y=parse_date(seconddate)

    if first_y==second_y:
        if first_m==second_m:
            if first_d==second_d:
                return 'No solution'
            elif first_d>second_d:
                return seconddate
        elif first_m>second_m:
            return seconddate
    elif first_y>second_y:
        return seconddate
    
    return firstdate
