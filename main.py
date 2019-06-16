from time import sleep
from random import randint
import PIL.Image
import PIL.ImageTk
from tkinter import *

def build_deck(numDecks):
    deck = []
    for val in range(2,15):
        for suit in ['spades','hearts','clubs','diamonds']:
            deck.append(Card(val,suit))
    return deck*numDecks


class Card(object):
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit
        
        if self.value > 10:
            l = ['jack','queen','king','ace']
            self.name = l[(self.value-11)]
        else:
            self.name = str(self.value)
           
        self.imgFile= './img/' + self.name + '_of_' + self.suit + '.png'
        
    def __str__(self):
        return self.name+' of '+self.suit
    
def eval_count(cc,crd):
    if crd.value <= 6:
        cc +=1
    elif crd.value >=10:
        cc -=1
    return cc

class ui(object):
    def __init__(self, parent):   
        #initiate GUI elements
        parent.title('Blackjack Card Counting Trainer')
        parent.iconbitmap(default='./img/blackjack.ico')
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()
        self.top_frame = Frame(self.frame)
        self.top_frame.pack(side=TOP)
        self.canvas = Canvas(self.top_frame, background="green", \
                             width=800, height=400 )
        self.canvas.pack()
        
        #initial display - card back shown and count hidden
        self.open_image()
        self.text_id = self.canvas.create_text((800,400),text='Peek to see the Count',fill='white',anchor='se',font=('Cambria',24))
        self.canvas.create_text((4,400),text='Created by Steve Gustus',fill='white',anchor='sw')
        
        #initaite buttons
        self.bottom_frame = Frame(self.frame)
        self.bottom_frame.pack(side=BOTTOM)
        self.dealButton = Button(self.bottom_frame, text="Deal", command=self.deal)
        self.dealButton.pack(side=LEFT)
        self.peekButton = Button(self.bottom_frame, text="Peek", command=self.peek)
        self.peekButton.pack(side=LEFT)
        self.hideButton = Button(self.bottom_frame, text="Hide", command=self.hide)
        self.hideButton.pack(side=LEFT)        
        self.restartButton = Button(self.bottom_frame, text="Restart", command=self.restart)
        self.restartButton.pack(side=LEFT)
        self.quitButton = Button(self.bottom_frame, text="Quit", command=self.quit)
        self.quitButton.pack(side=RIGHT)
        
        #initiate blackjack bits
        self.deck = build_deck(2)
        self.cardCount = 0
        
    def deal(self):  
        self.hide()
        for i in range(6):
            nextCard = self.deck.pop(randint(1,len(self.deck)-1))
            self.show_card(nextCard)
            self.cardCount = eval_count(self.cardCount,nextCard)
            sleep(1)

    def peek(self):
        s = 'Count: ' + str(self.cardCount)
        self.canvas.itemconfig(self.text_id, text=s)
    
    def hide(self):
        self.canvas.itemconfig(self.text_id, text='Peek to see the Count')
    
    def restart(self):
        self.deck = build_deck(2)
        self.cardCount = 0
        self.open_image()     
    
    def quit(self):
        self.parent.destroy()

    def show_card(self, cahd):
        self.open_image()
        sleep(0.25)
        self.open_image(cahd.imgFile)
        
    def open_image(self, fname='./img/card_back.png'):
        im = PIL.Image.open(fname)
        im = im.resize((150,210))
        self.canvas.img = PIL.ImageTk.PhotoImage(im)
        self.canvas.create_image(325,75,image=self.canvas.img,anchor='nw')
        self.canvas.update()        


if __name__ == "__main__":
    root = Tk()
    my_gui = ui(root)
    root.mainloop()

    

    
