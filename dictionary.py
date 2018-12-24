#Dictionary GUI and functionality
import tkinter
import json
from pprint import pprint
with open('dictionary1.json') as f:
    words = json.load(f)
misspell={}

class App:
    # GUI for 
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.title(window_title)
        self.window.resizable(True, True)
        self.window.configure(background='honeydew4')
        self.result_frame = tkinter.Frame(window, bd=3, bg="honeydew2", relief=tkinter.RAISED)
        ans_lab=tkinter.Label(self.result_frame, bg="SlateGray2", text="Enter word to search in dictionary")
        ans_lab.pack(anchor=tkinter.CENTER, pady=(10,5))
        self.ans_box=tkinter.Text(self.result_frame, width=50, height=4, bg="SlateGray3")
        self.ans_box.pack(anchor=tkinter.CENTER, padx=(10,10), pady=(5,10))
        btn=tkinter.Button(self.result_frame, text="Search", width=30, bg="honeydew3" , command=lambda:self.search(self.ans_box.get("1.0","e-1c")))
        btn.pack(anchor=tkinter.CENTER, pady=(5,5))
        self.results_lab=tkinter.Label(self.result_frame, bg="honeydew2", text="Your results appear here")
        self.results_lab.pack(anchor=tkinter.CENTER, pady=(10,10), expand=True)
        self.results_box=tkinter.Text(self.result_frame, width=50, height=10, bg="honeydew3")
        self.results_box.pack(anchor=tkinter.CENTER, padx=(10,10), pady=(10,10))
        self.result_frame.pack(side=tkinter.RIGHT, anchor=tkinter.CENTER, padx=(10,20), pady=(10,10), expand=True)
        
        self.window.mainloop()
    
    # function to find near or siilar words
    def findword(self,word):
        try:
            if misspell[word]:
                return misspell[word]
        except:
            alphabet = "abcdefghijklmnopqrstuvwxyz"
           
            word = word.lower()
            res= [] 
            for i in word:
                res.append(i)
            word=res
            results = []

              #Adding any one character (from the alphabet) anywhere in the word.
            for j in alphabet:    
                for i in range(0,len(word)+1):
                    newWord=word[:]
                    newWord.insert(i,j)
                    newWord=''.join(newWord)
                    try:
                        if words[newWord]:
                            results.append(newWord)
                    except:
                        k=0
            #print(results)

              #Removing any one character from the word.
            if len(word) > 1:
                for i in range(0,len(word)):
                    newWord = word[:]
                    del newWord[i]
                    newWord=''.join(newWord)
                    try:
                        if words[newWord]:
                            results.append(newWord)
                    except:
                        k=0

            #Transposing (switching) the order of any two adjacent characters in a word.
            if len(word) > 1:
                for i in range(0,len(word)):
                    newWord = word[:]
                    r = newWord[i]
                    del newWord[i]
                    newWord.insert(i + 1,r)
                    newWord=''.join(newWord)
                    try:
                        if words[newWord]:
                            results.append(newWord)
                    except:
                        k=0

            #Substituting any character in the word with another character.
            for i in range(0,len(word)):
                for j in alphabet:
                    newWord = word[:]
                    newWord[i] = j
                    newWord=''.join(newWord)
                    try:
                        if words[newWord]:
                            results.append(newWord)
                    except:
                        k=0
            dict2={}
            for i in range(0,len(results)):
                dict2[results[i]]=0
            #print(dict2)
            word=''.join(word)
            misspell[word]=dict2
            return misspell[word]
    
    #function that deletes all suggested words when clicked on one of them
    def delsearch(self,word,newword,n):
        self.results_box.destroy()
        self.results_box=tkinter.Text(self.result_frame, width=50, height=10, bg="honeydew3")
        self.results_box.pack(anchor=tkinter.CENTER, padx=(10,10), pady=(10,10))
        self.results_lab.config(text="Your result is here")
        self.results_box.insert("1.0",words[newword])
        self.ans_box.delete("1.0","end-1c")
        self.ans_box.insert("1.0",newword)
        dict2=misspell[word]
        dict2[newword]= dict2[newword]+1
        #print(dict2)
    
    #function to find meaning in dictionary
    def search(self,word):
        self.results_box.delete("1.0","end-1c")
        word=word.lower()
        try:
            if words[word]:
                self.results_box.insert("1.0",words[word])
        except:
            self.results_lab.config(text="Did you mean")
            results = self.findword(word)
            if len(results)==0:
                self.results_box.delete("1.0","end-1c")
                self.results_box.insert("1.0","No related word found")
            else:
                newlist = list()
                for i in results.keys():
                    newlist.append(i)
                buttons = []
                for i in range(len(newlist)):
                    newbtn = "nb"+str(i)
                    newbtn = tkinter.Button(self.results_box, text=newlist[i] ,command=lambda i=i:self.delsearch(word,buttons[i]["text"],len(newlist)))
                    newbtn.pack(side="left", pady=(2,2))
                    buttons.append(newbtn)
                self.results_box.delete("1.0","end-1c")
                self.results_box.insert("1.0",newlist)
        
        
if __name__ == '__main__':
    App(tkinter.Tk(), "Dictionary Tool")