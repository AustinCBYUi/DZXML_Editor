
import tkinter as tk
from tkinter import IntVar
import DZXML as main

#Main root window.
rootwin = tk.Tk()
rootwin.title("DZXML Editor")
rootwin.minsize(width = 360, height = 400)
#A few constants for colors / fonts.
BACKGROUND = "#172033"
WHITE = "#ffffff"
BTN_CLOR = "#172E33"
RAD_CLR = "#00FF91"
RED = "#FF0000"
GREEN = "#00FF06"
TITLE_FONT = "Rockwell"
BUTTON_FONT = ""
LABEL_FONT = ""

#Make root background into background color
rootwin.config(bg=BACKGROUND)


#Menu frame
menu_frame = tk.Frame(rootwin)
menu_frame.config(bg=BACKGROUND)
#Place
menu_frame.grid(column=0, row=0, columnspan=4, rowspan=2)

#Item frame (Will be used for individual windows.)
#Parent is menu_frame
item_frame = tk.Frame(menu_frame)
item_frame.config(bg=BACKGROUND)
#Place, needed to move row down 1 more as it was conflicting with buttons.
item_frame.grid(column=0, row=3, columnspan=5, rowspan=9)


#Destroy old window / objects. Used for multiple windows.
def clear(object):
    slaves = object.grid_slaves()
    for x in slaves:
        x.destroy()


#Let's start here. Main reason for tool here.
def xml_editor_menu():
    clear(item_frame)
    #Main Label
    label = tk.Label(item_frame, fg=WHITE, bg=BACKGROUND, text="DZXML Editor")
    label.grid(column=1, row=2)

    #Change Nominal Label + Entry
    nominal_label = tk.Label(item_frame, fg=WHITE, bg=BACKGROUND, text="Nominal Value: ")
    nominal_label.grid(column=0, row=3)
    nominal_entry = tk.Entry(item_frame, fg=WHITE, bg=BTN_CLOR, width=10)
    # nominal_entry.insert()
    nominal_entry.grid(column=1, row=3)

    #------------ Nominal Radio Button -------------
    #Get what state it is by storing an IntVar supplied by tk.
    nominal_radio_state = IntVar()
    nominalradio1 = tk.Radiobutton(item_frame, fg=WHITE, bg=BACKGROUND, text="Add", value=1, variable=nominal_radio_state)
    nominalradio2 = tk.Radiobutton(item_frame, fg=WHITE, bg=BACKGROUND, text="Multiply", value=2, variable=nominal_radio_state)
    #Used config to modify the little circle colors.
    nominalradio1.config(activebackground=BACKGROUND, activeforeground=BACKGROUND, selectcolor=BACKGROUND)
    nominalradio1.grid(column=2, row=3)
    #Used config to modify little circle colors.
    nominalradio2.config(activebackground=BACKGROUND, activeforeground=BACKGROUND, selectcolor=BACKGROUND)
    nominalradio2.grid(column=3, row=3)

    #Minimum Value
    min_label = tk.Label(item_frame, fg=WHITE, bg=BACKGROUND, text="Minimum Value: ")
    min_label.grid(column=0, row=4)
    #min Entry
    min_entry = tk.Entry(item_frame, fg=WHITE, bg=BTN_CLOR, width=10)
    min_entry.grid(column=1, row=4)
    #Min Radio Buttons
    min_radio_state = IntVar()
    minradio1 = tk.Radiobutton(item_frame, fg=WHITE, bg=BACKGROUND, text="Add", value=1, variable=min_radio_state)
    minradio2 = tk.Radiobutton(item_frame, fg=WHITE, bg=BACKGROUND, text="Multiply", value=2, variable=min_radio_state)
    minradio1.config(activebackground=BACKGROUND, activeforeground=BACKGROUND, selectcolor=BACKGROUND)
    minradio2.config(activebackground=BACKGROUND, activeforeground=BACKGROUND, selectcolor=BACKGROUND)
    minradio1.grid(column=2, row=4)
    minradio2.grid(column=3, row=4)

    #Labels for quantmin / quantmax
    quantmin_label = tk.Label(item_frame, fg=WHITE, bg=BACKGROUND, text="Quantmin: ")
    quantmax_label = tk.Label(item_frame, fg=WHITE, bg=BACKGROUND, text="Quantmax: ")
    quantmin_label.grid(column=0, row=5)
    quantmax_label.grid(column=2, row=5)
    #Spinboxes for quantmin / quantmax
    quantmin_spinbox = tk.Spinbox(item_frame, from_=0, to=100, fg=WHITE, bg=BACKGROUND, width=10)
    quantmin_spinbox.grid(column=1, row=5)
    quantmax_spinbox = tk.Spinbox(item_frame, from_=0, to=100, fg=WHITE, bg=BACKGROUND, width=10)
    quantmax_spinbox.grid(column=3, row=5)


    #Encapsulated function grabs values from parent function dzxml_editor, converts some to integers
    def grab_values():
        nomi = int(nominal_entry.get())
        nom_add_mult = nominal_radio_state.get()
        mini = int(min_entry.get())
        min_add_mult = min_radio_state.get()
        qmin = int(quantmin_spinbox.get())
        qmax = int(quantmax_spinbox.get())
        #Pass all values to get_all_xml_values.
        get_all_xml_values(nomi, nom_add_mult, mini, min_add_mult, qmin, qmax)


    #Write file button
    write_file = tk.Button(item_frame, fg=WHITE, bg=BTN_CLOR, text="Write File", command=grab_values)
    write_file.grid(column=0, row=8)


def get_all_xml_values(nom, nom_add_or_mult, min, min_add_or_mult, quantmin, quantmax):
    nominal = nom
    if nom_add_or_mult == 1: #Add
        main.nominal_addition_modifier(nominal)
    else:
        main.nominal_multiplication_modifier(nominal)
    minimum = min
    if min_add_or_mult == 1: #Add
        main.minimum_addition_modifier(minimum)
    else:
        main.minimum_multiplication_modifier(minimum)
    main.quantmin_modifier(quantmin)
    main.quantmax_modifier(quantmax)
    main.write_file()
    if main.minimum_check() == False:
        success_label = tk.Label(item_frame, fg=GREEN, bg=BACKGROUND, text="Successfully wrote types_modified.xml to bin folder!")
        success_label.grid(column=1, row=8)
    else:
        failure_label = tk.Label(item_frame, fg=RED, bg=BACKGROUND, text="Something went wrong, please try again..")
        failure_label.grid(column=1, row=8)



def msg_editor_menu():
    clear(item_frame)
    tester = tk.Label(item_frame, fg=WHITE, bg=BACKGROUND, text="Testing this window")
    tester.grid(column=0, row=2)


#Main selection. Menu_frame frame is supposed to stick around after clear()
xml_editor = tk.Button(menu_frame, fg=WHITE, bg=BTN_CLOR, text="XML Editor", command=xml_editor_menu, height=1, width=20)
xml_editor.grid(column=0, row=0, sticky="N")
msg_editor = tk.Button(menu_frame, fg=WHITE, bg=BTN_CLOR, text="Message Editor", command=msg_editor_menu, height=1, width=20)
msg_editor.grid(column=1, row=0, sticky="N")


rootwin.mainloop()