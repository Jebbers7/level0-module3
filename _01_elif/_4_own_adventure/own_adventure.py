from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    messagebox.showinfo("Story", "Once upon a time, there was an explorer. He is so adventurous that he decides to explore a creepy cave and try to find a treasure. He arrives at the cave, and then sees two entrances. Which entrance should he take?")
    a = simpledialog.askstring("Question", "Which entrance should he take, entrance 1 or entrance 2?")
    if(a == "entrance 1"):
        messagebox.showinfo("Story", "The explorer enters from entrance 1. Immediately, he spots a dragon! Will he attack or flee?")
        r = simpledialog.askstring("Question", "Will he attack or flee?")
        if(r == "attack"):
            messagebox.showinfo("Story", "The explorer attacks! He dodges the dragon's fire and slaughters it! Behind it is a chest full of gold dubloons. The explorer becomes rich and lives happily ever after.")
        elif(r == "flee"):
            messagebox.showinfo("Story", "The explorer, frightened out of his mind, scrambles away in the nick of time. He escapes and never returns.")
    elif(a == "entrance 2"):
        messagebox.showinfo("Story", "The explorer enters from entrance 2. It is dark and quiet, and he gets an eerie feeling... And out pops an enormous spider! Will he attack or flee?")
        r = simpledialog.askstring("Question", "Will he attack or flee?")
        if(r == "attack"):
            messagebox.showinfo("Story", "The explorer attacks! He slides below the spider's webs and stabs the spider through the heart, killing it. Inside the spider's web he finds a treasure chest filled with riches. He takes the chest and lives happily ever after")
        elif(r == "flee"):
            messagebox.showinfo("Story", "The explorer screams, and attempts to scurry out of the cave but is caught by a web shot by the spider! The spider pounces upon him and eats him alive. He is never seen again.")
