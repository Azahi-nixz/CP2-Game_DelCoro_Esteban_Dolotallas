from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps, ImageEnhance
import os
import sys
import threading

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

def asset(path):
    return os.path.join(_ROOT, path)

from gui.MusicManager import music


# ─────────────────────────────────────────────────────────────
# MUSIC BAR  — subtle persistent strip at the very bottom
# ─────────────────────────────────────────────────────────────
class MusicBar(Frame):
    """
    A slim (~28 px) bar docked to the bottom of the window.
    Contains:
      ♪ / ✕  mute toggle
      ━━━━━  volume slider (Scale widget)
      track label (truncated)
      [+]  browse local file
      [×]  clear custom / revert to slot music
    """
    BAR_H  = 28
    BG     = "#0d0d14"
    FG     = "#555566"
    FG_ACT = "#aaaacc"

    def __init__(self, master, controller):
        super().__init__(master, bg=self.BG, height=self.BAR_H)
        self.controller = controller
        self.place(relx=0, rely=1.0, relwidth=1, anchor="sw")

        self._build()
        self._refresh_label()

    def _build(self):
        # ── mute button ──────────────────────────────────────
        self._mute_btn = Label(
            self, text="♪", font=("rainyhearts", 11),
            fg=self.FG_ACT, bg=self.BG, cursor="hand2", padx=6)
        self._mute_btn.pack(side="left")
        self._mute_btn.bind("<Button-1>", self._toggle_mute)

        # ── volume slider ─────────────────────────────────────
        self._vol_var = DoubleVar(value=music.get_volume())
        self._slider = Scale(
            self, from_=0.0, to=1.0, resolution=0.01,
            orient="horizontal", variable=self._vol_var,
            command=self._on_volume,
            length=90, showvalue=False,
            bg=self.BG, fg=self.FG, troughcolor="#1a1a2e",
            highlightthickness=0, bd=0, sliderlength=10,
            activebackground=self.FG_ACT)
        self._slider.pack(side="left", padx=(0, 6))

        # ── track label ───────────────────────────────────────
        self._track_lbl = Label(
            self, text="", font=("rainyhearts", 9),
            fg=self.FG, bg=self.BG, anchor="w", width=28)
        self._track_lbl.pack(side="left", padx=(0, 4))

        # ── browse button ─────────────────────────────────────
        browse_btn = Label(
            self, text="[+]", font=("rainyhearts", 9),
            fg=self.FG, bg=self.BG, cursor="hand2", padx=4)
        browse_btn.pack(side="left")
        browse_btn.bind("<Button-1>", self._browse)
        browse_btn.bind("<Enter>", lambda e: e.widget.config(fg=self.FG_ACT))
        browse_btn.bind("<Leave>", lambda e: e.widget.config(fg=self.FG))

        # ── clear custom button ───────────────────────────────
        self._clear_btn = Label(
            self, text="[×]", font=("rainyhearts", 9),
            fg=self.FG, bg=self.BG, cursor="hand2", padx=4)
        self._clear_btn.pack(side="left")
        self._clear_btn.bind("<Button-1>", self._clear_custom)
        self._clear_btn.bind("<Enter>", lambda e: e.widget.config(fg="#ff6644"))
        self._clear_btn.bind("<Leave>", lambda e: e.widget.config(fg=self.FG))

    def _on_volume(self, val):
        music.set_volume(float(val))
        self._refresh_mute_icon()

    def _toggle_mute(self, _event=None):
        music.toggle_mute()
        self._refresh_mute_icon()

    def _refresh_mute_icon(self):
        self._mute_btn.config(text="✕" if music.is_muted() else "♪")

    def _refresh_label(self):
        if music.has_custom():
            name = music.get_custom_name() or ""
            # truncate long names
            if len(name) > 28:
                name = name[:25] + "..."
            self._track_lbl.config(text=f"♫ {name}", fg="#8888aa")
            self._clear_btn.config(fg=self.FG)
        else:
            self._track_lbl.config(text="default music", fg=self.FG)
            self._clear_btn.config(fg="#2a2a3a")   # dim — nothing to clear

    def _browse(self, _event=None):
        """Open a file dialog and load the chosen track immediately."""
        path = filedialog.askopenfilename(
            title="Select music file",
            filetypes=[
                ("Audio files", "*.ogg *.mp3 *.wav *.flac"),
                ("All files",   "*.*"),
            ],
            initialdir=os.path.join(_ROOT, "Assets", "Music"),
        )
        if not path:
            return
        if music.load_custom(path):
            self._refresh_label()

    def _clear_custom(self, _event=None):
        """Revert to the slot music for the current screen."""
        if not music.has_custom():
            return
        music.clear_custom()
        self._refresh_label()
        # Re-trigger the current screen's slot music
        self.controller.replay_current_music()

    def update_label(self):
        """Call after any music change to sync the label."""
        self._refresh_label()
        self._vol_var.set(music.get_volume())
        self._refresh_mute_icon()


