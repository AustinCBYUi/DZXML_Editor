# import xml_auto_editor as xml
import xml.etree.ElementTree as ET
# from pathlib import *
from pathlib import *

#Author - Austin Campbell || Released on my school github acc.
#Purpose - Automate types.xml editing without screwing up loot tables / exponential nominal / min values.
# ^^ I know too high nominals / mins can mess with spawns on console, which is why I made this.
#Designed for console use.
#Please read additional documentation on the readme.md, thanks! I hope it works well for you, and you can
#send suggestions to contacts below. feel free to edit as desired. Please message me if you are re-releasing it.
#
#Email - infrared.dayz@gmail.com
#Discord - Danny2#5070


#TODO Remember to switch this for .exe build / public build
file_to_edit = PurePath("types.xml")
#file_to_edit = Path(r"Projects\DZXML_Editor\types.xml") #Dev

#Primary tree and root to be edited.
tree = ET.parse(file_to_edit)
root = tree.getroot()

#Constant for functionality / feedback after performing actions
#Modified message, this is a good sign!
GOOD_MSG = "\n\033[1;32;48m** Modified! **" #Will be Green and bold
#Generic error message
ERROR_MSG = "\033[1;31;48mError. Please re-try.." #Will be red and bold
#Non integer message, only used on user inputs for change_value!
NON_INT_MSG = "\033[1;31;48mError. Inputs must be integers only! Please try again." #Red and bold
#Non option message, only used for option menus!
NON_OPT_MSG = "\033[0;31;48mSorry that is not an option, please try again!" #Just red


#-------- Nominal Modifiers ---------#

#Prompt for multiplying or adding to the nominal values.
def nominal_selection():
    """Selection menu for nominal editing."""
    print("\033[0;33;48m -- Nominal Modifier -- ") #Title
    #Options menu, we can only multiply or add
    multiply_or_add = int(input("\033[1;35;48m Multiply or Add off nominal?(0 = Multiply, 1 = Add):\n"))

    #Multiplication option
    if multiply_or_add == 0:
        #Get input
        change_value = float(input("\033[0;36;48mHow much would you like to multiply each nominal value by? Use integers:\n"))
        #Check if you are trying to multiply too high..
        if change_value >= 6:
            print("\033[0;31;48m Integer is too large. Please try a smaller number.")
            #If you are, return back to the beginning.
            nominal_selection()
        #Passing exception to get down to business changing the nominal value
        elif change_value <= 6 and change_value > 0:
            #Parameter is the change_value variable we have above
            nominal_multiplication_modifier(change_value)
        #Anything aside from 0-6 and anything greater than 6 will be here.
        else:
            #Print our non integer message to user
            print(NON_INT_MSG)
            #return user to top dialog
            nominal_selection()

    #Addition exception
    elif multiply_or_add == 1:
        #Needs to stay as an integer as it is addition. (No point in adding 24.5 to the value if it is only gonna round.)
        change_value = int(input("\033[0;36;48mHow much to add to the nominal? Use integers:\n"))
        #Anything greater than 0 works for me.
        if change_value > 0:
            #Parameter is the change_value variable we have above
            nominal_addition_modifier(change_value)
        #Anything that doesn't fit up there goes down here.
        else:
            #Print the non integer error msg
            print(NON_INT_MSG)
            #Try again now.
            nominal_selection()

    #IF you don't type 0 for mult or 1 for addition you will get this error.
    else:
        print("\033[0;31;48mSorry that is not an option, please try again!")
        nominal_selection()


#Nominal modifiers
#FINISHED
def nominal_multiplication_modifier(change_value):
    """Multiplication modifier for nominal values, takes parameter change_value as a user input value and loops through all
    parts in the root xml to change values."""
    for nominal in root.iter("nominal"):
        #Multiply whatever user input is in the input. Can multiply decimals now too.
        nominal.text = str(round(int(nominal.text) * change_value))
        #We don't need to check for zeros because multiplying anything by 0 will equal 0,
        # but addition ones will have the zero check.
    print(GOOD_MSG)


#-------- Nominal modifiers --------#

#Changing nominal values by adding user value to pre-existing value.
#FINISHED
def nominal_addition_modifier(change_value):
    """Addition modifier for nominal values, takes parameter change_value as a user input value and loops through all
    parts in the root xml to change values. Checks for zeroed nominals and keeps them as a zero using a check."""
    #For loop to loop through the <nominal></nominal> tag
    for nominal in root.iter("nominal"):
        #Add whatever integer the user puts in to the pre-existing value.
        nominal.text = str(int(nominal.text) + change_value)
        #Check for zeros, if we find they're not equal to a zero already
        if nominal.text != "0":
            #Change to what the user wanted
            nominal.text = str(nominal.text)
        #Otherwise if it is a zero,
        elif nominal.text == "0":
            #Keep it set at a zero.
            nominal.text = "0"
        #Everything else will print a error msg, I don't know how you'd even get here.
        else:
            print(ERROR_MSG)
    #Modified message
    print(GOOD_MSG)


