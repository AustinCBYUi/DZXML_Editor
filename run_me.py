import xml_auto_editor as xml

#Author - Austin Campbell || Released on my school github acc.
#Purpose - Automate types.xml editing without screwing up loot tables / exponential nominal / min values.
# ^^ I know too high nominals / mins can mess with spawns on console, which is why I made this.
#Designed for console use.
#Please read additional documentation on the readme.md, thanks! I hope it works well for you, and you can
#send suggestions to contacts below. feel free to edit as desired. Please message me if you are re-releasing it.
#
#Email - infrared.dayz@gmail.com
#Discord - Danny2#5070

menu_stop = False

#TODO Finish writing options menu for specific selections.
while menu_stop == False:
    #Used a variable instead of a print statement to help cleanliness
    options_menu = """
    1) Modify Nominal Values
    2) Modify Minimum Values
    3) Modify Quantity Minimum Values
    4) Modify Quantity Maximum Values
    0) Exit and write to new file
    """
    #Print out the options menu now
    print(options_menu)
    #Now get the input from the user on which option to utilize
    user_selected = int(input(""))

    #Option 1 is modifying the nominal values
    if user_selected == 1:
        xml.nominal_selection()
    #Option 2 is modifying the min values
    elif user_selected == 2:
        xml.minimum_selection()
    elif user_selected == 3:
        xml.quantmin_modifier()
    elif user_selected == 0:
        xml.tree.write("types_modified.xml")
        exit()