# =========================================================
#
# this module does validation
# written by zi chen                          09/05/2022

#
# =========================================================


# this function check the length of a text
# parameters data mean the text you want to check , length mean the length want to check
# option is the type user want to check, done by given integer as argument
# 1 means ==,2 mean > ,3  mean lower than 
def check_length(data, length, option=1):
    if option == 1:
        if len(data) == length:
            return True
        else:
            return False
    elif option == 2:
        if len(data) > length:
            return True
        else:
            return False
    elif option == 3:
        if len(data) < length:
            return True
        else:
            return False
    else:
        return False

#
def check_range(data:int ,needed_range:tuple[int]):
    print(needed_range)
    for i in range(needed_range[0],needed_range[1]):
        if data==i:
            return True
    else:
        return False 


if __name__ == "__main__":
    # testing
##    print(check_length("abc", 2, 1))
##    print(check_length("abc", 2, 2))
##    print(check_length("abc", 2, 3))
##  print(check_length("abc", 1, 1))
      print(check_range(1,(1,3)))
