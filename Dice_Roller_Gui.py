#importing the libraries
import tkinter
from PIL import Image, ImageTk
import random

#Creating application window for dice simulator using tkinter widgets
root = tkinter.Tk()

#getting screen width and height of display
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (width, height))

root.title('Please roll the dice')
root.configure(bg='#B9C6C9')

#Adding lables to the frames
l1 = tkinter.Label(root, text='')
l1.pack()

l2 = tkinter.Label(root, text='Welcome to the Dice Roll Simulator!', fg='black', bg='#B9C6C9', font='Times 16 bold italic')
l2.pack()

#Dice images
dice = ['Dice1.png', 'Dice2.png', 'Dice3.png', 'Dice4.png', 'Dice5.png', 'Dice6.png']

#Assigning a default image and constructing a label widget for the image
img= Image.open('Dice.png')
resize_img = img.resize((300, 300))
width, height = resize_img.size
print(width)
print(height)
image_def = ImageTk.PhotoImage(resize_img)
label1 = tkinter.Label(root, image=image_def)
label1.image = image_def
label1.pack(side=tkinter.LEFT, expand = True)

label2 = tkinter.Label(root, image=image_def)
label2.image = image_def
label2.pack(side = tkinter.LEFT, expand = True)

#function to create random dice logic and being activated by a button
def roll_dice():
    image_roll = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    #updating existing image with the random one
    label1.configure(image = image_roll, bg='#B9C6C9')
    #Referring this image
    label1.image = image_roll

    image_roll1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # updating existing image with the random one
    label2.configure(image=image_roll1, bg='#B9C6C9')
    # Referring this image
    label2.image = image_roll1

#Adding button to trigger roll_dice function
button = tkinter.Button(root, text='Click to roll the dice', font=('Helvetica,12,bold'),
                        width=20, height=2, bg='#FE3939', fg='white', command=roll_dice)

button.pack(side=tkinter.LEFT, padx=325, pady=375, expand=True)
root.mainloop()