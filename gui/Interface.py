from tkinter import *
from PIL import Image, ImageTk, ImageOps, ImageEnhance
import os
import sys
import threading

# Ensure project root is on sys.path so imports work
# whether this file is run directly or as part of a package
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

def asset(path):
    return os.path.join(_ROOT, path)


# ─────────────────────────────────────────────────────────────
# LOADING SCREEN FRAME
# ─────────────────────────────────────────────────────────────
class LoadingScreen(Frame):

    _SPLASH_IMAGES = [
        "Assets/download (2).jpg",
        "Assets/download (1).jpg"
    ]
    _splash_idx = 0

    def __init__(self, master, controller):
        super().__init__(master, bg="black")
        self.place(relwidth=1, relheight=1)
        self.controller = controller
        self._refs      = {}
        self._dot_count = 0
        self._dot_job   = None
        self._bar_job   = None

        self.update_idletasks()
        W = master.winfo_width()  or 1280
        H = master.winfo_height() or 720

        # Dimmed background
        try:
            raw = Image.open(asset("Assets/bg.jpg")).convert("RGBA")
            raw = raw.resize((W, H), Image.Resampling.LANCZOS)
            self._refs["bg"] = ImageTk.PhotoImage(
                ImageEnhance.Brightness(raw).enhance(0.18))
            Label(self, image=self._refs["bg"], bd=0).place(
                x=0, y=0, relwidth=1, relheight=1)
        except Exception:
            pass

        # Character splash (right side)
        splash_path = self._SPLASH_IMAGES[LoadingScreen._splash_idx % len(self._SPLASH_IMAGES)]
        LoadingScreen._splash_idx += 1
        splash_h = int(H * 0.75)
        splash_w = int(splash_h * 0.55)
        try:
            raw_s = Image.open(asset(splash_path)).convert("RGBA")
            raw_s.thumbnail((splash_w, splash_h), Image.Resampling.LANCZOS)
            fade = Image.new("L", raw_s.size, 255)
            for x in range(raw_s.width):
                alpha = int(255 * (1 - (x / raw_s.width) ** 2))
                for y in range(raw_s.height):
                    fade.putpixel((x, y), alpha)
            raw_s.putalpha(fade)
            self._refs["splash"] = ImageTk.PhotoImage(raw_s)
            splash_x = W - raw_s.width - int(W * 0.04)
            splash_y = (H - raw_s.height) // 2
            Label(self, image=self._refs["splash"], bg="black", bd=0).place(
                x=splash_x, y=splash_y)
        except Exception:
            pass

        # Left text block
        text_x = int(W * 0.07)
        Label(self, text="BLUROOM BATTLEFIELD",
              font=("rainyhearts", max(16, int(W * 0.022)), "bold"),
              fg="#3399ff", bg="black"
              ).place(x=text_x, y=int(H * 0.28))
        Label(self, text="CHARACTER SELECT",
              font=("rainyhearts", max(28, int(W * 0.042)), "bold"),
              fg="#ffffff", bg="black"
              ).place(x=text_x, y=int(H * 0.35))
        Frame(self, bg="#3399ff", height=3).place(
            x=text_x, y=int(H * 0.47), width=int(W * 0.35))

        self._loading_lbl = Label(self, text="Loading",
                                  font=("rainyhearts", max(13, int(W * 0.016))),
                                  fg="#888899", bg="black")
        self._loading_lbl.place(x=text_x, y=int(H * 0.52))

        # Progress bar
        bar_y = int(H * 0.60)
        bar_w = int(W * 0.35)
        Frame(self, bg="#1a1a2e").place(x=text_x, y=bar_y, width=bar_w, height=4)
        self._bar_fill = Frame(self, bg="#3399ff")
        self._bar_fill.place(x=text_x, y=bar_y, width=0, height=4)
        self._bar_w   = bar_w
        self._bar_x   = text_x
        self._bar_y   = bar_y
        self._bar_pos = 0
        self._bar_dir = 1

        self._animate_dots()
        self._animate_bar()

    def _animate_dots(self):
        if not self.winfo_exists():
            return
        dots = "." * (self._dot_count % 4)
        self._loading_lbl.config(text=f"Loading{dots}")
        self._dot_count += 1
        self._dot_job = self.after(400, self._animate_dots)

    def _animate_bar(self):
        if not self.winfo_exists():
            return
        chunk = int(self._bar_w * 0.35)
        self._bar_pos += self._bar_dir * 12
        if self._bar_pos + chunk >= self._bar_w:
            self._bar_pos = self._bar_w - chunk
            self._bar_dir = -1
        elif self._bar_pos <= 0:
            self._bar_pos = 0
            self._bar_dir = 1
        self._bar_fill.place(x=self._bar_x + self._bar_pos,
                             y=self._bar_y, width=chunk, height=4)
        self._bar_job = self.after(30, self._animate_bar)

    def stop_animations(self):
        if self._dot_job:
            self.after_cancel(self._dot_job)
        if self._bar_job:
            self.after_cancel(self._bar_job)


