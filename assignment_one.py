__author__ = "Samantha Kuang"
__email__ = "samxhk@bu.edu"

def main():
    """ The main function runs through questions 2 to 6. Without argument parser.
    """
    # to run question 2:
    print("QUESTION 2:\t")
    print_multiplication_table()

    # to run question 3:
    print("\nQUESTION 3:\t")
    is_palindrome()

    # to run question 4:
    print("\nQUESTION 4:\t")
    alternate_lists()

    # to run question 5:
    print("\nQUESTION 5:\t")
    calc_fib(100)

    #to run question 6:
    print("\nQUESTION 6:\t")
    print(is_leap_year())

def print_multiplication_table(n=12):
    """ Prints mutliplication Table up to n. n = 12 as default
       
    Args:
        n (str): integer for multiplying up to

    Returns:
        prints the multiplication table
    """
    first_int_list = [i for i in range(1, n+1)]
    second_int_list = [j for j in range(1, n+1)]

    results = []
    for first_int in first_int_list:
        for second_int in second_int_list:
            results.append(first_int * second_int)

    subset = []
    for i in results:
        if len(subset)< 12:
            subset.append(i)
        else:
            print(subset)
            subset = []
            subset.append(i)
    print(subset)


def is_palindrome():
    """ Determines in the user input string is a palindrome. Must type q for program to exist.

    Args:
        s (str): The string to check
    
    Returns:
        prints “The string <the string the user typed in> [is | is not] a palindrome."
    """
    check_string = input("provide a string to check if it is a palindrome: ")

    reverse_string = check_string[::-1]

    if check_string == reverse_string:
        print(f"The string {check_string} is a palindrome.") 
    else:
        print(f"The string {check_string} is NOT a palindrome.")
    
    while True:
        key = input("Enter 'q' to exit program!")
        if key.lower() == 'q':
            break


def alternate_lists():
    """ Take in two lists and checks if they're the same length.
    Combine the two lists by alternating the elements.

    Args:
        lst_one (list): first list
        lst_two (list): second list

    Returns:
        prints the alternating string
    """

    print("Please provide 2 list of equal length as such : [a,b,c] and [1,2,3]")
    lst_one= input("Provide First List: ")
    lst_two= input("Provide Second List: ")

    lst_one = lst_one.strip('[]"').split(',')
    lst_two = lst_two.strip('[]"').split(',')

    if not len(lst_one) == len(lst_two):
        raise Exception("Lists are NOT the same length. Expected same length lists.")
    combine_alternate_lst = []
    for i in range(len(lst_one)):
        combine_alternate_lst.append(lst_one[i])
        combine_alternate_lst.append(lst_two[i])

    print(combine_alternate_lst)

def calc_fib(x):
    """
    """
    calculated = {1: 1, 2: 1}  # Initialize with base cases, starting with 1, 1

    def fibonacci_of(n):
        # Check if the value is already calculated
        if n in calculated:
            return calculated[n]

        calculated[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)
        return calculated[n]

    fibonacci_of(x)
    print(f"- fibonacci of {x} is {calculated.get(x)}!")
    print(f"- fibonacci sequence up to {x}:\n\t{list(calculated.values())}")

def is_leap_year():
    """reference 
    https://learn.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year#how-to-determine-whether-a-year-is-a-leap-year

    If year is evenly dividiable by 4, not evenly divisible by 100 then it's a leap year
    If year is evenly divisible by 4, 100, and 400 then it's a leap year

    """
    year= int(input("Provide a year to check if it is a leap year. "))
    if year%4 == 0:
        if year% 100 == 0:
            if year%400 == 0:
                return f"{year} IS a leap year."
            else:
                return f"{year} is NOT a leap year."
        else:
            return f"{year} IS a leap year."
    else:
        return f"{year} is NOT a leap year."


if __name__ == '__main__':
    # run assignment one
    main()
    