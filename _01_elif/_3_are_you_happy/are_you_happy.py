from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    window = Tk()
    window.withdraw()
    a = simpledialog.askstring("Happiness", "Are you happy?")
    if(a == "Yes"):
        messagebox.showinfo("Good", "Keep doing whatever you're doing!")
    elif(a == "No"):
        r = simpledialog.askstring("Hmmm", "Do you want to be happy?")
        if(r == "Yes"):
            messagebox.showinfo("Good", "Change something")
        elif(r == "No"):
            messagebox.showinfo("Ok", "Keep doing whatever you're doing")
    pass
