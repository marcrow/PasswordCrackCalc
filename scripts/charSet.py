#!/usr/bin/env python
# This script is used to calculate how many different characters can be used in a password policy.
# It is also used to calculate the complexity of a password.

# Usage ; python charSet.py --lower --upper --digits --special --size 9
# If the special flag is set but without a value, the default special characters are used
# Usage ; python charSet.py --lower --upper --digits --special "!@#$%^&*()_+" --size 8
# Usage : python charSet.py 
# The last one will prompt you to enter the values via a prompt

# Import the necessary packages
import argparse


# user variables
special_set = "!@#$*-_+"

base64_set = "abcdefghijklmnopqrstuvwxyz0123456789" # 26 letters + 10 digits (equals are excluded because predictable)

sha256_length = 64
sha512_length = 128
sha1_length = 40
md5_length = 32
md4_length = 32

# hash dictionary
hash_length = {
    "sha256": 64,
    "sha512": 128,
    "sha1": 40,
    "md5": 32,
    "md4": 32
}

hash_set = {
    "sha256": base64_set,
    "sha512": base64_set,
    "sha1": base64_set,
    "md5": base64_set,
    "md4": base64_set
}



# Define the function to calculate the character set
def calculate_char_set(lower, upper, digits, special):
    # Initialize the character set
    char_set = 0

    # Check if the lower case characters are included
    if lower:
        char_set += 26
    

    # Check if the upper case characters are included
    if upper:
        char_set += 26

    # Check if the digits are included
    if digits:
        char_set += 10

    # Check if the special characters are included
    if special:
        char_set += len(special)

    # Return the character set
    return char_set


# Retrieve the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-l", "--lower", action="store_true", help="Include lower case characters")
ap.add_argument("-u", "--upper", action="store_true", help="Include upper case characters")
ap.add_argument("-d", "--digits", action="store_true", help="Include digits")
ap.add_argument("--special", type=str, help="Include special characters")
ap.add_argument("-s", "--user-special", action="store_true", help="Use the default special characters set")
ap.add_argument("-z", "--size", type=int, help="Size of the password")
ap.add_argument("--hash", type=str, help="Hash algorithm (sha256, sha512, sha1, md5, md4)")
args = vars(ap.parse_args())


if args["special"] and args["user_special"]:
    print("Special and user special cannot be set at the same time")
    exit()

# Retrieve the values
hash = None
lower = args["lower"]
upper = args["upper"]
digits = args["digits"]
special = args["special"]
if args["user_special"]:
    special = special_set
size = args["size"]
if args["hash"]:
    hash = args["hash"]
    if hash not in hash_length.keys():
        print(f"Hash algorithm {hash} is not supported")
        exit()
    size = hash_length[hash]
    special = hash_set[hash]
    lower = False
    upper = False
    digits = False



# Check if no arguments are provided
if not any(args.values()):
    # Prompt the user to enter the values
    lower = input("Include lower case characters (y/n): ")
    upper = input("Include upper case characters (y/n): ")
    digits = input("Include digits (y/n): ")
    special = input("Include special characters (y/n): ")
    if special.lower() == "y":
        special = input(f"Enter the special characters (default: {special_set}): ")
        print(f"Special: {special}")
        if special == "" or special.lower() == "default" or special == False:
            special = special_set
            print("Special is set to default")
            print(f"Special: {special}")
    

    size = input("Enter the size of the password: ")

    # Convert the input to boolean values
    lower = True if lower.lower() == "y" else False
    upper = True if upper.lower() == "y" else False
    digits = True if digits.lower() == "y" else False

while size is None or size == "":
    size = input("Enter the size of the password: ")

size = int(size)



# Calculate the character set
char_set = calculate_char_set(lower, upper, digits, special)

# Print the character set
print(f"Character set: {char_set}")
print(f"Number of potential passwords: {char_set**size}")