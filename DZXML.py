# import xml_auto_editor as xml
import xml.etree.ElementTree as ET
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
# file_to_edit = PurePath("types.xml")
file_to_edit = Path(r"Projects\DZXML_Editor\types.xml") #Dev

#Primary tree and root to be edited.
tree = ET.parse(file_to_edit)
root = tree.getroot()

#Constant for functionality / feedback after performing actions
MSG = "\n\033[1;32;48m** Modified! **" #Will be Green


#-------- Nominal Modifiers ---------#

#Prompt for multiplying or adding to the nominal values.
def nominal_selection():
    """Selection menu for nominal editing."""
    multiply_or_add = int(input("\033[1;35;48m Multiply or Add off nominal?(0 = Multiply, 1 = Add):\n"))

    if multiply_or_add == 0:
        change_value = float(input("\033[0;36;48mHow much would you like to multiply each nominal value by? Use integers:\n"))
        #Check if you are trying to multiply too high..
        if change_value >= 6:
            print("\033[0;31;48m Integer is too large. Please try a smaller number.")
            #If you are, return back to the beginning.
            nominal_selection()
        #Parameter is the change_value variable we have above
        nominal_multiplication_modifier(change_value)
    elif multiply_or_add == 1:
        change_value = float(input("\033[0;36;48mHow much to add to the nominal? Use integers:\n")) #Converted to float
        #Parameter is the change_value variable we have above
        nominal_addition_modifier(change_value)


#Nominal modifiers
def nominal_multiplication_modifier(change_value):
    """Multiplication modifier for nominal values, takes parameter change_value as a user input value and loops through all
    parts in the root xml to change values."""
    for nominal in root.iter("nominal"):
        #Multiply whatever user input is in the input
        nominal.text = str(int(nominal.text) * change_value)
        #TODO Trying to work on getting this to work with decimals, so I could do 1.5x, but guess I could just use addition..?
        if nominal.text == float:
            nominal.text = round(nominal.text)
            nominal.text = (str(int(nominal.text)))
    print(MSG)


#Nominal modifiers
#Changing nominal values by adding user value to pre-existing value
def nominal_addition_modifier(change_value):
    """Addition modifier for nominal values, takes parameter change_value as a user input value and loops through all
    parts in the root xml to change values."""
    #For loop to loop through the <nominal></nominal> tag
    for nominal in root.iter("nominal"):
        #Add whatever integer the user puts in to the pre-existing value.
        nominal.text = str(int(nominal.text) + change_value)

    print(MSG)


#-------- Minimum Modifiers --------#

#function to modify min values
def minimum_selection():
    """Min selection menu for editing min values in xml."""
    multiply_or_add = int(input("\033[0;35;48mMultiply or Add Min? (0 = Multiply, 1 = Add):\n"))
    if multiply_or_add == 0:
        change_value = int(input("\033[0;36;48mHow much to multiply each min value by? Use integers:\n"))
        #minimum_multiplication_modifier(change_value)
        #Check if you're doing too much..
        if change_value >= 6:
            print("\033[0;31;48m Integer is too large. Please try a smaller number.")
            #If you are, try again.
            minimum_selection()
            #No idea how this got missed? It was here before! Edit: I see why now, I commented it out like a goon
        #If you're not trying to do too much..
        else:
            #Run the function
            minimum_multiplication_modifier(change_value)
    elif multiply_or_add == 1:
        change_value = int(input("\033[0;36;48mHow much to add to each min value? Use integers:\n"))
        minimum_addition_modifier(change_value)


#Modifier to add to mins
#If min value is 2 and you add 4 the new min will be 6.
def minimum_addition_modifier(change_value):
    """Addition modifier for min values, takes parameter change_value as a user input and loops through all
    parts in the root xml to change values."""
    #Loop through all min elements
    for min in root.iter("min"):
        #access values in min and add user input value
        min.text = str(int(min.text) + change_value)
    print(MSG)


