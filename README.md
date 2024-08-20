# PasswordCrackCalc
List of scripts i use to estimate the complexity of password and token bruteforce

This list of script can be completed, if you have any suggestions or code to share, don't hesitate to contact me.

## Requirement

- Python 3
- numpy and pyplot libraries

## Scripts

### Char Set

Simple script to help you quickly find out the number of different characters from a password policy.
It is also used to calculate the nummber of potential password from this policy.

### Password Bruteforce

A password lenght, a bruteforce rate ? This script will tell you how long it will take to crack it
As this script is cool, it will adapt the scale to the time it will take to crack the password (from second to century)

Parameters :
- Number of password tested per seconds 
- Complexity of the password (set of characters ^ password length)
  

### Reset Token Bruteforce (time limit)

This script is used to calculate optimal transition from token generation to brute force.

Requirement : 
1. Reset token can be created without cancelling the previous reset token. (Unlimited number of token)
2. Reset token are valid a limit period of time

Parameters :
- Number of password tested per seconds 
- Number of token created per seconds
- Lifetime of a reset token
- Complexity of the token (set of characters ^ token length)
- Limit number of reset token (optionnal)


