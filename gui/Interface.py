from tkinter import *
from PIL import Image, ImageTk, ImageOps
import os

# Resolve asset paths relative to project root
_ROOT = os.path.dirname(os.path.dirname(__file__))

def asset(path):
    return os.path.join(_ROOT, path)


class Interface:
    def __init__(self):
        self.root = Tk()
        self.root.title("Bluroom Battlefield")

        WIN_W, WIN_H = 500, 500
        self.root.geometry(f"{WIN_W}x{WIN_H}")
        try:
            raw_bg = Image.open(asset("Assets/bg.jpg"))
            self.bg = ImageTk.PhotoImage(raw_bg)

            self.bg_label = Label(self.root, image=self.bg)
            self.bg_label.place(relwidth=1, relheight=1)
        except Exception as e:
            print(f"Error loading background: {e}")
            self.root.configure(bg="black")

        self.btn_images = {}
        self.btn_hover_images = {}

        self.upper_grid("Bluroom Battlefield")
        self.lower_grid()

    def upper_grid(self, text):
        self.upper_text = Label(self.root,
                                text=text,
                                fg="white",
                                bg="black",
                                font=("rainyhearts", 72, "bold"))

        self.upper_text.pack(pady=(40, 100))

    def lower_grid(self):
        buttons = ["Player 1", "Player 2", "Guides", "Exit"]
        images = [
            asset("Assets/PLAY/p1.png"),
            asset("Assets/PLAY/p2.png"),
            asset("Assets/PLAY/guide.png"),
            asset("Assets/PLAY/exit.png")
        ]
        hovers = [
            asset("Assets/PLAY/p1_hover.png"),
            asset("Assets/PLAY/p2_hover.png"),
            asset("Assets/PLAY/guide_hover.png"),
            asset("Assets/PLAY/exit_hover.png")
        ]

        BTN_W, BTN_H = 280, 60

        for name, img_path, hover_path in zip(buttons, images, hovers):
            try:
                raw_norm = Image.open(img_path)
                raw_hov = Image.open(hover_path)

                norm_resized = ImageOps.fit(raw_norm, (BTN_W, BTN_H), Image.Resampling.LANCZOS)
                hov_resized = ImageOps.fit(raw_hov, (BTN_W, BTN_H), Image.Resampling.LANCZOS)

                self.btn_images[name] = ImageTk.PhotoImage(norm_resized)
                self.btn_hover_images[name] = ImageTk.PhotoImage(hov_resized)

                btn = Button(self.root,
                             text=name,
                             font=("rainyhearts", 18, "bold"),
                             image=self.btn_images[name],
                             fg="white",
                             bd=0,
                             highlightthickness=0,
                             activebackground="black",
                             cursor="hand2")

                btn.pack(pady=10)

                btn.bind("<Enter>", lambda e, n=name: e.widget.config(image=self.btn_hover_images[n]))
                btn.bind("<Leave>", lambda e, n=name: e.widget.config(image=self.btn_images[n]))

            except Exception as e:
                print(f"Error processing {name}: {e}")


if __name__ == "__main__":
    app = Interface()
    app.root.mainloop()