#-------- Minimum Modifiers --------#

#function to modify min values. SHOULD BE COMPLETELY FINISHED.
def minimum_selection():
    """Min selection menu for editing min values in xml."""
    #MULTIPLY OR ADD OPTION!
    print("\033[0;33;48m -- Min Modifier -- ") #Title
    multiply_or_add = int(input("\033[0;35;48mMultiply or Add Min? (0 = Multiply, 1 = Add):\n"))

    #Multiply option here
    if multiply_or_add == 0:
        #Using float input for maybe multiplying 2.5x the loot values
        change_value = float(input("\033[0;36;48mHow much to multiply each min value by? Use integers:\n"))
        #Check if you're doing too much real quick..
        if change_value >= 6:
            print("\033[0;31;48m Integer is too large. Please try a smaller number.")
            #If you are, try again.
        #If you're not trying to do too much and you fit my requests you can..
        elif change_value > 0 and change_value <= 6:
            #..Run the function
            minimum_multiplication_modifier(change_value)
        #Anything else will be triggered here
        else:
            #Which has non integer error message
            print(NON_INT_MSG)
            #And returning you to selection again.
            minimum_selection()

    #Addition option here
    elif multiply_or_add == 1:
        #Used to be a float, like above - no point in adding a float because it will just round. Can't have .5 of a loot
        change_value = int(input("\033[0;36;48mHow much to add to each min value? Use integers:\n"))
        #If you put anything higher than 0 I'm happy.
        if change_value > 0:
            #Run the function
            minimum_addition_modifier(change_value)
        #Anything other than 0+++ and you get the non_int_msg
        else:
            #Print the non integer msg
            print(NON_INT_MSG)
            #Return user to selection menu.
            minimum_selection()

    #Not an option on the selection menu - anything other than 0 or 1 throws this error.
    else:
        #Print the non-option-message
        print(NON_OPT_MSG)
        #return user to minimum selection menu
        minimum_selection()


#Modifier to add to mins
#If min value is 2 and you add 4 the new min will be 6.
def minimum_addition_modifier(change_value):
    """Addition modifier for min values, takes parameter change_value as a user input and loops through all
    parts in the root xml to change values."""
    #Loop through all min elements
    for min in root.iter("min"):
        #access values in min and add user input value
        min.text = str(int(min.text) + change_value)
        #Check if it is not 0
        if min.text != "0":
            #If not a 0, go ahead and change to what the user wanted
            min.text = str(min.text)
        #If it is a 0...
        elif min.text == "0":
            #Keep it a 0
            min.text = "0"
        #All else print an error msg
        else:
            print(ERROR_MSG)
    print(GOOD_MSG)


#Modifier to multiply from min
#If min value is 2 and you multiply by 2 the new min will be 4.
def minimum_multiplication_modifier(change_value):
    """Multiplication modifier for min values, takes parameter change_value as a user input and loops through
    all parts in the root xml to change values."""
    #loop through all min elements
    for min in root.iter("min"):
        #access values in min and multiply by user input value
        #This here already converts the stuff to a string outside, but inside is still treated like a integer!
        min.text = str(round(int(min.text) * change_value))
    print(GOOD_MSG)


#-------- Quantmin Modifier --------#
#Commentating my issues with this function:
#Python is always reading the xml as a string, so always convert our inputs or values to a str() first.
def quantmin_modifier():
    """Quantmin modifier, modifies from 0 to 100. Does not modify values set at -1."""
    print("\033[0;33;48m -- Quantmin Modifier -- ") #Title
    print("\033[0;35;48mMust use integer and entire value, so if you want 80% type 80.")
    change_value = int(input("\033[0;36;48mWhat would you like to set the quantmin to?:\n"))
    #If you hit these parameters it will do the following
    if change_value >= 0 and change_value <= 100:
        #Print the modified message now so we can only get one display
        print(GOOD_MSG)
        for quantmin in root.iter("quantmin"):
            quantmin.text = str(int(quantmin.text))
            if quantmin.text != "-1": #The -1 in the xml is a int, but Python is reading as a string, so had to change this to "-1"
                #Set the value to whatever the user typed
                quantmin.text = str(change_value) #Had to add str in front to convert the user input look above for reason
                #If quantmin is already "-1", keep it at "-1"
            elif quantmin.text == "-1":
                quantmin.text = "-1"
            else:
                print(ERROR_MSG)
    else:
        #I guess technically anything over 100 is not an option!
        print(NON_OPT_MSG)
        quantmin_modifier()


