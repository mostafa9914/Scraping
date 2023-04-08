# https://www.goodreads.com/quotes
import  requests
import bs4
import random
from tkinter import*
import tkinter.scrolledtext as sc
from tkinter import ttk


def Scraping():
    word = en1.get()
    while True:
          quote_type = word
          if quote_type == "science" or quote_type == "life"or quote_type == "love":
              html = requests.get("https://www.goodreads.com/quotes/tag/"+quote_type)
              break
          else:
              print("Plese choose one of the three options (science ,life , love)")


    html = html.text
    html_parser = bs4.BeautifulSoup(html, "html.parser")
    all_quotes = html_parser.findAll("div" , attrs={"class":"quoteText"})
    random_numbre = random.randint(1,30)
    text1.insert('end', '[-]The Word Is :' , 'black')
    text1.insert('end', word , 'white')
    text1.insert("end" , "\n")
    text1.insert('end',all_quotes[random_numbre].text)

root = Tk()
root.geometry('500x450')

text1 = sc.ScrolledText(root)
text1['font'] = ('Courier' , '8' ,'bold')
text1.place(x=1 , y=50 , width=500, height=250)
text1.tag_config('red' , background='white', foreground='red')
text1.tag_config('white' , background='black', foreground='white')
text1.tag_config('green' , background='white', foreground='green')




en1 = ttk.Entry(root , font=('Arial' , '12') , justify=CENTER)
en1.place(x=100 , y=320 ,width=300 , height=24)

b1 = ttk.Button(root, text='Get' , width=45 ,cursor='hand2'  , command= Scraping)
b1.place(x=110 , y=360)


root.mainloop()

