from tkinter import *
from PIL import Image, ImageTk, ImageOps, ImageEnhance, ImageDraw, ImageFont
import os
import sys

# Ensure project root is on sys.path so imports work
# whether this file is run directly or as part of a package
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

def asset(path):
    return os.path.join(_ROOT, path)

# ─────────────────────────────────────────────────────────────
# ROSTER  (11 characters)
# ─────────────────────────────────────────────────────────────
CHARACTERS = [
    {"name": "Maruzen",  "thumbnail": "Assets/Game characters/MaruzenAssets/Thumbnail_maruzen.png", "desc": "Sanity-driven brawler.\nEnrages when pushed to the edge."},
    {"name": "Zen",      "thumbnail": "Assets/Game characters/ZenAssets/Zen_thumbnail.png",          "desc": "Calm swordsman.\nBlood Rage unlocks true power."},
    {"name": "Devourer", "thumbnail": None,                                                           "desc": "Immortal predator.\nDrains life and refuses to die."},
    {"name": "J.A.D.",   "thumbnail": "Assets/Game characters/JADAssets/Thumbnail_JAD.png",          "desc": "Gun & blade duelist.\nAmmo management is key."},
    {"name": "Giga",     "thumbnail": "Assets/Game characters/GigaAssets/Thumbnail_Giga.png",        "desc": "Armored tank.\nReflects damage and buffs himself."},
    {"name": "Minos",    "thumbnail": "Assets/Game characters/MinosAssets/Thumbnail_Minos.png",      "desc": "Luck-based wildcard.\nCan one-shot or barely scratch."},
    {"name": "Pol",      "thumbnail": None,                                                           "desc": "Wind warrior.\nSpeed-scaled damage and counters."},
    {"name": "Sed",      "thumbnail": "Assets/Game characters/SedAssets/Thumbnail_sed.png",          "desc": "War maiden summoner.\nExcalibur mode boosts all stats."},
    {"name": "???",      "thumbnail": None,                                                           "desc": "Identity unknown.\nComing soon..."},
    {"name": "???",      "thumbnail": None,                                                           "desc": "Identity unknown.\nComing soon..."},
    {"name": "???",      "thumbnail": None,                                                           "desc": "Identity unknown.\nComing soon..."},
]

COLS = 6

C_BG     = "#0a0a0f"
C_PANEL  = "#10101a"
C_BORDER = "#2a2a3a"
C_P1     = "#3399ff"
C_P2     = "#ff4444"
C_GOLD   = "#ffd700"
C_WHITE  = "#ffffff"
C_GREY   = "#888899"
C_DARK   = "#1a1a2e"


# ─────────────────────────────────────────────────────────────
# PIL-ONLY HELPERS  (safe to call from any thread)
# Return PIL Image objects, NOT PhotoImage.
# ─────────────────────────────────────────────────────────────
def _pil_load(path, size, crop=True):
    if not path:
        return None
    full = asset(path)
    if not os.path.exists(full):
        return None
    try:
        img = Image.open(full).convert("RGBA")
        if crop:
            img = ImageOps.fit(img, size, Image.Resampling.LANCZOS)
        else:
            img.thumbnail(size, Image.Resampling.LANCZOS)
        return img
    except Exception as e:
        print(f"[CharacterSelect] load error {path}: {e}")
        return None