# ─────────────────────────────────────────────────────────────
# LOADING SCREEN
# ─────────────────────────────────────────────────────────────
class LoadingScreen(Frame):

    _SPLASH_IMAGES = [
        "Assets/download (2).jpg",
        "Assets/download (1).jpg",
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

        try:
            raw = Image.open(asset("Assets/bg.jpg")).convert("RGBA")
            raw = raw.resize((W, H), Image.Resampling.LANCZOS)
            self._refs["bg"] = ImageTk.PhotoImage(
                ImageEnhance.Brightness(raw).enhance(0.18))
            Label(self, image=self._refs["bg"], bd=0).place(
                x=0, y=0, relwidth=1, relheight=1)
        except Exception:
            pass

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

        text_x = int(W * 0.07)
        Label(self, text="BLUROOM BATTLEFIELD",
              font=("rainyhearts", max(16, int(W * 0.022)), "bold"),
              fg="#3399ff", bg="black").place(x=text_x, y=int(H * 0.28))
        Label(self, text="CHARACTER SELECT",
              font=("rainyhearts", max(28, int(W * 0.042)), "bold"),
              fg="#ffffff", bg="black").place(x=text_x, y=int(H * 0.35))
        Frame(self, bg="#3399ff", height=3).place(
            x=text_x, y=int(H * 0.47), width=int(W * 0.35))

        self._loading_lbl = Label(self, text="Loading",
                                  font=("rainyhearts", max(13, int(W * 0.016))),
                                  fg="#888899", bg="black")
        self._loading_lbl.place(x=text_x, y=int(H * 0.52))

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
        self._loading_lbl.config(text="Loading" + "." * (self._dot_count % 4))
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
# HOME SCREEN
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
              font=("rainyhearts", 36, "bold")).pack(pady=(80, 60))

        btn_data = [
            ("Player 1", "Assets/PLAY/p1.png",    "Assets/PLAY/p1_hover.png",
             lambda: controller.show_char_select(1)),
            ("Player 2", "Assets/PLAY/p2.png",    "Assets/PLAY/p2_hover.png",
             lambda: controller.show_char_select(2)),
            ("Guides",   "Assets/PLAY/guide.png", "Assets/PLAY/guide_hover.png",
             controller.open_guides),
            ("Exit",     "Assets/PLAY/exit.png",  "Assets/PLAY/exit_hover.png",
             master.destroy),
        ]

        BTN_W, BTN_H = 280, 60
        for name, img_path, hover_path, cmd in btn_data:
            try:
                norm = ImageOps.fit(Image.open(asset(img_path)),
                                    (BTN_W, BTN_H), Image.Resampling.LANCZOS)
                hov  = ImageOps.fit(Image.open(asset(hover_path)),
                                    (BTN_W, BTN_H), Image.Resampling.LANCZOS)
                self._img_refs[name]          = ImageTk.PhotoImage(norm)
                self._img_refs[name + "_hov"] = ImageTk.PhotoImage(hov)
                btn = Button(self, image=self._img_refs[name],
                             bd=0, highlightthickness=0,
                             activebackground="black", cursor="hand2",
                             command=cmd)
                btn.pack(pady=8)
                btn.bind("<Enter>",
                         lambda e, n=name: e.widget.config(
                             image=self._img_refs[n + "_hov"]))
                btn.bind("<Leave>",
                         lambda e, n=name: e.widget.config(
                             image=self._img_refs[n]))
            except Exception as e:
                print(f"Button error [{name}]: {e}")