#-------- Quantmax Modifier ---------#
def quantmax_modifier():
    """Quantmax modifier, modifies from 0 to 100. Does not modify values set at -1."""
    #Little bit of direction for users
    print("\033[0;33;48m -- Quantmax Modifier -- ") #Title
    print("\033[0;35;48mMust use integer and entire value, so if you want 100% type 100.")
    #Get input
    change_value = int(input("\033[0;36;48mWhat would you like to set quantmax to?:\n"))
    if change_value >= 0 and change_value <= 100:
        print(GOOD_MSG)
        #Run the loop
        for quantmax in root.iter("quantmax"):
            quantmax.text = str(int(quantmax.text))
            if quantmax.text != "-1":
                #Set the value to whatever the user typed
                quantmax.text = str(change_value)
            elif quantmax.text == "-1":
                quantmax.text = "-1"
            else:
                print(ERROR_MSG) #Red
    else:
        print(NON_OPT_MSG)
        #Return to selection
        quantmax_modifier()



#-------- Check Min and Max --------#

#Check the minimum -> nominal values in the document before creating the types_modified.xml file.
def minimum_check():
    """Check the minimum value to the nominal value. If min is greater than nominal, 
    switch bool to True as it is a corrupted file. Otherwise default = False."""
    #Set var to False
    corrupted_file = False
    #Loop through all min values first
    for min in root.iter("min"):
        #capture the values into min.text with str->int conversions
        min.text = str(int(min.text))
    #Same, loop through all nominal values second
    for nom in root.iter("nominal"):
        #capture the values into nom.text with the string to int conversion
        nom.text = (str(int(nom.text)))
    #Now all that so we can just ask if minimum values are greater than nominal values then:
    if min.text > nom.text:
        #Change var to True, now the file is technically corrupted
        corrupted_file = True
    #Otherwise if the min is NOT greater than the nominal or whatever else gets sent here
    else:
        #Changing the var to False, the file is not corrupted
        corrupted_file = False
    #return the corrupted_file bool(True or False) to the options menu when trying to create the new file
    return corrupted_file

#TODO List:
# 3 - Maybe add a lifetime modifier (Why??)
# 4 - Try to get an icon for the .exe so it doesn't look so sketch
# 6 - Build as .exe and include a blank types.xml in a zip with the github code as well.

 #bool for the while loop for the menu.
menu_stop = False

#Begin menu loop
while menu_stop == False:
    #Used a variable instead of a print statement to help cleanliness
    options_menu = """\033[0;36;48m
    DZXML Types Modifier
    Please read the documentation before using. Thank you!\n
    1) Modify Nominal Values
    2) Modify Minimum Values
    3) Modify Quantity Minimum Values
    4) Modify Quantity Maximum Values
    0) Exit and write to new file"""
    #Print out the options menu now
    print(options_menu)
    #Now get the input from the user on which option to utilize
    #Gets just a regular input and allows us to have a cleaner menu with wrong inputs?
    user_selected = (input(""))

    #1111 Option 1 is modifying the nominal values 1111#
    #If you type a string or an int this works because both are supported?
    if user_selected == "1" or user_selected == 1:
        nominal_selection()
    #2222 Option 2 is modifying the min values 2222#
    elif user_selected == "2" or user_selected ==  2:
        minimum_selection()
    #3333 Option 3 is modifying the quantmin values 3333#
    elif user_selected == "3" or user_selected == 3:
        quantmin_modifier()
    #4444 Option 4 is modifying the quantmax values 4444#
    elif user_selected == "4" or user_selected == 4:
        quantmax_modifier()
    #Removed to do as the exe DOES write the program to the same directory as the .exe
    #0000 Option 0 is writing the file! 0000#
    elif user_selected == "0" or user_selected == 0:
        #If this option is ran, we need to check and verify your values first.
        minimum_check()
        #If your values are good then we're good to write the file, so
        if minimum_check() == False:
            #Using the xml package, write to types_modified.xml file
            tree.write("types_modified.xml")
            #Stop the menu loop by setting bool to True
            menu_stop = True
            #Execute the built-in exit function to close the prompt.
            exit(code="Success")
        #If somehow your values got messed up and the min is higher than the nominal then you get this statement
        elif minimum_check() == True:
            #Print error messages to user.
            print("\033[0;31;48mError. Your min values are higher than nominals. Please retry with a lower min.")
            print("\033[0;31;48mYour progress was not saved.")
            #stop the loop and get the user to try again.
            menu_stop = True
    #And anything else is a non option error
    else:
        print(NON_OPT_MSG)