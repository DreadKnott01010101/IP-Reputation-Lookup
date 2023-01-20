import easygui
# importing easygui module 
from easygui import *
  
# message to be displayed 
text = "IP Reputation Checker"
  
# window title 
title = "IP Lookup"
  
# default text 
d_text = "Enter Here"
  
# creating a enter box 
output = enterbox(text, title, d_text) 
  
# title for the message box 
title = "Message Box"
  
# creating a message 
message = "Analyzing " + str(output) 
  
# creating a message box 
msg = msgbox(message, title) 

#1 (1/18/23)To Oppen Chrome but it breaks the Script in Sublime Editor but not Terminal
#2 (1/19/23) As of this date this code no longer breaks this script
import webbrowser
webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("google.com")

import pyautogui
#Show Screen Dimensions
print(pyautogui.size())

#Go to Abuse IPD
pyautogui.click(80, 80, duration = 1)
pyautogui.click(84, 112, duration = .5)
pyautogui.click(750, 283, duration = 1)

#Autofill IP provided (output) and Enter
pyautogui.write(output)
pyautogui.press('enter')

#CODE For Mouse Location "pyautogui.mouseInfo()"

#CODE for VirusTotal and OUTPUT entered
pyautogui.click(269, 15, duration = .5)
pyautogui.click(80, 80, duration = .5)
pyautogui.click(85, 135, duration = .5)
pyautogui.click(230, 55, duration = .5)
pyautogui.write("https://www.virustotal.com/gui/ip-address/") 
pyautogui.write(output)
pyautogui.press('enter')

#Code for Talos search and OUTPUT entered
pyautogui.click(80, 80, duration = .5)
pyautogui.click(510, 15, duration = .5)
pyautogui.click(230, 55, duration = .5)
pyautogui.write("https://talosintelligence.com/reputation_center/lookup?search=") 
pyautogui.write(output)
pyautogui.press('enter')