#Modifier to multiply from min
#If min value is 2 and you multiply by 2 the new min will be 4.
def minimum_multiplication_modifier(change_value):
    """Multiplication modifier for min values, takes parameter change_value as a user input and loops through
    all parts in the root xml to change values."""
    #loop through all min elements
    for min in root.iter("min"):
        #access values in min and multiply by user input value
        #This here already converts the stuff to a string outside, but inside is still treated like a integer!
        min.text = str(int(min.text) * change_value)
    print(MSG)


#-------- Quantmin Modifier --------#
#Commentating my issues with this function:
#Python is always reading the xml as a string, so always convert our inputs or values to a str() first.
#TODO Add the ability to put 0 up to 100, nothing less or higher.
def quantmin_modifier():
    """Quantmin modifier, modifies from 0 to 100. Does not modify values set at -1."""
    print("\033[0;35;48mMust use integer and entire value, so if you want 80% type 80.")
    change_value = int(input("\033[0;36;48mWhat would you like to set the quantmin to?:\n"))
    for quantmin in root.iter("quantmin"):
        quantmin.text = str(int(quantmin.text))
        if quantmin.text != "-1": #The -1 in the xml is a int, but Python is reading as a string, so had to change this to "-1"
            #Set the value to whatever the user typed
            quantmin.text = str(change_value) #Had to add str in front to convert the user input look above for reason
            #If quantmin is already "-1", keep it at "-1"
        elif quantmin.text == "-1":
            quantmin.text = "-1"
    print(MSG)


#-------- Quantmax Modifier ---------#
def quantmax_modifier():
    """Quantmax modifier, modifies from 0 to 100. Does not modify values set at -1."""
    #Little bit of direction for users
    print("\033[0;35;48mMust use integer and entire value, so if you want 100% type 100.")
    #Get input
    change_value = int(input("\033[0;36;48mWhat would you like to set quantmax to?:\n"))
    #run loop
    for quantmax in root.iter("quantmax"):
        quantmax.text = str(int(quantmax.text))
        if quantmax.text != "-1":
            #Set the value to whatever the user typed
            quantmax.text = str(change_value)
        elif quantmax.text == "-1":
            quantmax.text = "-1"
        else:
            print("\033[0;31;48mError. Please re-try..") #Red
    print(MSG)



#Need to get this working.
#It is working, but needs some polishing.
def minimum_check():
    """Check the minimum value to the nominal value. If min is greater than nominal, 
    switch bool to True as it is a corrupted file. Otherwise default = False."""
    corrupted_file = False
    for min in root.iter("min"):
        min.text = str(int(min.text))
    for nom in root.iter("nominal"):
        nom.text = (str(int(nom.text)))
    if min.text > nom.text:
        corrupted_file = True
    else:
        corrupted_file = False
    return corrupted_file

#TODO List:
#  1 - Clean up user dialogue.
# 2 - Make a check work for min - nominal
# 3 - Maybe add a lifetime modifier
# 4 - Try to get an icon for the .exe so it doesn't look so sketch
# 5 - Maybe make the multiplier able to multiply only up to 5x including decimal points but rounds to a whole number for the types.xml
# 6 - Build as .exe and include a blank types.xml in a zip with the github code as well.
#7 - Write documentation including docstrings for the functions just in-case?

#TODO Due Date:
#Must complete the above todo list by Sunday 04/30/23.
 
menu_stop = False
#TODO Finish writing options menu for specific selections.
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
    user_selected = int(input(""))

    #Option 1 is modifying the nominal values
    if user_selected == 1:
        nominal_selection()
    #Option 2 is modifying the min values
    elif user_selected == 2:
        minimum_selection()
    elif user_selected == 3:
        quantmin_modifier()
    elif user_selected == 4:
        quantmax_modifier()
        #TODO Get the program to write file to same path as exe
    elif user_selected == 0:
        minimum_check()
        if minimum_check() == False:
            tree.write("types_modified.xml")
            menu_stop = True
            exit()
        elif minimum_check() == True:
            print("\033[0;31;48mError. Your min values are higher than nominals. Please retry with a lower min.")
            print("\033[0;31;48mYour progress was not saved.")
            menu_stop = True