def _pil_placeholder(size, label="?", bg_color="#1a1a2e"):
    img = Image.new("RGBA", size, bg_color)
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", max(10, size[0] // 4))
    except Exception:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), label, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((size[0] - tw) // 2, (size[1] - th) // 2), label, fill="#555566", font=font)
    draw.rectangle([0, 0, size[0] - 1, size[1] - 1], outline="#2a2a3a", width=2)
    return img


def _pil_dim(path, size, factor=0.45):
    if not path:
        return None
    full = asset(path)
    if not os.path.exists(full):
        return None
    try:
        img = Image.open(full).convert("RGBA")
        img = ImageOps.fit(img, size, Image.Resampling.LANCZOS)
        return ImageEnhance.Brightness(img).enhance(factor)
    except Exception:
        return None


def preload_images_bg(thumb_w, thumb_h, prev_w, prev_h, icon_sz):
    """
    Heavy PIL work — safe to run in a background thread.
    Returns dict of lists of PIL Image objects (NOT PhotoImage).
    """
    norm_pil   = []
    bright_pil = []
    prev_pil   = []
    p1bar_pil  = []
    p2bar_pil  = []

    for char in CHARACTERS:
        path = char.get("thumbnail")
        tag  = char["name"][:3].upper()

        bright = _pil_load(path, (thumb_w, thumb_h)) \
                 or _pil_placeholder((thumb_w, thumb_h), tag)
        bright_pil.append(bright)

        dimmed = _pil_dim(path, (thumb_w, thumb_h)) \
                 or _pil_placeholder((thumb_w, thumb_h), tag, "#0d0d18")
        norm_pil.append(dimmed)

        prev = _pil_load(path, (prev_w, prev_h), crop=False) \
               or _pil_placeholder((prev_w, prev_h), tag, C_DARK)
        prev_pil.append(prev)

        p1 = _pil_load(path, (icon_sz, icon_sz)) \
             or _pil_placeholder((icon_sz, icon_sz), tag, "#0a1a2e")
        p1bar_pil.append(p1)

        p2 = _pil_load(path, (icon_sz, icon_sz)) \
             or _pil_placeholder((icon_sz, icon_sz), tag, "#2e0a0a")
        p2bar_pil.append(p2)

    return {
        "norm":   norm_pil,
        "bright": bright_pil,
        "prev":   prev_pil,
        "p1bar":  p1bar_pil,
        "p2bar":  p2bar_pil,
    }


# ─────────────────────────────────────────────────────────────
# CHARACTER SELECT FRAME
# ─────────────────────────────────────────────────────────────
class CharacterSelectScreen(Frame):

    def __init__(self, master, controller, mode=2, preloaded=None):
        """
        preloaded: dict from preload_images_bg(), already processed on bg thread.
        If None, loads inline (blocking).
        """
        super().__init__(master, bg=C_BG)
        self.place(relwidth=1, relheight=1)

        self.controller = controller
        self.mode       = mode
        self.phase      = 1
        self.cursor     = 0
        self.p1_choice  = None
        self.p2_choice  = None

        # PhotoImage caches — must stay alive as instance attrs
        self._norm   = []
        self._bright = []
        self._prev   = []
        self._p1bar  = []
        self._p2bar  = []

        self.update_idletasks()
        self.W = master.winfo_width()  or 1280
        self.H = master.winfo_height() or 720

        self._build_background()
        self._calc_layout()
        self._build_ui()

        # Convert PIL → PhotoImage on main thread (fast, no I/O)
        if preloaded:
            self._convert(preloaded)
        else:
            self._convert(preload_images_bg(
                self.THUMB_W, self.THUMB_H,
                self.PREV_W,  self.PREV_H,
                self.ICON_SZ
            ))

        self._refresh_grid()
        self._update_preview(0)
        self._update_banner()

        self.focus_set()
        self.bind("<Left>",   lambda e: self._move(-1))
        self.bind("<Right>",  lambda e: self._move(1))
        self.bind("<Up>",     lambda e: self._move(-COLS))
        self.bind("<Down>",   lambda e: self._move(COLS))
        self.bind("<Return>", lambda e: self._confirm())
        self.bind("<Escape>", lambda e: self._back())

    # ── LAYOUT ───────────────────────────────────────────────
    def _calc_layout(self):
        W, H = self.W, self.H
        self.BANNER_H  = max(50, int(H * 0.07))
        self.LINE_H    = 3
        self.BOT_H     = max(80, int(H * 0.12))
        self.HINT_H    = max(24, int(H * 0.04))
        self.PAD       = max(8,  int(W * 0.008))
        content_top    = self.BANNER_H + self.LINE_H
        content_bot    = H - self.BOT_H - self.HINT_H
        self.CONTENT_Y = content_top
        self.CONTENT_H = content_bot - content_top
        self.LEFT_W    = max(220, int(W * 0.22))
        self.PREV_W    = self.LEFT_W - self.PAD * 2
        self.PREV_H    = max(200, int(self.CONTENT_H * 0.72))
        self.GRID_X    = self.LEFT_W + self.PAD * 2
        self.GRID_W    = W - self.GRID_X - self.PAD
        gap            = max(6, int(W * 0.005))
        self.GAP       = gap
        self.THUMB_W   = max(80, (self.GRID_W - (COLS + 1) * gap) // COLS)
        self.THUMB_H   = self.THUMB_W
        self.NAME_H    = max(20, int(H * 0.03))
        self.CELL_H    = self.THUMB_H + self.NAME_H + 4
        self.ICON_SZ   = max(50, self.BOT_H - 16)

    # ── BACKGROUND ───────────────────────────────────────────
    def _build_background(self):
        try:
            raw = Image.open(asset("Assets/bg.jpg")).convert("RGBA")
            raw = raw.resize((self.W, self.H), Image.Resampling.LANCZOS)
            self._bg_photo = ImageTk.PhotoImage(
                ImageEnhance.Brightness(raw).enhance(0.22))
            Label(self, image=self._bg_photo, bd=0).place(
                x=0, y=0, relwidth=1, relheight=1)
        except Exception:
            self._bg_photo = None

    # ── UI ───────────────────────────────────────────────────
    def _build_ui(self):
        W, H = self.W, self.H
        PAD  = self.PAD

        # Banner
        self._banner_bar = Frame(self, bg=C_DARK)
        self._banner_bar.place(x=0, y=0, width=W, height=self.BANNER_H)
        self._banner_lbl = Label(self._banner_bar, text="",
                                 font=("rainyhearts", max(14, int(self.BANNER_H * 0.42)), "bold"),
                                 fg=C_P1, bg=C_DARK)
        self._banner_lbl.place(relx=0.5, rely=0.5, anchor="center")
        back_btn = Label(self._banner_bar, text="◀ BACK",
                         font=("rainyhearts", max(10, int(self.BANNER_H * 0.28))),
                         fg=C_GREY, bg=C_DARK, cursor="hand2")
        back_btn.place(x=PAD * 2, rely=0.5, anchor="w")
        back_btn.bind("<Button-1>", lambda e: self._back())
        self._banner_line = Frame(self, bg=C_P1)
        self._banner_line.place(x=0, y=self.BANNER_H, width=W, height=self.LINE_H)

        # Left panel
        left = Frame(self, bg=C_PANEL)
        left.place(x=PAD, y=self.CONTENT_Y, width=self.LEFT_W, height=self.CONTENT_H)
        self._prev_lbl = Label(left, bg=C_DARK)
        self._prev_lbl.place(x=PAD, y=PAD, width=self.PREV_W, height=self.PREV_H)
        name_y = self.PREV_H + PAD * 2
        self._name_lbl = Label(left, text="",
                               font=("rainyhearts", max(13, int(self.LEFT_W * 0.08)), "bold"),
                               fg=C_GOLD, bg=C_PANEL)
        self._name_lbl.place(x=0, y=name_y, width=self.LEFT_W,
                             height=max(26, int(H * 0.04)))
        desc_y = name_y + max(26, int(H * 0.04)) + PAD
        self._desc_lbl = Label(left, text="",
                               font=("Arial", max(9, int(H * 0.014))),
                               fg=C_GREY, bg=C_PANEL,
                               justify="center", wraplength=self.LEFT_W - PAD * 2)
        self._desc_lbl.place(x=PAD, y=desc_y,
                             width=self.LEFT_W - PAD * 2,
                             height=max(40, int(H * 0.07)))

        # Grid
        grid_bg = Frame(self, bg=C_BG)
        grid_bg.place(x=self.GRID_X, y=self.CONTENT_Y,
                      width=self.GRID_W, height=self.CONTENT_H)
        self._cell_frames = []
        self._cell_imgs   = []
        self._cell_names  = []
        for idx, char in enumerate(CHARACTERS):
            row, col = divmod(idx, COLS)
            fx = self.GAP + col * (self.THUMB_W + self.GAP)
            fy = self.GAP + row * (self.CELL_H  + self.GAP)
            cell = Frame(grid_bg, bg=C_BORDER,
                         width=self.THUMB_W + 4, height=self.CELL_H + 4)
            cell.place(x=fx, y=fy)
            cell.pack_propagate(False)
            img_lbl = Label(cell, bg=C_DARK, cursor="hand2")
            img_lbl.place(x=2, y=2, width=self.THUMB_W, height=self.THUMB_H)
            name_lbl = Label(cell, text=char["name"],
                             font=("rainyhearts", max(7, int(self.THUMB_W * 0.09)), "bold"),
                             fg=C_WHITE, bg=C_BORDER)
            name_lbl.place(x=0, y=self.THUMB_H + 4,
                           width=self.THUMB_W + 4, height=self.NAME_H)
            img_lbl.bind("<Button-1>",  lambda e, i=idx: self._on_click(i))
            img_lbl.bind("<Enter>",     lambda e, i=idx: self._on_hover(i))
            name_lbl.bind("<Button-1>", lambda e, i=idx: self._on_click(i))
            name_lbl.bind("<Enter>",    lambda e, i=idx: self._on_hover(i))
            self._cell_frames.append(cell)
            self._cell_imgs.append(img_lbl)
            self._cell_names.append(name_lbl)

        # Bottom bar
        bot_y = H - self.BOT_H - self.HINT_H
        bot = Frame(self, bg=C_DARK)
        bot.place(x=0, y=bot_y, width=W, height=self.BOT_H)
        mid_x = W // 2
        Frame(bot, bg=C_P1, width=4, height=self.BOT_H).place(x=0, y=0)
        Label(bot, text="PLAYER 1",
              font=("rainyhearts", max(9, int(self.BOT_H * 0.16)), "bold"),
              fg=C_P1, bg=C_DARK).place(x=PAD * 2, y=int(self.BOT_H * 0.1))
        self._p1_name = Label(bot, text="—",
                              font=("rainyhearts", max(13, int(self.BOT_H * 0.22)), "bold"),
                              fg=C_WHITE, bg=C_DARK)
        self._p1_name.place(x=PAD * 2, y=int(self.BOT_H * 0.42))
        self._p1_icon = Label(bot, bg=C_DARK)
        self._p1_icon.place(x=int(W * 0.18), y=(self.BOT_H - self.ICON_SZ) // 2,
                            width=self.ICON_SZ, height=self.ICON_SZ)
        Label(bot, text="VS",
              font=("rainyhearts", max(18, int(self.BOT_H * 0.38)), "bold"),
              fg=C_GOLD, bg=C_DARK).place(x=mid_x, y=int(self.BOT_H * 0.2), anchor="n")
        Frame(bot, bg=C_P2, width=4, height=self.BOT_H).place(x=W - 4, y=0)
        Label(bot, text="PLAYER 2",
              font=("rainyhearts", max(9, int(self.BOT_H * 0.16)), "bold"),
              fg=C_P2, bg=C_DARK).place(x=int(W * 0.72), y=int(self.BOT_H * 0.1))
        self._p2_name = Label(bot, text="—",
                              font=("rainyhearts", max(13, int(self.BOT_H * 0.22)), "bold"),
                              fg=C_WHITE, bg=C_DARK)
        self._p2_name.place(x=int(W * 0.72), y=int(self.BOT_H * 0.42))
        self._p2_icon = Label(bot, bg=C_DARK)
        self._p2_icon.place(x=int(W * 0.6), y=(self.BOT_H - self.ICON_SZ) // 2,
                            width=self.ICON_SZ, height=self.ICON_SZ)

        # Hint bar
        hint_y = H - self.HINT_H
        hint = Frame(self, bg="#050508")
        hint.place(x=0, y=hint_y, width=W, height=self.HINT_H)
        Label(hint,
              text="← → ↑ ↓  Navigate     Enter / Click  Confirm     Esc  Back",
              font=("Arial", max(8, int(self.HINT_H * 0.38))),
              fg="#555566", bg="#050508"
              ).place(relx=0.5, rely=0.5, anchor="center")

    # ── CONVERT PIL → PhotoImage (main thread, fast) ─────────
    def _convert(self, data):
        for pil_img in data["bright"]:
            self._bright.append(ImageTk.PhotoImage(pil_img))
        for pil_img in data["norm"]:
            self._norm.append(ImageTk.PhotoImage(pil_img))
        for pil_img in data["prev"]:
            self._prev.append(ImageTk.PhotoImage(pil_img))
        for pil_img in data["p1bar"]:
            self._p1bar.append(ImageTk.PhotoImage(pil_img))
        for pil_img in data["p2bar"]:
            self._p2bar.append(ImageTk.PhotoImage(pil_img))

    # ── GRID ─────────────────────────────────────────────────
    def _refresh_grid(self):
        for idx in range(len(CHARACTERS)):
            is_cur = idx == self.cursor
            is_p1  = idx == self.p1_choice
            is_p2  = idx == self.p2_choice
            if is_cur:
                border = C_P1 if self.phase == 1 else C_P2
            elif is_p1 and is_p2:
                border = C_GOLD
            elif is_p1:
                border = C_P1
            elif is_p2:
                border = C_P2
            else:
                border = C_BORDER
            self._cell_frames[idx].config(bg=border)
            self._cell_names[idx].config(bg=border)
            img = self._bright[idx] if (is_cur or is_p1 or is_p2) else self._norm[idx]
            self._cell_imgs[idx].config(image=img)
            badge = ""
            if is_p1 and is_p2:
                badge = " ◀P1 P2▶"
            elif is_p1:
                badge = " ◀P1"
            elif is_p2:
                badge = " P2▶"
            self._cell_names[idx].config(text=CHARACTERS[idx]["name"] + badge)

    def _update_preview(self, idx):
        char = CHARACTERS[idx]
        self._prev_lbl.config(image=self._prev[idx])
        self._name_lbl.config(text=char["name"])
        self._desc_lbl.config(text=char["desc"])

    def _update_banner(self):
        if self.phase == 1:
            self._banner_lbl.config(text="PLAYER 1  —  SELECT YOUR FIGHTER", fg=C_P1)
            self._banner_line.config(bg=C_P1)
        else:
            self._banner_lbl.config(text="PLAYER 2  —  SELECT YOUR FIGHTER", fg=C_P2)
            self._banner_line.config(bg=C_P2)

    def _move(self, delta):
        self.cursor = (self.cursor + delta) % len(CHARACTERS)
        self._refresh_grid()
        self._update_preview(self.cursor)

    def _on_hover(self, idx):
        self.cursor = idx
        self._refresh_grid()
        self._update_preview(idx)

    def _on_click(self, idx):
        self.cursor = idx
        self._refresh_grid()
        self._update_preview(idx)
        self._confirm()

    def _confirm(self):
        idx = self.cursor
        if self.phase == 1:
            self.p1_choice = idx
            self._p1_name.config(text=CHARACTERS[idx]["name"])
            self._p1_icon.config(image=self._p1bar[idx])
            if self.mode == 1:
                self.p2_choice = idx
                self.after(400, self._finish)
            else:
                self.phase = 2
                self._update_banner()
                self._refresh_grid()
        elif self.phase == 2:
            self.p2_choice = idx
            self._p2_name.config(text=CHARACTERS[idx]["name"])
            self._p2_icon.config(image=self._p2bar[idx])
            self._refresh_grid()
            self.after(500, self._finish)

    def _back(self):
        if self.phase == 2:
            self.phase = 1
            self.p1_choice = None
            self._p1_name.config(text="—")
            self._p1_icon.config(image="")
            self._update_banner()
            self._refresh_grid()
        else:
            self.controller.show_home()

    def _finish(self):
        self.controller.on_selection_done(self.p1_choice, self.p2_choice)
