from tkinter import Tk, Toplevel, Label, Text, END, BOTH
import os

def guide():

    # Use Toplevel if a root window already exists, otherwise create one
    try:
        root = Tk._default_root
        if root is not None:
            app = Toplevel(root)
        else:
            raise AttributeError
    except AttributeError:
        app = Tk()

    app.title("Guides")
    app.geometry("800x800")

    label = Label(app, text="Guides",
                  font='Arial 24 bold',
                  fg="blue")
    label.pack(pady=10)

    guides = []

    # Resolve path relative to project root
    guides_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Guides.txt")
    with open(guides_path, "r", encoding="utf-8") as f:
        for line in f:
            guides.append(line)

    full_text = "".join(guides)

    display_area = Text(app, font='Arial 14', wrap="word", padx=20, pady=20)
    display_area.insert(END, full_text)

    display_area.config(state=DISABLED)

    display_area.pack(expand=True, fill=BOTH)

    app.mainloop()
