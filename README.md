# PasswordCrackCalc
List of scripts i use to estimate the complexity of password and token bruteforce

This list of script can be completed, if you have any suggestions or code to share, don't hesitate to contact me.

## Requirement

- Python 3
- numpy and pyplot libraries

## Scripts

### Password Bruteforce

Parameters :
- Number of password tested per seconds 
- Complexity of the password (set of characters ^ password length)
- 
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


