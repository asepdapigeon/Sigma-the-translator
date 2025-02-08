from tkinter import *


from tkinter import messagebox


root = Tk()


variable1 = StringVar(root) 
variable2 = StringVar(root) 


variable1.set("Choose Language") 
variable2.set("Choose Language") 

''' 
VARIABLE KEY 
'cipher' -> 'stores the morse translated form of the english string' 
'decipher' -> 'stores the english translated form of the morse string' 
'citext' -> 'stores morse code of a single character' 
'i' -> 'keeps count of the spaces between morse characters' 
'message' -> 'stores the string to be encoded or decoded' 
'''


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
					'C':'-.-.', 'D':'-..', 'E':'.', 
					'F':'..-.', 'G':'--.', 'H':'....', 
					'I':'..', 'J':'.---', 'K':'-.-', 
					'L':'.-..', 'M':'--', 'N':'-.', 
					'O':'---', 'P':'.--.', 'Q':'--.-', 
					'R':'.-.', 'S':'...', 'T':'-', 
					'U':'..-', 'V':'...-', 'W':'.--', 
					'X':'-..-', 'Y':'-.--', 'Z':'--..', 
					'1':'.----', '2':'..---', '3':'...--', 
					'4':'....-', '5':'.....', '6':'-....', 
					'7':'--...', '8':'---..', '9':'----.', 
					'0':'-----', ', ':'--..--', '.':'.-.-.-', 
					'?':'..--..', '/':'-..-.', '-':'-....-', 
					'(':'-.--.', ')':'-.--.-'} 


def clearAll() :
	
	language1_field.delete(1.0, END)
	language2_field.delete(1.0, END)


<<<<<<< Tabnine <<<<<<<
def convert() :
    """#+
    This function converts the input message from the selected language to the target language.#+

    Parameters:#+
    None#+

	message = language1_field.get("1.0", "end")[:-1]#-
    Returns:#+
    None#+

    The function first retrieves the input message from the language1_field. It then checks if the selected languages for translation are the same. If they are, it displays an error message and returns. If the selected languages are different, it checks if the selected languages are English and Morse code. If they are, it encrypts the input message using the encrypt function and assigns the result to the variable 'rslt'. If the selected languages are Morse code and English, it decrypts the input message using the decrypt function and assigns the result to the variable 'rslt'. If the selected languages are neither English and Morse code, it displays an error message and returns. Finally, it inserts the result into the language2_field.#+
    """#+
    message = language1_field.get("1.0", "end")[:-1]#+

	if variable1.get() == variable2.get() :#-
    if variable1.get() == variable2.get() :#+
        messagebox.showerror("Can't Be the same Language")#+
        return#+

    elif variable1.get() == "Eng" and variable2.get() == "Morse" :#+
        rslt = encrypt(message)#+

		messagebox.showerror("Can't Be the same Language")#-
		return#-
    elif variable1.get() == "Morse" and variable2.get() == "Eng" :#+
        rslt = decrypt(message)#+

	elif variable1.get() == "Eng" and variable2.get() == "Morse" :#-
    else :#+
        messagebox.showerror("please choose valid language code..")#+
        return#+

#-
		rslt = encrypt(message)#-
#-
	elif variable1.get() == "Morse" and variable2.get() == "Eng" :#-
#-
#-
		rslt = decrypt(message)#-
#-
	else :#-
#-
#-
		messagebox.showerror("please choose valid language code..")#-
		return#-
#-
#-
	language2_field.insert('end -1 chars', rslt)#-
    language2_field.insert('end -1 chars', rslt)#+
>>>>>>> Tabnine >>>>>>># {"conversationId":"fcea9b71-a236-48f5-88fc-482eb79aa77a","source":"instruct"}
	
		

def encrypt(message):
	cipher = '' 
	for letter in message: 
		if letter != ' ':

			
			cipher += MORSE_CODE_DICT[letter] + ' '
		else: 
			
			cipher += ' '

	return cipher 


def decrypt(message): 


	message += ' '

	decipher = '' 
	citext = '' 
	for letter in message: 


		if (letter != ' '): 


			i = 0


			citext += letter 


		else: 

			i += 1


			if i == 2 : 


				decipher += ' '
			else: 


				decipher += list(MORSE_CODE_DICT.keys())[
							list(MORSE_CODE_DICT .values()).index(citext)] 
				citext = '' 

	return decipher 


if __name__ == "__main__" : 
	

	root.configure(background = '#0f0616') 
	

	root.geometry("400x350") 

	root.title("Sigma: The Morse Code Translator")

	headlabel = Label(root, text = 'Translator menu | The Text Needs To Be Capitalized!', 
							fg = 'black', bg = "pink") 


	label1 = Label(root, text = "Default language ", 
				fg = 'white', bg = '#301934') 
	

	label2 = Label(root, text = "From", 
				fg = 'white', bg = '#301934') 
	

	label3 = Label(root, text = "To", 
				fg = 'white', bg = '#301934') 


	label4 = Label(root, text = "Result", 
				fg = 'white', bg = '#301934') 
	
    

	headlabel.grid(row = 0, column = 1) 
	label1.grid(row = 1, column = 0) 
	label2.grid(row = 2, column = 0) 
	label3.grid(row = 3, column = 0) 
	label4.grid(row = 5, column = 0) 
	

	language1_field = Text(root, height = 5, width = 25, 
									font = "lucida 13") 
	language2_field = Text(root, height = 5, width = 25, 
									font = "lucida 13")
		

	language1_field.grid(row = 1, column = 1, padx = 10) 
	language2_field.grid(row = 5, column = 1, padx = 10) 


	languageCode_list = ["Eng", "Morse"] 


	FromLanguage_option = OptionMenu(root, variable1, *languageCode_list) 
	ToLanguage_option = OptionMenu(root, variable2, *languageCode_list) 
	
	FromLanguage_option.grid(row = 2, column = 1, ipadx = 10) 
	ToLanguage_option.grid(row = 3, column = 1, ipadx = 10) 
	
	
	button1 = Button(root, text = "Convert", bg = "pink", fg = "black", 
								command = convert) 
	
	button1.grid(row = 4, column = 1) 

	
	button2 = Button(root, text = "Clear", bg = "pink", 
					fg = "black", command = clearAll)
	
	button2.grid(row = 6, column = 1) 
	
	
	root.mainloop() 