# ─────────────────────────────────────────────────────────────
# HOME SCREEN FRAME
# ─────────────────────────────────────────────────────────────
class HomeScreen(Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="black")
        self.controller = controller
        self.place(relwidth=1, relheight=1)
        self._img_refs = {}

        self.update_idletasks()
        w = master.winfo_width()  or 1280
        h = master.winfo_height() or 720

        try:
            raw_bg = Image.open(asset("Assets/bg.jpg"))
            raw_bg = raw_bg.resize((w, h), Image.Resampling.LANCZOS)
            self._img_refs["bg"] = ImageTk.PhotoImage(raw_bg)
            Label(self, image=self._img_refs["bg"], bd=0).place(
                x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Background error: {e}")

        Label(self, text="Bluroom Battlefield",
              fg="white", bg="black",
              font=("rainyhearts", 36, "bold")
              ).pack(pady=(80, 60))

        btn_data = [
            ("Player 1", "Assets/PLAY/p1.png",    "Assets/PLAY/p1_hover.png",    lambda: controller.show_char_select(1)),
            ("Player 2", "Assets/PLAY/p2.png",    "Assets/PLAY/p2_hover.png",    lambda: controller.show_char_select(2)),
            ("Guides",   "Assets/PLAY/guide.png", "Assets/PLAY/guide_hover.png", controller.open_guides),
            ("Exit",     "Assets/PLAY/exit.png",  "Assets/PLAY/exit_hover.png",  master.destroy),
        ]

        BTN_W, BTN_H = 280, 60
        for name, img_path, hover_path, cmd in btn_data:
            try:
                norm = ImageOps.fit(Image.open(asset(img_path)),  (BTN_W, BTN_H), Image.Resampling.LANCZOS)
                hov  = ImageOps.fit(Image.open(asset(hover_path)), (BTN_W, BTN_H), Image.Resampling.LANCZOS)
                self._img_refs[name]          = ImageTk.PhotoImage(norm)
                self._img_refs[name + "_hov"] = ImageTk.PhotoImage(hov)
                btn = Button(self, image=self._img_refs[name],
                             bd=0, highlightthickness=0,
                             activebackground="black", cursor="hand2",
                             command=cmd)
                btn.pack(pady=8)
                btn.bind("<Enter>", lambda e, n=name: e.widget.config(image=self._img_refs[n + "_hov"]))
                btn.bind("<Leave>", lambda e, n=name: e.widget.config(image=self._img_refs[n]))
            except Exception as e:
                print(f"Button error [{name}]: {e}")


# ─────────────────────────────────────────────────────────────
# APP CONTROLLER  (owns the Tk root)
# ─────────────────────────────────────────────────────────────
class Interface:
    def __init__(self):
        self.root = Tk()
        self.root.title("Bluroom Battlefield")
        self.root.configure(bg="black")
        self.root.state("zoomed")

        self._current_frame = None
        self.show_home()

    def _switch(self, frame):
        if self._current_frame is not None:
            self._current_frame.destroy()
        self._current_frame = frame

    def show_home(self):
        self._switch(HomeScreen(self.root, self))

    def show_char_select(self, mode):
        """
        1. Paint loading screen immediately.
        2. Kick off PIL image processing on a background thread.
        3. When done, convert PIL→PhotoImage on main thread and show CharacterSelect.
        """
        from gui.CharacterSelect import preload_images_bg, COLS

        # Show loading screen and force a repaint before anything else
        loading = LoadingScreen(self.root, self)
        self._switch(loading)
        self.root.update()          # paint loading screen NOW

        # Calculate the same dimensions CharacterSelectScreen will use
        self.root.update_idletasks()
        W = self.root.winfo_width()  or 1280
        H = self.root.winfo_height() or 720

        BANNER_H  = max(50, int(H * 0.07))
        BOT_H     = max(80, int(H * 0.12))
        HINT_H    = max(24, int(H * 0.04))
        PAD       = max(8,  int(W * 0.008))
        CONTENT_H = H - BANNER_H - 3 - BOT_H - HINT_H
        LEFT_W    = max(220, int(W * 0.22))
        PREV_W    = LEFT_W - PAD * 2
        PREV_H    = max(200, int(CONTENT_H * 0.72))
        GRID_X    = LEFT_W + PAD * 2
        GRID_W    = W - GRID_X - PAD
        gap       = max(6, int(W * 0.005))
        THUMB_W   = max(80, (GRID_W - (COLS + 1) * gap) // COLS)
        ICON_SZ   = max(50, BOT_H - 16)

        result = [None]   # shared container for thread result

        def do_preload():
            # All heavy PIL work happens here (background thread)
            result[0] = preload_images_bg(THUMB_W, THUMB_W, PREV_W, PREV_H, ICON_SZ)
            # Schedule the final switch on the main thread
            self.root.after(0, lambda: _on_done())

        def _on_done():
            # Only switch if loading screen is still showing
            if self._current_frame is loading:
                loading.stop_animations()
                from gui.CharacterSelect import CharacterSelectScreen
                self._switch(CharacterSelectScreen(
                    self.root, self, mode=mode, preloaded=result[0]))

        threading.Thread(target=do_preload, daemon=True).start()

    def open_guides(self):
        from gui.Guides import guide
        guide()

    def on_selection_done(self, p1_idx, p2_idx):
        from gui.CharacterSelect import CHARACTERS
        print(f"P1 → {CHARACTERS[p1_idx]['name']}")
        print(f"P2 → {CHARACTERS[p2_idx]['name']}")
        # TODO: launch battle screen
        self.show_home()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Interface()
    app.run()
