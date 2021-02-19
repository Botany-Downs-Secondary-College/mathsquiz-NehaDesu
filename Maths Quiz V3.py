from tkinter import*
from random import*

class MathQuiz:
    def __init__(self,parent):
        
        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)
        
        #Welcome Label
        self.TitleLabel = Label(self.Welcome, text = "Welcome to Maths Quiz",
                                bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                                font = ("Time", "14", "bold"))
        self.TitleLabel.grid(columnspan = 2)
        
        #Name & Age Label
        self.NameLabel = Label(self.Welcome, text = "Name",
                                fg = "black", width = 5, padx = 5, pady = 5,
                                font = ("Time", "14", "bold italic"))
        self.NameLabel.grid(row = 1, column = 0)
        
        self.AgeLabel = Label(self.Welcome, text = "Age",
                                fg = "black", width = 5, padx = 5, pady = 5,
                                font = ("Time", "14", "bold italic"))
        self.AgeLabel.grid(row = 2, column = 0)       
        
        self.feedback1 = Label(self.Welcome, text = "", fg = "red")
        self.feedback1.grid(row = 3, column = 1)
        
        
        #Name & Age Entry
        self.NameEntry = Entry(self.Welcome, width = 15)
        self.NameEntry.grid(row = 1, column = 1)  
        
        self.AgeEntry = Entry(self.Welcome, width = 15)
        self.AgeEntry.grid(row = 2, column = 1) 
        
        
        #Difficulty Level
        
        self.DifficultyLabel = Label(self.Welcome, text = "Choose the Difficulty Level",
                                     fg = "black", padx = 5, pady = 5,
                                     font = ("Time", "11", "bold"))  
        self.DifficultyLabel.grid(row = 4, column = 0, columnspan = 2)
        
        self.DifficultyLevel = ["Easy", "Medium", "Hard"]
        self.Difficulty_Level = StringVar()
        self.Difficulty_Level.set(0)
        self.Difficulty_Level_btns = []
        
        for i in range(len(self.DifficultyLevel)):
            rb = Radiobutton(self.Welcome, variable = self.Difficulty_Level, value = i, text = self.DifficultyLevel[i],
                             padx = 30)
            self.Difficulty_Level_btns.append(rb)
            rb.grid(row = i + 5, column = 0, sticky = W)
        
        
        self.NextButton = Button(self.Welcome, text = "Next", command = self.show_question)
        self.NextButton.grid(row = 9, column = 1, pady = 10)
        
        #2nd Frame
        
        self.question = Frame(parent)
        
        self.questionLabel = Label(self.question, text = "Quiz Questions",
                                        bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                                        font = ("Time", "14", "bold italic"))
        self.questionLabel.grid(columnspan = 2)
        
        self.HomeButton = Button(self.question, text = "Home", command = self.show_Welcome)
        self.HomeButton.grid(row = 9, column = 0, pady = 10)
        
        self.questionLabel2 = Label(self.question, text = "", width = 10, height = 2)
        self.questionLabel2.grid(row = 1, column = 0, sticky = W)
        
        self.AnswerLabel = Entry(self.question, width = 20)
        self.AnswerLabel.grid(row = 1, column = 0, sticky = E)
        
        self.CheckButton = Button(self.question, text = "Check", command = self.check_question)
        self.CheckButton.grid(row = 9, column = 1, pady = 10) 
        
        self.ScoreButton = Button(self.question, text = "Score", command = self.check_score)
        self.ScoreButton.grid(row = 10, column = 0)
        
        self.Feedbacklabel = Label(self.question, text = "")
        self.Feedbacklabel.grid(row = 1, column = 1)
        
        
        
    def show_Welcome(self):
        self.question.grid_remove()
        self.Welcome.grid()

    def show_question(self):
        
        try:
            if self.NameEntry.get() =="":
                self.feedback1.configure(text = "Please enter your name")
            elif self.NameEntry.get().isalpha() == False:
                self.feedback1.configure(text = "Please enter a valid name")
            elif self.AgeEntry.get() == "":
                self.feedback1.configure(text = "Please enter your age")
            elif int(self.AgeEntry.get()) > 12:
                self.feedback1.configure(text = "You are too old.")
            elif int (self.AgeEntry.get()) < 7:
                self.feedback1.configure(text = "You are too young.")
            else:
                self.Welcome.grid_remove()
                self.question.grid()  
                
                x = randrange(10)
                y = randrange(10)                
                
                self.problem_text = str(x) + " + " + str(y) + " = "
                self.questionLabel2.configure(text = self.problem_text)
                self.answer = x + y                  
                
                
        except ValueError:
            self.feedback1.configure(text = "Please enter a number")    
        
    def check_question(self):
                         
            try:    
                self.user_answer = int(self.AnswerLabel.get())
            
                if self.user_answer == self.answer:
                
                    self.Feedbacklabel.configure(text = "Correct!")
                    score = +1
                
                    self.AnswerLabel.delete(0, END)
                    self.AnswerLabel.focus()
        
                    x = randrange(10)
                    y = randrange(10)                
                
                    self.problem_text = str(x) + " + " + str(y) + " = "
                    self.questionLabel2.configure(text = self.problem_text)
                    self.answer = x + y                         
                
                else:   
                    self.Feedbacklabel.configure(text = "Wrong Answer")
                
            except ValueError:
                self.Feedbacklabel.configure(text = "Wrong Answer.")
                self.AnswerLabel.delete(0, END)
                self.AnswerLabel.focus()
                
    def check_score(self):
        
        ScoreLabel = Label(self.question, text = "Your score is []". score)
        ScoreLabel.grid(row = 10, column = 1)
     
if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("Quiz")
    root.mainloop()
    
