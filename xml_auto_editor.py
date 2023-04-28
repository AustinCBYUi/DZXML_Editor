import xml.etree.ElementTree as ET

#Author - Austin Campbell || Released on my school github acc.
#Purpose - Automate types.xml editing without screwing up loot tables / exponential nominal / min values.
# ^^ I know too high nominals / mins can mess with spawns on console, which is why I made this.
#Designed for console use.
#Please read additional documentation on the readme.md, thanks! I hope it works well for you, and you can
#send suggestions to contacts below. feel free to edit as desired. Please message me if you are re-releasing it.
#
#Email - infrared.dayz@gmail.com
#Discord - Danny2#5070


file_to_edit = r"DZXML_Editor\types.xml"

#Primary tree and root to be edited.
tree = ET.parse(file_to_edit)
root = tree.getroot()

#Constant for functionality / feedback after performing actions
MSG = "Modified!"


#-------- Nominal Modifiers ---------#

#Prompt for multiplying or adding to the nominal values.
def nominal_selection():
    multiply_or_add = int(input("Multiply or Add nominal?(0 - Multiply, 1 - Add): "))

    if multiply_or_add == 0:
        change_value = int(input("How much would you like to multiply each nominal value by? Use integers: "))
        #Parameter is the change_value variable we have above
        nominal_multiplication_modifier(change_value)
    elif multiply_or_add == 1:
        change_value = int(input("How much to add to the nominal? Use integers: "))
        #Parameter is the change_value variable we have above
        nominal_addition_modifier(change_value)


#Nominal modifiers
def nominal_multiplication_modifier(change_value):
    for nominal in root.iter("nominal"):
        #Multiply whatever user input is in the input
        nominal.text = str(int(nominal.text) * change_value)
    print(MSG)


#Nominal modifiers
#Changing nominal values by adding user value to pre-existing value
def nominal_addition_modifier(change_value):
    #For loop to loop through the <nominal></nominal> tag
    for nominal in root.iter("nominal"):
        #Add whatever integer the user puts in to the pre-existing value.
        nominal.text = str(int(nominal.text) + change_value)
    print(MSG)


#-------- Minimum Modifiers --------#

#function to modify min values
def minimum_selection():
    multiply_or_add = int(input("Multiply or Add Min?(0 - Multiply, 1 - Add): "))
    if multiply_or_add == 0:
        change_value = int(input("How much to multiply each min value by? Use integers:"))
        #minimum_multiplication_modifier(change_value)
    elif multiply_or_add == 1:
        change_value = int(input("How much to add to each min value? Use integers: "))
        minimum_addition_modifier(change_value)


#Modifier to add to mins
#If min value is 2 and you add 4 the new min will be 6.
def minimum_addition_modifier(change_value):
    #Loop through all min elements
    for min in root.iter("min"):
        #access values in min and add user input value
        min.text = str(int(min.text) + change_value)
    print(MSG)


#Modifier to multiply from min
#If min value is 2 and you multiply by 2 the new min will be 4.
def minimum_multiplication_modifier(change_value):
    #loop through all min elements
    for min in root.iter("min"):
        #access values in min and multiply by user input value
        #This here already converts the stuff to a string outside, but inside is still treated like a integer!
        min.text = str(int(min.text) * change_value)
    print(MSG)


#-------- Quantmin Modifier --------#
#Commentating my issues with this function:
#Python is always reading the xml as a string, so always convert our inputs or values to a str() first.
def quantmin_modifier():
    print("Must use integer and entire value, so if you want 80% type 80.")
    change_value = int(input("What would you like to set the quantmin to?: "))
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
    #Little bit of direction for users
    print("Must use integer and entire value, so if you want 100% type 100.")
    #Get input
    change_value = int(input("What would you like to set quantmax to?: "))
    #run loop
    for quantmax in root.iter("quantmax"):
        quantmax.text = str(int(quantmax.text))
        if quantmax.text != "-1":
            #Set the value to whatever the user typed
            quantmax.text = str(change_value)
        elif quantmax.text == "-1":
            quantmax.text = "-1"
    print(MSG)



#Need to get this working.
# def minimum_check():
#     minimum_text = str(int(minimum.text))
#     maximum_text = str(int(maximum.text))
#     nominal_root = root.iter("nominal") #Grabs current nominal root
#     nominal_value = str(int(nominal_value.text)) #Current value
#     minimum_root = root.iter("min") #Grabs current min value
#     minimum_value = str(int(minimum_value.text))
#     for min in root.iter("min"):
#         if minimum_value > nominal_value:

#     print(nominal_value)