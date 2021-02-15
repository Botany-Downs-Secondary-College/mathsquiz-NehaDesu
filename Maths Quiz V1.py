from tkinter import*

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
        
        self.question = Frame(parent)
        
        
        self.questionLabel = Label(self.question, text = "Quiz Questions",
                                        bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                                        font = ("Time", "14", "bold italic"))
        self.questionLabel.grid(columnspan = 2)
        
        self.HomeButton = Button(self.question, text = "Home", command = self.show_Welcome)
        self.HomeButton.grid(row = 9, column = 1, pady = 10)
        
    def show_Welcome(self):
        self.question.grid_remove()
        self.Welcome.grid()
        
    def show_question(self):
        self.Welcome.grid_remove()
        self.question.grid()        
       
        
        
if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("Quiz")
    root.mainloop()
    
   