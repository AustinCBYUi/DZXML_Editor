# DZXML_Editor ![Editor Status](https://img.shields.io/badge/Editor-Passing-brightgreen) ![Software Status](https://img.shields.io/badge/Software-WIP-yellow)

DZ types.xml editor. This program is now a UI based software.

**Please read further for directions / clarification before usage.**

Contact Info:
Email - *infrared.dayz@gmail.com*
Discord - *Danny2#5070*

---

### Introduction
DZXML Editor is an open-source Python developed simple types.xml modifier for DayZ server owners. I developed this
application so I didn't have to individually go through each nominal and min value on an xml ever again. Additionally
I don't like dealing with corrupted files from the web based editor. Aside from that it is just a project for fun for me to advance my skills and hopefully aid me in getting a software job in the future. That is the reason the program is so heavily commented as well, I try to keep as many comments in as possible so the process can be understood, and for my future self if I ever need to re-read.

I will do my absolute best to keep the types.xml files updated, but I think after 1.20 update you will have to use your own types.xml file as I don't plan to update them forever. Thank you in advance and I hope the tool serves you well! If there is any problems at all please let me know!

---

### Documentation

The easiest way to use this tool is to run the .exe file that comes in the package. Make sure you have a types.xml file
in the same directory as the .exe or it will not run the program. The application is written in Python and compiled to the
executable for Windows using auto-py-to-exe. If your computer is any other operating system or you are skeptic you will have to:

**Updated**
1. Download the most recent python at https://www.python.org/downloads/
2. Make sure there is a types.xml file in the directory in the same place as the ui.py. (Should be if you just downloaded it.)
3. With the src folder open, right click in the open window and select "Open in Terminal".
![alt text](https://github.com/AustinCBYUi/DZXML_editor/blob/main/src/bin/piccer1.png?raw=true)
5. Type "python ui.py". This will run the program with console in the background.
6. Use the UI to modify your values. Once you submit, it will dump your new file to the 'bin' folder

**The types files included are in separate folders named Livona and Chernarus. Please drag whichever one you are using DIRECTLY to your directory containing the .exe or .py file.**

----------

*I will use the acog scope as a reference here for quite a bit*

***Addition Nominal and Minimum***

This tool is designed to modify values to precision. So if you choose to add to nominal values, it will simply take the original
value, so the Acog being 9 for instance, and if you decided to add 5 to each nominal it would simply add 9+5=14. Now your acog
nominal is 14..

***Multiplication Nominal and Minimum***

The same goes with multiplication: If your input is to multiply by 4, the acog is default at 9: the program will do 9*4=36. Now
your acog nominal is 36.
Whatever number you choose for the Nominal **MUST** be higher or equal to the minimum number. I recommend if you add or multiply
by a certain number that you do -1 or -2 off the min. So if you once again multiplied the file nominal by 4, I would multiply the
min value by 2. *IF* you add or multiply your values I would go through regardless and check all values to make sure everything looks good and logical. Additionally if you try to multiply over 6, you will be unable to. I set the cutoff to greater or equal to 6 to not work.
You can read the promptings but when you go through the menu options, you will notice `Multiply or Add Min? (0 = Multiply, 1 = Add)` The parenthesis is telling you type 0 to multiply or type 1 to add - afterward it will ask for your value to either add or multiply based off what you chose and it will edit the file that way.

***Quantmin and Quantmax***

Modifying quantmin / quantmax is easier. The syntax when you type your input is just 0-100 which is in percent. A good example for quantmin and quantmax is ammo stacks or rice: If you want either of those to spawn 10% full at a minimum and only 80% full at a maximum, you would do exactly that: 10 for min and 80 for max. **NOTE** Any value that is set to -1 for quantmin and quantmax as a default is not affected by your input. It will always be -1 unless you manually changed it. Anything that is set to -1 is typically objects that don't have quantity like the acog. Also another **NOTE:** if you are modifying this, make sure your quantmin is less than or equal to the quantmax. Wouldn't make sense to have a quantmin of 80% and a quantmax of 60%.


The reason as to why I built the .exe and included the source code is for:
- Open-source software can be edited by others.
- To show the source code.
- .exe doesn't require Python to be installed as it is interpretted.
If you are interesting in editing the program, please read at the very bottom for dev documentation.

---

### Words of Advice
I assume if you're using this tool you are a veteran to server running, if you are not that is fine too. This message is
directed to all categories. I advise if you're going to multiply your nominal or minimum values that you don't go over 5x.
If you do, I **HIGHLY** recommend going through common items and reducing the nominal / min count. Xbox and Playstation both
limit to around 1000 total items spawning on the map, if you modify your items too much, you will lose out on a LOT of loot.

---

### TODOs for 2.0
- Add dzmessages.py to app.
- Work on continuing developer suite tools.
- Re-write DZXML.py as a class, and remove the 'selection' functions.
- Work on better user-feedback from UI.
- Move Success / Failure task label down below button so it doesn't expand window.

---

### Changelogs
This section will be updated with changes after initial release if necessary. This will primarily be used for major bugs fixed if any exist, or any requests are made to add. If I decide to make any other .xml modifiers for DayZ I will merge all projects into one super application that will allow you to modify different xmls.
Current version = v2.0! (1.0=public release and up to my standards)
- Refactored all files. 'src' is now the main source, with children named bin and types.
- Bin is the dump for both messages.xml and types.xml (namely types_modified.xml).
- Modified the pathing inside DZXML.py (main), this should work with console to run the application, and in IDEs.
- Built a small graphical user interface for the application. Consoles aren't fun.
- Removed most print statements / input statements from DZXML.py as we no longer utilize the console.

---

### Developer Documentation
If you are planning on taking the source code to develop on your own, please read this.