# ─────────────────────────────────────────────────────────────
# APP CONTROLLER
# ─────────────────────────────────────────────────────────────
class Interface:
    def __init__(self):
        self.root = Tk()
        self.root.title("Bluroom Battlefield")
        self.root.configure(bg="black")
        self.root.state("zoomed")

        # ── Window + taskbar icon ─────────────────────────────
        ico_path = asset("Assets/BrB.ico")
        if os.path.exists(ico_path):
            try:
                self.root.wm_iconbitmap(ico_path)
            except Exception:
                pass
            try:
                # iconphoto ensures the icon shows in the taskbar on Windows
                img = ImageTk.PhotoImage(
                    Image.open(ico_path).resize((32, 32), Image.Resampling.LANCZOS),
                    master=self.root)
                self.root.iconphoto(True, img)
                self._icon_img = img   # keep reference alive
            except Exception:
                pass

        self._current_frame  = None
        self._current_screen = "menu"   # track which screen for replay

        # Music bar lives on root — persists across all screen switches
        self._music_bar = MusicBar(self.root, self)

        self.show_home()

    def _switch(self, frame):
        if self._current_frame is not None:
            self._current_frame.destroy()
        self._current_frame = frame
        # Keep music bar on top
        self._music_bar.lift()

    def replay_current_music(self):
        """Re-trigger the slot music for whichever screen is active."""
        if self._current_screen == "menu":
            music.play_menu()
        elif self._current_screen == "select":
            music.play_select()
        elif self._current_screen == "battle":
            music.play_battle()

    def show_home(self):
        self._current_screen = "menu"
        music.play_menu()
        self._switch(HomeScreen(self.root, self))
        self._music_bar.update_label()

    def show_char_select(self, mode):
        from gui.CharacterSelect import preload_images_bg, COLS

        loading = LoadingScreen(self.root, self)
        self._switch(loading)
        self.root.update()

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

        result   = [None]
        mode_ref = [mode]

        def do_preload():
            result[0] = preload_images_bg(THUMB_W, THUMB_W, PREV_W, PREV_H, ICON_SZ)
            self.root.after(0, _on_done)

        def _on_done():
            if self._current_frame is loading:
                loading.stop_animations()
                self._current_screen = "select"
                music.play_select()
                from gui.CharacterSelect import CharacterSelectScreen
                self._switch(CharacterSelectScreen(
                    self.root, self, mode=mode_ref[0], preloaded=result[0]))
                self._music_bar.update_label()

        threading.Thread(target=do_preload, daemon=True).start()

    def open_guides(self):
        from gui.Guides import guide
        guide()

    def show_battle(self, mode, p1_name, p2_name):
        from gui.BattleScene import preload_battle_assets_bg, BattleScene

        loading = LoadingScreen(self.root, self)
        self._switch(loading)
        self.root.update()

        self.root.update_idletasks()
        H        = self.root.winfo_height() or 720
        sprite_h = int(H * 0.45)

        result = [None]

        def do_preload():
            result[0] = preload_battle_assets_bg(p1_name, p2_name, sprite_h)
            self.root.after(0, _on_done)

        def _on_done():
            if self._current_frame is loading:
                loading.stop_animations()
                self._current_screen = "battle"
                music.play_battle()
                self._switch(BattleScene(
                    self.root, self, mode, p1_name, p2_name,
                    preloaded=result[0]))
                self._music_bar.update_label()

        threading.Thread(target=do_preload, daemon=True).start()

    def on_selection_done(self, p1_idx, p2_idx, mode):
        from gui.CharacterSelect import CHARACTERS
        p1_name = CHARACTERS[p1_idx]["name"]
        p2_name = CHARACTERS[p2_idx]["name"]
        self.show_battle(mode, p1_name, p2_name)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Interface()
    app.run()
