import tkinter as tk
from PIL import Image, ImageTk
from functools import partial
import subprocess
import json
import sys

icon    = 'R0lGODlhfACAAPMKACIiIlVVVYiIiN0AAAC7AERERHd3dwAAAMzM/8zMzP///wAAAAAAAAAAAAAAAAAAACH5BAEAAAoALAAAAAB8AIAAAAT+UMlJqzo46827/2AojodlnqhErmzrimkcv3Rtg3Ju3nxP6zpNYkgsGo/IpHLJbDoTGiBK+Kxar1hmVLrLZL/g8HLLrVDF6DSWXJ6c1fB4kt2+eOX4PDRTp7z1gGJ0bX+Bhmt8fSp3SwWOj5CRkpOUlZaXjk2DZYVHmJ+goaCaiYqdRqKpqqmkGIqLGE2rs7SUrSWvp5AIvL2+v8DBwsPExbwGyAZzpX26j8bQ0dLRycpIm1zOjtPc3dzVy665jKjP3ufoweDXzHXaBenx8etH2FLv8vne9Eb2QPj6AlJLFg6XKXJFdglcSIxfEX9BEBJRyLDiL4dEIOYAaLEjAoz+QzTK4OixIsg94g7GQkKxJMOTImdIHNLSmAabGXBimAazHaGZCWoWuzk0Z9Gd0nqmbAZUKDGiT41GRToQWcFXdlZ6MhcN6jCvwsAWU2qQqdZy26SJBbb2V1thZLGS1HmArt2kBNktddeUK7S3vQDzEnwxbz2fnPqm7Sr1a+Owj8ca7oc4m2J4FQmfizvubEK/AjXvm/yw8r3LFkV346zyQBKn+VR/I53R9D/UmSPrY23WNUvQAWXzpB3SdkTPE4HrE47Xqt6yfJHTVB5bdz7e0X1vXVydg0XsP6UHpX7Ow3fiKKGH144W8/IO550f3rv+NXlv5k2ij5lirsuA4CX+Jh5s/82zn3Eb4VagQAFaNuB9C44mH2X0CcjeZ9xNIxtzwDR42oMZqmUdZFSh4+FtILrHzYYjNmfNfOpZaF+IjJV4VzonHndhcjSuuAKDB1bo4I7T9ajhjwAGGeOQM6pYHpK7KSmXguiwAOSEpQn5IZHjGRmhhC9SuOSWTX6ZJJa1aYkilwSaORuaxampY5luypNjginWaaeUnbEJoZ7G3DkSlYCuxmdrdBYK5lV9NlHNo5BGKumklFYq6S1TileEpZx26mmnmDbKxKeklkpqqIiOauqqrEaKam+HxJoFf1MAJeutz2XKJa68pjnmmr0Gm6uowhabnq7GGkvrCaf+JBvrsl1o6qwh0FrQ7LSBVGuGrdgCoq0f3Habx7duhCuuHOTCsuu5eKSb1brsxuHutfHCMa+59aJxr3gE9Otvv3r4wMGr2SXx778BC0zvscQacbC/CSssbZy/zonEwwCPK/HEDKd6xAAghwyyHq1SSnB9SIgsMsklX6oFgoOKp3LILLcM6ckypjzzADXbfFKWFeMJb776wiwTx0SHse/QSYOxdNMRBx0z01AjIqfQVbdrdH/4Zm3F017bu3WtSIf9BNhmF3311GmngXbbTo899cZ0C4wVs3Xn7cPd0ert9w98b/v34C0ELvgBASSu+OKMN674LABELvnklFdu+eWsHhgOLgaOd+455JeHLjrmHWheLueep7446KO3Pnrmpr+r+uwBsO767ZXDbroGPkPauSi4h6675rz3Xs3voQRPOgexv2v88Y4Dr3zupcde/PMGIA/K9NQzb30GAoQv/vjkl2/++JZq/0nrwxuuwfnwx09++tEn/3r1u4Mv//7n09+49KJrX+Dex78Coq9S6sME+/BHPMI5kATNe6AEQxDBCVrQe/m7oAalNoEIAAA7'
font    = 'Arial 16'
welcome = 'Choose an Operating System to begin.'

window = tk.Tk()
window.attributes('-fullscreen', True)

data  = None
icons = {}
funct = {}
try:
	with open("./config.json") as json_file:
		data = json.load(json_file)
except FileNotFoundError:
	msg = 'No configuration file found. A config.json file is required.'
	print(msg)
	sys.exit(1)

def shutdown_sys():
	subprocess.Popen(['sudo', 'shutdown', '-r', 'now'])
	exit()

def quit_app():
	exit()

def load_app(command, cwd=None):
	try:
		op_path = None if not cwd else cwd

		print("Executing '"+ command + ("." if op_path == None else "' (in directory '" + op_path + "').") )
		process = subprocess.Popen(command.split(), cwd=op_path)
	except IndexError:
		#sg.Popup('No command specified.', title='No runner specified', keep_on_top=True)
		print("Failed, no command found.")
	except FileNotFoundError:
		#sg.Popup('Couldn\'t find the requested application.', title='No application', keep_on_top=True)
		print("Failed, no application found.")

imgLogo = tk.PhotoImage(data=icon)
frmLogo = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frmLogo.grid(row=0, column=0, columnspan=2)
lblLogo = tk.Label(master=frmLogo, image=imgLogo)
lblLogo.pack()

frmWelcome = tk.Frame(master=window)
frmWelcome.grid(row=1, column=0, columnspan=2)
lblWelcome = tk.Label(master=frmWelcome, text=welcome, font=font)
lblWelcome.pack()

for i, entry in enumerate(data['options']):
	icons[i] = ImageTk.PhotoImage(file=entry['logo'])

	frmItem = tk.Frame(master=window)
	frmItem.grid(row=2, column=i)
	btnItem = tk.Button(master=frmItem, image=icons[i], command=partial( load_app, entry['command'], entry['cwd'] ))
	btnItem.pack()

frmClose = tk.Frame(master=window)
frmClose.grid(row=3, column=0)
btnClose = tk.Button(master=frmClose, text='Close', command=quit_app, font=font)
btnClose.pack()
frmShutdown = tk.Frame(master=window)
frmShutdown.grid(row=3, column=1)
btnShutdown = tk.Button(master=frmShutdown, text='Shutdown', command=shutdown_sys, font=font)
btnShutdown.pack()

window.mainloop()
