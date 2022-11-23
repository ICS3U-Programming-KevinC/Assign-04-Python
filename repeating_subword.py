# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Nov. 14, 2022
# This program asks the user for a string, the length of the subword,
# and how many times to repeat it, then cuts out the subword and repeats it
# the correct number of times


def inputs():
    # makes the variables global so they can be accessed later in the code
    global user_string
    global num_repeat_str
    global subword_len_str

    # gets all required user inputs
    user_string = input("Please enter a string: ")
    num_repeat_str = input("Please enter the number of copies: ")
    subword_len_str = input("Please enter the length of the subword: ")


# error checking
def errors():
    # access global variables
    global num_repeat_int
    global subword_len_int

    try:
        # cast the user inputs into integers
        num_repeat_int = int(num_repeat_str)
        subword_len_int = int(subword_len_str)

        # checks if the inputs are less than or equal to zero
        if (num_repeat_int <= 0) | (subword_len_int <= 0):
            print("Please enter a positive integer")

    # catch errors
    except:
        print("Please enter a valid integer")
        exit()


def get_subword():
    # access global variables
    global subword

    # sets the subword to the cut initial word
    subword = str(user_string[:subword_len_int])


def loop():
    # loop through and repeat the sub word the user specified amount of times
    for counter in range(num_repeat_int):
        print(subword, end="")

    # once the loop has completed add extra line
    print()


# calls all of the functions in the correct order
def main():
    inputs()
    errors()
    get_subword()
    loop()


if __name__ == "__main__":
    main()
