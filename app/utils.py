




def to_usd(my_price):
    """
    Invoke like this: to_usd(9.9999)

    Example return value "$9.99"
    """
    return '${:,.2f}'.format(my_price)


if __name__ == "__main__":
    # if this code is in the global scope
    # ... of a file we're trying to import from 
    # ... it will throw errors when we try to run those.
    
    # nesting code in the main conditional will 
    # allow other scripts to cleanly import functions from this file
    # without running this code 

    # this code still gets run when we invoke the script from the command line  
    price = input("Please choose a price like 4.9999: ")
    print(to_usd(float(price)))


