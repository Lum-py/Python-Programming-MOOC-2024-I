# Write your solution here
from datetime import datetime
def is_it_valid(pic: str):
    control_chars = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    if len(pic) != 11:
        return False
    
    dob = pic[:6]
    century_marker = pic[6]
    pers_id = pic[7:10]
    
    year = int(pic[4:6])
    if century_marker == "+":
        year += 1800
    elif century_marker == "-":
        year += 1900
    elif century_marker == "A":
        year += 2000
    
    try:
        datetime(year, int(dob[2:4]), int(dob[:2]))
    except ValueError:
        return False
    
    try:
        num = int(dob + pers_id)
        remainder = num % 31
        control_char = control_chars[remainder]
    except ValueError:
        return False
    
    if control_char != pic[-1]:
        return False
    
    return True

   
if __name__ == "__main__":
    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))
    print(is_it_valid("290200-1239"))
