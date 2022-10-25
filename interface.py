from tkinter import *
from tkinter import messagebox
from config import csv_path
import pandas as pd 
from sentence_sim import preprocess,Jaccard_Similarity,answer_score

data = pd.read_csv(csv_path)


class Question:
    
    question_count = 0

    def __init__(self):
        self.newWindow = Tk()
        self.newWindow.title("Descriptive Answer Evaluator")
        self.newWindow.geometry("800x800")
        self.newWindow.configure(bg='#ccffff')
    
        # A Label widget to show in toplevel
        self.head = Label(self.newWindow, text="Question", font=("Arial Bold", 25),
            fg='blue').place(x=350, y=180) 
        
        self.question_field = Label(self.newWindow, text=data.Question[0], font=(
            "Arial", 18), fg='red', bg='#ccffff')
        
        self.question_field.place(x=130, y=250)
        
        self.answer_field = Text(self.newWindow, wrap=WORD, font=('Ariel', 18))
        self.answer_field.place(x=130, y=300, width=400, height=150)
        
        #next and submit buttons
        self.next_button = Button(self.newWindow, text="Next", font=("Arial Bold", 18), command = self.next)
        self.next_button.place(x=130, y=470, width=80, height=35)
        
        self.submit_button = Button(self.newWindow, text="Submit", font=(
            "Arial Bold", 18), command=self.submit)
        self.submit_button.place(x=450, y=470, width=80, height=35)
        
        self.score_label = Label(self.newWindow, text="Score: ", font=(
            "Arial Bold", 18), fg='Blue', bg='#ccffff').place(x=130, y=520)
        
        self.score_entry = Label(self.newWindow,font=("Arial Bold", 18), fg='Blue',bg = '#ccffff',
                                 text='0')
        self.score_entry.place(x=200, y=520)
                                 
    def next(self):
        
        Question.question_count += 1
        self.answer_field.delete("1.0", "end")
        self.question_field.config(text=data.Question[Question.question_count])
        self.score_entry.config(text='0')
        
        if Question.question_count >= len(data.Question) -1 :
            messagebox.showinfo("System", "Test questions ended")
    
    def submit(self):
        
        doc1 = preprocess(self.answer_field.get(1.0, "end-1c"))
        doc2 = preprocess(data.Model_Answer[Question.question_count])
        
        jaccard_score = Jaccard_Similarity(doc1, doc2)
        ans_score = answer_score(jaccard_score)
        self.score_entry.config(text=str(ans_score))
        

def open_new_window():
    Question()
    window.destroy()

window=Tk()

window.title('Descriptive Answer Evaluator')
window.geometry("800x800")
window.configure(bg='#ccffff')

lbl = Label(window, text="Descriptive Answer Evaluator",
            font=("Arial Bold", 20), fg='blue', bg='#ccffff')
lbl.place(x=260, y=260)

lbl = Label(window, text="An interface that evaluates the quality of a descriptive answer",
            font=("Arial Bold", 16), fg='black', bg='#ccffff')
lbl.place(x=165, y=290)

btn=Button(window, text="Proceed", fg='blue', command = open_new_window)
btn.place(x=370, y=370, width=80, height=35)

window.mainloop()
