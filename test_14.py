def my_div(num, denom):
    try:
        res = num / denom
        print("Divide {0} by {1} results in {2}".format(num, denom, res))
    except ZeroDivisionError:
        print("Sorry, I'm not able to divide {0} by {1} as I am not allowed to divide by zero".format(num, denom))
    except:
        print("Sorry, I'm not able to divide '{0}' by '{1}' and I don't understand why".format(num, denom))
    finally:
        print("Thank you for using me, have a nice day!")

my_div(3, 2)

my_div(6, 0)

my_div(0, 6)

my_div(2.5, 0.0)

my_div(2.5, 0.000000000000000000000000000000000000001)




my_div('hello', 'world')
