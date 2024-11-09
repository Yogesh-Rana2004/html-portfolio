from tkinter import *
from PIL import Image,ImageTk
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
timer=None
current_card={}
flip_timer=None
to_learn={}

try:
    data=pd.read_csv('/Users/sameerrana/Desktop/Desktop/Mom/Project.py/day 31/flash-card-project-start/data/words_to_learn.csv')
except FileNotFoundError:
    original_data=pd.read_csv('/Users/sameerrana/Desktop/Desktop/Mom/Project.py/day 31/flash-card-project-start/data/french_words.csv')
    to_learn=original_data.to_dict(orient="records")
else:    
    to_learn=data.to_dict(orient="records") 


def new_card():
    global current_card ,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill='black')
    canvas.itemconfig(card_word,text=current_card["French"],fill='black')
    canvas.itemconfig(canvas_image, image=old_image)
    flip_timer=window.after(3000,flip_card)

 
    
#     word=new_data.keys(index=random.randint(1,13))
#     canvas.create_text(400,150,text=word,font=("ariel",40,'italic'))

def flip_card():
    canvas.itemconfig(card_title,text="English",fill='white')
    canvas.itemconfig(card_word,text=current_card["English"],fill='white') 
    canvas.itemconfig(canvas_image, image=new_image)

def is_known():
    to_learn.remove(current_card)
    new_data=pd.DataFrame(to_learn)
    new_data.to_csv("/Users/sameerrana/Desktop/Desktop/Mom/Project.py/day 31/flash-card-project-start/data/words_to_learn.csv",index=False)
    new_card()


window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,flip_card)


canvas=Canvas(width=800,height=526)
image_1=Image.open("/Users/sameerrana/Desktop/Desktop/Mom/Project.py/day 31/flash-card-project-start/images/card_front.png")
image_2=Image.open("/Users/sameerrana/Desktop/Desktop/Mom/Project.py/day 31/flash-card-project-start/images/card_back.png")
new_image = ImageTk.PhotoImage(image_2)
old_image = ImageTk.PhotoImage(image_1)
canvas_image=canvas.create_image(400,263,image=old_image)
card_title=canvas.create_text(400,150,text="",font=("ariel",40,'italic'))
card_word=canvas.create_text(400,250,text="",font=("ariel",60,'bold'))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)



cross_image=PhotoImage(file="/Users/sameerrana/Desktop/Desktop/Mom/Project.py/day 31/flash-card-project-start/images/wrong.png")
cross_button=Button(image=cross_image,highlightthickness=0,command=new_card)
cross_button.grid(row=1,column=0)
right_image=PhotoImage(file="/Users/sameerrana/Desktop/Desktop/Mom/Project.py/day 31/flash-card-project-start/images/right.png")
right_button=Button(image=right_image,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)

new_card()

window.mainloop()
 