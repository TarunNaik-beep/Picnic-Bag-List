from tkinter import *
import random



root = Tk()
root.title("Picnic Bag List")
root.geometry("500x500")

label1 = Label(root)
label2 = Label(root)


List1 = ["Snacks", "Wipes", "Water", "Bag"]

label1["text"] = "Listed_items: "  +str(List1)

def random_number():
    random_list = random.sample(range(0,4),1)
    label2["text"] = "Put Item number" +str(random_list) + " in bag"
    
label1.place(relx=0.5,rely=0.4,anchor=CENTER)
btn = Button(root, text="which item to put in the bag", command=random_number)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label2.place(relx=0.5, rely=0.6, anchor=CENTER)
root.mainloop()
