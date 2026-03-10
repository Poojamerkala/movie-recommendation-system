import tkinter as tk

# datasets
movies = {
    "kgf": ["Kantara", "Salaar", "Pushpa"],
    "kantara": ["KGF", "Charlie 777", "Vikrant Rona"],
    "premam": ["Bangalore Days", "Hridayam", "Charlie"],
    "vikram": ["Master", "Leo", "Kaithi"]
}

books = {
    "harry potter": ["Percy Jackson", "Narnia", "The Hobbit"],
    "wings of fire": ["Ignited Minds", "My Journey", "Turning Points"],
    "five point someone": ["2 States", "Half Girlfriend", "One Indian Girl"]
}

music = {
    "believer": ["Thunder", "Demons", "Radioactive"],
    "malare": ["Darshana", "Jimikki Kammal", "Pavizha Mazha"],
    "butta bomma": ["Ramulo Ramula", "Samajavaragamana", "Oo Antava"],
    "arabic kuthu": ["Rowdy Baby", "Vaathi Coming", "Why This Kolaveri"]
}

def recommend():

    t = item_type.get()
    name = entry.get().lower()

    if t == "Movie":
        data = movies
    elif t == "Book":
        data = books
    else:
        data = music

    if name in data:
        result_label.config(text="\n".join(data[name]))
    else:
        result_label.config(text="Item not found")


root = tk.Tk()
root.title("Smart Recommendation System")
root.geometry("380x330")
root.configure(bg="#dbeafe")

tk.Label(root,
         text="Smart Recommendation System",
         font=("Arial",16,"bold"),
         bg="#dbeafe",
         fg="#1e3a8a").pack(pady=10)


tk.Label(root,text="Select Item Type",bg="#dbeafe",font=("Arial",11)).pack()

item_type = tk.StringVar()
tk.OptionMenu(root,item_type,"Movie","Book","Music").pack()

tk.Label(root,text="Enter Name",bg="#dbeafe",font=("Arial",11)).pack()

entry = tk.Entry(root,font=("Arial",11),width=25)
entry.pack(pady=5)

tk.Button(root,
          text="Get Recommendations",
          font=("Arial",11,"bold"),
          bg="#2563eb",
          fg="white",
          padx=10,
          pady=5,
          command=recommend).pack(pady=10)

tk.Label(root,
         text="Recommendations",
         font=("Arial",12,"bold"),
         bg="#dbeafe").pack()

result_label = tk.Label(root,
                        text="",
                        bg="white",
                        width=30,
                        height=6,
                        relief="solid",
                        justify="left")

result_label.pack(pady=10)

root.mainloop()