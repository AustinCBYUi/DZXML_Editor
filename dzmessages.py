import xml.etree.ElementTree as ET

#This is from a new friend on discord. Brilliant idea.
class colors:
    PINK = '\033[95m'
    MAGENTA = '\033[95m'
    CYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    GREY = '\033[90m'
    WHITE = '\033[97m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = "\033[0m"


#Main portion of the function
def main():
    print(colors.CYAN + "Message Creator 1.0")
    print(colors.CYAN + "Message repeated every X minutes(0 = no repeat):")
    repeat_msg = int(input(colors.GREEN + ""))
    if repeat_msg == 0:
        repeat = False
    elif repeat_msg >= 1:
        repeat = repeat_msg

    print(colors.CYAN + "On connection type message?(1=True, 0=False)")
    onconnect = int(input(colors.GREEN + ""))
    if onconnect == 1:
        onconnect = True
    elif onconnect == 0:
        onconnect = False
    else:
        print(colors.RED + "Cannot be greater than 1 or less than 0.")

    print(colors.CYAN + "Message delay on connection in X mins?:")
    delay = int(input(colors.GREEN + ""))
    if delay >= 1:
        delay = delay
    else:
        delay = False
    
    print(colors.CYAN + "Message deadline?(restart msgs typically):")
    deadline = int(input(colors.GREEN + ""))
    if deadline == 0:
        deadline = False
    else:
        deadline = deadline

    print(colors.CYAN + "Message shutdown?(1=True, 0=False)")
    shutdown = int(input(colors.GREEN + ""))
    if shutdown == 1:
        shutdown = True
    else:
        shutdown = False

    print(colors.CYAN + "Text for message below: ")
    text = input(colors.GREEN + "")
    
    MessageCreator(repeat, delay, onconnect, deadline, shutdown, text)


#I don't know if this is absolutely required, but we created our values above, this function is about
#creating the stuff for the message using your values from above.
def MessageCreator(repeat, delay, onconnect, deadline, shutdown, text):
    """Creates the messages for the XML using specific XML tags and placing the user inputs
    into the tags."""
    if repeat == False:
        repeat_line = False
    elif repeat >= 1:
        repeat_line = f"<repeat>{repeat}</repeat>"
    
    if delay == False:
        delay_line = False
    elif delay >= 1:
        delay_line = f"<delay>{delay}</delay>"

    if onconnect == True:
        onconnect_line = f"<onconnect>{1}</onconnect>"
    elif onconnect == False:
        onconnect_line = False

    if deadline == False:
        deadline_line = False
    elif deadline >= 1:
        deadline_line = f"<deadline>{deadline}</deadline>"

    if shutdown == False:
        shutdown_line = False
    elif shutdown == True:
        shutdown_line = f"<shutdown>{1}</shutdown>"

    text_line = f"<text>{text}</text>"

    #Call the function
    WriteXML(repeat_line, delay_line, onconnect_line, deadline_line, shutdown_line, text_line)


#Writes the XML Using the parameters to put into the xml.
def WriteXML(repeat, delay, onconnect, deadline, shutdown, text):
    #create the messages.xml file as write
    file = open("messages.xml", "w")
    #First line in XML
    file.write("""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n""")
    #Start of <messages>
    file.write("<messages>\n")
    #LEGIT Tab for YOUR message
    file.write("    <message>\n")
    #Specific way this works, if you don't have a repeat value it SHOULD be False, if it is it will pass
    if repeat == False:
        pass
    #If it passes it will pass the statement completely, if it isn't False it will trigger the else: statement to write the line.
    else:
        #the variable repeat is already set up in the format at this point as <repeat>X</repeat>
        file.write(f"       {repeat}\n")
    #Same thing as above for the rest of the program.
    if delay == False:
        pass
    else:
        file.write(f"       {delay}\n")
    if onconnect == True:
        file.write(f"       {onconnect}\n")
    else:
        pass
    if deadline == False:
        pass
    else:
        file.write(f"       {deadline}\n")
    if shutdown == True:
        file.write(f"       {shutdown}\n")
    else:
        pass
    file.write(f"       {text}\n")
    file.write("    </message>\n")
    file.write("</messages>")
