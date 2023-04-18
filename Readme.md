Readme.md

# paycalc

### Paycalc is a program written in C to convert one rate of pay to another.
    User enters a pay amount.
    User selects the frequency of the entered amount.
        [1] hourly
        [2] weekly
        [3] bi-weekly
        [4] monthly
        [5] annually
    User selects the frequency to convert to.
        same as above
        hidden option of [0] will perform all calculations
    User can exit at either menu by selecting [6] to exit.
    Requested calculations will be displayed to User.
    User can select [1] to perform another calculation, or [2] to exit.

## Paycalc rewrite in Python

### payCalc.py
    Re-Write from the C version
    Uses if...elif statements
    Runs in a 'True' While loop
    Adds 'C' to Continue or 'Q' to Quit
        anything other than 'Q' or 'q' will continue the loop
    Arguements are now passed to the Functions
    User can no longer exit excpet at end

### payCalc2.py
    Modified from payCalc.py
    Replaces if...elif with match...case

### payCalc3.py / Paycalc3.exe
    Modified from payCalc2.py
    Imports os, and time Modules
    Adds Function to Clear the Screen
        utilizes os.system
            uses 'cls' to clear the screen in Windows
    Includes String Splicing
        takes only the first character input
    Adds Error Handling for Pay Input
        returns 'Invalid Entry' on error
        uses time.sleep for delay
        uses 'continue' to restart loop
        allows 3 consecutive attempts
            returns '*****OPERATION TERMINATED*****'
            uses time.sleep for delay
            uses 'break' to end loop
    
    


