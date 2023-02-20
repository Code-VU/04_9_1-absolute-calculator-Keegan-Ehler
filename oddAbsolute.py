def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = int (input ("Enter a number: "))
    
    if int(in_num) > 21:
        in_num = (in_num - 21) * 2
        print (f"Result: {in_num}")
    elif int(in_num) < 21:
        in_num = (in_num - 21) * -1
        print (f"Result: {in_num}")
    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
