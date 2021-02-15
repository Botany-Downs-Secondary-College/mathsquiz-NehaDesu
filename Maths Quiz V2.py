from tkinter import*
from random import*

class MathQuiz:
    def __init__(self,parent):
        
        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)
        
        self.TitleLabel = Label(self.Welcome, text = "Welcome to Maths Quiz",
                                bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                                font = ("Time", "14", "bold italic"))
        self.TitleLabel.grid(columnspan = 2)
        
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
        
        self.CheckButton = Button(self.question, text = "Check", command = "check_question")
        self.CheckButton.grid(row = 9, column = 1, pady = 10)        
        
        
        
    def show_Welcome(self):
        self.question.grid_remove()
        self.Welcome.grid()
        
    def show_question(self):
        self.Welcome.grid_remove()
        self.question.grid()  
        
        x = randrange(10)
        y = randrange(10)
        
        self.problem_text = str(x) + " + " + str(y) + " = "
        self.questionLabel2.configure(text = self.problem_text)
        
    def check_question(self):
        
        self.answer = x + y
        
        try:
            self.user_answer = int(self.AnswerLabel.get())
            
            if self.user_answer == self.answer:
                
                self.feedback.configure(text = "Correct!")
                
            else:
                self.feedback.configure(text = "Wrong Answer")
                
        except ValueError:
            self.feedback.configure(text = "Enter your answer as a number.")
            self.AnswerLabel.delete(0, END)
            self.AnswerLabel.focus()
        
if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("Quiz")
    root.mainloop()
    
