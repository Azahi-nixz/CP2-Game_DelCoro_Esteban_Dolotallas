from tkinter import *
from PIL import Image, ImageTk, ImageOps, ImageEnhance
import os, sys, random, io

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

def asset(path):
    return os.path.join(_ROOT, path)

from characters.Maruzensky   import Maruzen
from characters.Zen          import Zen
from characters.Devourer     import Devourer
from characters.JAD          import JAD
from characters.Giga         import Giga
from characters.Minos        import Minos
from characters.Pol          import Pol
from characters.Sed          import Sed
from characters.Russel       import Russel
from characters.Sol_Emberload import SolEmberload
from characters.Hotori       import Hotori

CHARACTER_MAP = {
    "Maruzen":      Maruzen,
    "Zen":          Zen,
    "Devourer":     Devourer,
    "J.A.D.":       JAD,
    "Giga":         Giga,
    "Minos":        Minos,
    "Pol":          Pol,
    "Sed":          Sed,
    "Russelle":     Russel,
    "Sol Emberload": SolEmberload,
    "Hotori":       Hotori,
}

CHARACTER_ASSETS = {
    "Maruzen": {
        "p1":           "Assets/Game characters/MaruzenAssets/Maruzen_player1.png",
        "p2":           "Assets/Game characters/MaruzenAssets/Maruzen_player2.png",
        "win":          "Assets/Game characters/MaruzenAssets/Maruzen_win.png",
        "lose":         "Assets/Game characters/MaruzenAssets/Maruzen_lose.png",
        "enraged_p1":   "Assets/Game characters/MaruzenAssets/enraged_player1.png",
        "enraged_p2":   "Assets/Game characters/MaruzenAssets/enraged_player2.png",
        "enraged_win":  "Assets/Game characters/MaruzenAssets/enraged_win.png",
        "enraged_lose": "Assets/Game characters/MaruzenAssets/enraged_lose.png",
    },
    "Zen": {
        "p1":   "Assets/Game characters/ZenAssets/zen_p1.png",
        "p2":   "Assets/Game characters/ZenAssets/zen_p2.png",
        "win":  "Assets/Game characters/ZenAssets/zen_win.png",
        "lose": "Assets/Game characters/ZenAssets/zen_lose.png",
    },
    "Devourer": {
        "p1":   "Assets/Game characters/DevourerAssets/devourer_p1.png",
        "p2":   "Assets/Game characters/DevourerAssets/devourer_p2.png",
        "win":  "Assets/Game characters/DevourerAssets/devourer_win.png",
        "lose": "Assets/Game characters/DevourerAssets/devourer_lose.png",
    },
    "J.A.D.": {
        "p1":   "Assets/Game characters/JADAssets/JAD_p1.png",
        "p2":   "Assets/Game characters/JADAssets/JAD_p2.png",
        "win":  "Assets/Game characters/JADAssets/JAD_win.png",
        "lose": "Assets/Game characters/JADAssets/JAD_lose.png",
    },
    "Giga": {
        "p1":   "Assets/Game characters/GigaAssets/Giga_p1.png",
        "p2":   "Assets/Game characters/GigaAssets/Giga_p2.png",
        "win":  "Assets/Game characters/GigaAssets/Giga_win.png",
        "lose": "Assets/Game characters/GigaAssets/Giga_lose.png",
    },
    "Minos": {
        "p1":   "Assets/Game characters/MinosAssets/Minos_p1.png",
        "p2":   "Assets/Game characters/MinosAssets/Minos_p2.png",
        "win":  "Assets/Game characters/MinosAssets/Minos_win.png",
        "lose": "Assets/Game characters/MinosAssets/Minos_lose.png",
    },
    "Pol": {
        "p1":   "Assets/Game characters/PolAssets/pol_p1.png",
        "p2":   "Assets/Game characters/PolAssets/pol_p2.png",
        "win":  "Assets/Game characters/PolAssets/pol_win.png",
        "lose": "Assets/Game characters/PolAssets/pol_lose.png",
    },
    "Sed": {
        "p1":   "Assets/Game characters/SedAssets/p1_sed.png",
        "p2":   "Assets/Game characters/SedAssets/p2_sed.png",
        "win":  "Assets/Game characters/SedAssets/win_sed.png",
        "lose": "Assets/Game characters/SedAssets/lose_sed.png",
    },
    "Russelle": {
        "p1":   "Assets/Game characters/RusselleAssets/p1_russele.png",
        "p2":   "Assets/Game characters/RusselleAssets/p2_russelle.png",
        "win":  "Assets/Game characters/RusselleAssets/win_russelle.png",
        "lose": "Assets/Game characters/RusselleAssets/lose_russelle.png",
    },
    "Sol Emberload": {
        "p1":   "Assets/Game characters/EmberloadAssets/p1_emberload.png",
        "p2":   "Assets/Game characters/EmberloadAssets/emberload_p2.png",
        "win":  "Assets/Game characters/EmberloadAssets/emberload_win.png",
        "lose": "Assets/Game characters/EmberloadAssets/emberload_lose.png",
    },
    "Hotori": {
        "p1":   "Assets/Game characters/EnzoAssets/p1_enzo.png",
        "p2":   "Assets/Game characters/EnzoAssets/p2_enzo.png",
        "win":  "Assets/Game characters/EnzoAssets/enzo_win.png",
        "lose": "Assets/Game characters/EnzoAssets/enzo_lose.png",
    },
}

# ── Attack animation configs per character ──────────────────
# "attack_color"  : flash tint on the ATTACKER sprite label
# "hit_color"     : screen-flash colour when the DEFENDER is hit
# "attack_offset" : px the attacker lunges toward the enemy
ANIM_CONFIG = {
    "Maruzen":       {"attack_color": "#ff6622", "hit_color": "#ff5533", "attack_offset": 60},
    "Zen":           {"attack_color": "#aaddff", "hit_color": "#4488cc", "attack_offset": 70},
    "Devourer":      {"attack_color": "#aa00ff", "hit_color": "#7700cc", "attack_offset": 65},
    "J.A.D.":        {"attack_color": "#ffee44", "hit_color": "#ccaa00", "attack_offset": 45},
    "Giga":          {"attack_color": "#44ffaa", "hit_color": "#22aa66", "attack_offset": 50},
    "Minos":         {"attack_color": "#ffd700", "hit_color": "#cc9900", "attack_offset": 55},
    "Pol":           {"attack_color": "#88ffee", "hit_color": "#44ccaa", "attack_offset": 75},
    "Sed":           {"attack_color": "#ff88cc", "hit_color": "#cc4488", "attack_offset": 60},
    "Russel":        {"attack_color": "#ccccff", "hit_color": "#8888cc", "attack_offset": 40},
    "Sol Emberload": {"attack_color": "#ff4400", "hit_color": "#cc2200", "attack_offset": 65},
    "Hotori":        {"attack_color": "#00eeff", "hit_color": "#0099bb", "attack_offset": 80},
}

SKILL_DESCS = {
    "Maruzen": {
        "normal": [
            ("Basic\nWhy would I fight?",  "Restore +10 sanity. 10% bonus turn."),
            ("Please Slap Me",             "Heal last damage taken. -20 sanity."),
            ("Invincible",                 "Immune to damage 2 turns. -30 sanity."),
            ("Sanity Implosion",           "Deal sanity/2 dmg. Lose sanity/2."),
        ],
        "enraged": [
            ("Payback",                    "1-3 hits, 5% MaxHP each. Combo bonus."),
            ("Manipulation",               "Surrender chance scales with turns."),
            ("Death Wish",                 "30 + (100-sanity)/5 damage dealt."),
            ("System Sabotage",            "Inflict Sabotage on enemy 2 turns."),
        ],
    },
    "Zen": {
        "normal": [
            ("Basic\nGale Strike",         "5 dmg (normal) or full ATK (Blood Rage)."),
            ("A Lost Cause",               "0.2x ATK. +40 Blood Rage gauge."),
            ("A Silent Plead",             "Gain High Counter buff 3 turns."),
            ("Death Slash",                "1x ATK. Halve Blood Rage gauge."),
        ],
    },
    "J.A.D.": {
        "Gun": [
            ("Basic\nGunshot",             "0.3x ATK. Costs 1 ammo."),
            ("Gunho",                      "Clear all enemy buffs & self debuffs."),
            ("Long Shot",                  "Costs 2 ammo. Near-kill headshot (10%)."),
            ("Mist",                       "Costs 3 ammo. Blind enemy 2 turns."),
        ],
        "Hand": [
            ("Basic\nKnife Slash",         "0.2x ATK."),
            ("Gunho",                      "Clear all enemy buffs & self debuffs."),
            ("Backstab",                   "0.4x ATK."),
            ("Throat Cutter",              "15% chance to instantly execute."),
        ],
    },
    "Giga": {
        "normal": [
            ("Basic\nShield Bash",         "0.5x ATK. Reflects 30% dmg taken."),
            ("Double Damage",              "Next attack deals 2x damage."),
            ("Invincible",                 "Immune to all damage for 2 turns."),
            ("Enhanced",                   "Double all stats for 2 turns."),
        ],
    },
    "Minos": {
        "normal": [
            ("Basic\nLucky Strike",        "Random damage 1-999 based on luck."),
            ("Dunca Tonca",                "+5 luck permanently."),
            ("Take It All",                "50%: SE Immunity + Regen. 50%: Vulnerable."),
            ("Immortality",                "Cannot die for 2 turns."),
        ],
    },
    "Devourer": {
        "normal": [
            ("Basic\nSlash",               "20 + 0.1x ATK dmg. Regen 5 HP/turn."),
            ("Lemme Suck 'Em",             "Drain 20% of enemy current HP."),
            ("Lethal Claw",                "20 dmg + Bleeding 2 turns."),
            ("Immortality",                "Cannot die for 2 turns."),
        ],
    },
    "Pol": {
        "normal": [
            ("Basic\nGale Slash",          "20 + 0.1x SPD damage."),
            ("Stance: Unyielding",         "Gain High Counter buff 3 turns."),
            ("Drive: Windcharge",          "0.2x ATK + 0.3x SPD damage."),
            ("Wind Maiden Hael",           "Gain Covenant of Wind. Clear debuffs."),
        ],
    },
    "Sed": {
        "normal": [
            ("Basic\nGale Slash",          "20 + 0.1x SPD damage."),
            ("Serene Posture",             "Gain BA Boost buff 3 turns."),
            ("Warhammer Onslaught",        "0.6x ATK damage."),
            ("War Maiden Ei-ram",          "Gain Excalibur buff. Clear debuffs."),
        ],
    },
    "Russel": {
        "normal": [
            ("Basic\nIron Fist",           "20 + 0.5x ATK. 80% dmg reduction."),
            ("Sleep Cures All",            "Heal 30% MaxHP. 15% extra dmg reduction while sleeping."),
            ("Let's Dance!",               "Taunt: enemy uses basic only. Both take 20% more dmg."),
            ("Guardian Angel",             "Passive: Auto-revive at 35% HP once. Immune to debuffs 1 turn."),
        ],
    },
    "Sol Emberload": {
        "normal": [
            ("Basic\nEmber Strike",        "ATK dmg + Burned 2 turns."),
            ("Sol Kick",                   "ATK + 25 damage."),
            ("Smoke Veil",                 "Blind enemy. Heal self 15 HP."),
            ("Inferno Burst",              "2x ATK dmg + Burned 3 turns."),
        ],
    },
    "Hotori": {
        "normal": [
            ("Basic\nBasic Attack",        "15 dmg. 20% bonus turn chance."),
            ("Chrono Shift",               "Recover last damage taken as HP."),
            ("Godspeed",                   "Deal 30% of enemy current HP."),
            ("Time Stop",                  "Freeze enemy 4 turns. Reset cooldowns."),
        ],
    },
}

# Colours
C_BG     = "#ffffff"
C_DARK   = "#1a1a2e"
C_PANEL  = "#f5f5f5"
C_P1     = "#3399ff"
C_P2     = "#ff4444"
C_GOLD   = "#ffd700"
C_GREY   = "#555566"
C_GREEN  = "#22cc66"
C_RED    = "#ff3333"
C_BUFF   = "#44aaff"
C_DEBUFF = "#ff6644"


def preload_battle_assets_bg(p1_name, p2_name, sprite_h):
    result = {"p1": {}, "p2": {}}
    for player, char_name in [("p1", p1_name), ("p2", p2_name)]:
        assets = CHARACTER_ASSETS.get(char_name, {})
        for state, path in assets.items():
            full = asset(path)
            if path and os.path.exists(full):
                try:
                    img = Image.open(full).convert("RGBA")
                    img.thumbnail((int(sprite_h * 0.75), sprite_h), Image.Resampling.LANCZOS)
                    result[player][state] = img
                except Exception as e:
                    print(f"[Battle] sprite load error {path}: {e}")
    return result


class BattleScene(Frame):
    """
    Full battle scene frame.
    mode=1 → P1 vs Bot   mode=2 → P1 vs P2
    """

    def __init__(self, master, controller, mode, p1_name, p2_name, preloaded=None):
        super().__init__(master, bg=C_BG)
        self.place(relwidth=1, relheight=1)

        self.controller = controller
        self.mode       = mode
        self.p1_name    = p1_name
        self.p2_name    = p2_name

        self.p1 = CHARACTER_MAP[p1_name]()
        self.p2 = CHARACTER_MAP[p2_name]()

        self.current_turn  = 1
        self.turn_number   = 1
        self.game_over     = False
        self.waiting_input = False
        self._paused       = False          # game pause state

        # Configurable turn timer (seconds); default 60, range 60-120
        self._turn_duration = 60
        self.p1_time        = self._turn_duration
        self.p2_time        = self._turn_duration
        self._timer_job     = None

        self._sprites  = {"p1": {}, "p2": {}}
        self._img_refs = {}

        self._p1_base_x = 0
        self._p2_base_x = 0
        self._sprite_y  = 0
        self._anim_jobs = []

        self._log_buffer  = []
        self._orig_stdout = sys.stdout
        self._log_capture = _LogCapture(self._log_buffer)

        # Settings panel reference (created lazily)
        self._settings_panel = None

        self.update_idletasks()
        self.W = master.winfo_width()  or 1280
        self.H = master.winfo_height() or 720

        self._build_ui()

        if preloaded:
            self._convert_sprites(preloaded)

        self._update_display()
        self._start_timer()
        self.after(400, self._process_turn)

        # Keyboard shortcut: Escape → toggle settings/pause
        self.focus_set()
        self.bind("<Escape>", lambda e: self._toggle_settings())

    # ── SPRITE CONVERSION ────────────────────────────────────
    def _convert_sprites(self, preloaded):
        for side in ("p1", "p2"):
            for state, pil_img in preloaded[side].items():
                self._sprites[side][state] = ImageTk.PhotoImage(pil_img)

    # ── UI BUILD ─────────────────────────────────────────────
    def _build_ui(self):
        W, H = self.W, self.H

        TOP_H = max(110, int(H * 0.15))
        BOT_H = max(180, int(H * 0.26))
        MID_H = H - TOP_H - BOT_H
        BAR_W = int(W * 0.32)
        PAD   = max(10, int(W * 0.01))

        self._TOP_H = TOP_H
        self._MID_H = MID_H
        self._BOT_H = BOT_H
        self._BAR_W = BAR_W
        self._PAD   = PAD

        # ── TOP BAR ──────────────────────────────────────────
        top = Frame(self, bg=C_DARK, height=TOP_H)
        top.place(x=0, y=0, width=W, height=TOP_H)

        Label(top, text="PLAYER 1", font=("rainyhearts", 11, "bold"),
              fg=C_P1, bg=C_DARK).place(x=PAD, y=6)
        self._p1_name_lbl = Label(top, text=self.p1_name,
                                  font=("rainyhearts", 13, "bold"),
                                  fg="white", bg=C_DARK)
        self._p1_name_lbl.place(x=PAD, y=24)

        Frame(top, bg="#333344").place(x=PAD, y=52, width=BAR_W, height=16)
        self._p1_hp_fill = Frame(top, bg=C_P1)
        self._p1_hp_fill.place(x=PAD, y=52, width=BAR_W, height=16)
        self._p1_hp_lbl = Label(top, text="", font=("Arial", 9, "bold"),
                                fg="white", bg=C_DARK)
        self._p1_hp_lbl.place(x=PAD, y=71)
        self._p1_stat_lbl = Label(top, text="", font=("rainyhearts", 10),
                                  fg=C_GOLD, bg=C_DARK)
        self._p1_stat_lbl.place(x=PAD, y=88)
        self._p1_timer_lbl = Label(top, text="60",
                                   font=("rainyhearts", 26, "bold"),
                                   fg=C_P1, bg=C_DARK)
        self._p1_timer_lbl.place(x=PAD + BAR_W + 10, y=28)

        Label(top, text="VS", font=("rainyhearts", 20, "bold"),
              fg=C_GOLD, bg=C_DARK).place(x=W // 2, y=TOP_H // 2 - 14, anchor="n")
        self._turn_lbl = Label(top, text="", font=("rainyhearts", 12, "bold"),
                               fg=C_GOLD, bg=C_DARK)
        self._turn_lbl.place(x=W // 2, y=TOP_H - 22, anchor="n")

        # ── Settings / Pause button ───────────────────────────
        self._settings_btn = Label(
            top, text="⚙", font=("rainyhearts", 18),
            fg="#555566", bg=C_DARK, cursor="hand2")
        self._settings_btn.place(x=W // 2 + 44, y=6)
        self._settings_btn.bind("<Button-1>", lambda e: self._toggle_settings())
        self._settings_btn.bind("<Enter>",    lambda e: self._settings_btn.config(fg=C_GOLD))
        self._settings_btn.bind("<Leave>",    lambda e: self._settings_btn.config(fg="#555566"))

        p2_bar_x = W - PAD - BAR_W
        Label(top, text="PLAYER 2", font=("rainyhearts", 11, "bold"),
              fg=C_P2, bg=C_DARK).place(x=p2_bar_x, y=6)
        self._p2_name_lbl = Label(top, text=self.p2_name,
                                  font=("rainyhearts", 13, "bold"),
                                  fg="white", bg=C_DARK)
        self._p2_name_lbl.place(x=p2_bar_x, y=24)

        Frame(top, bg="#333344").place(x=p2_bar_x, y=52, width=BAR_W, height=16)
        self._p2_hp_fill = Frame(top, bg=C_P2)
        self._p2_hp_fill.place(x=p2_bar_x, y=52, width=BAR_W, height=16)
        self._p2_hp_lbl = Label(top, text="", font=("Arial", 9, "bold"),
                                fg="white", bg=C_DARK)
        self._p2_hp_lbl.place(x=p2_bar_x, y=71)
        self._p2_stat_lbl = Label(top, text="", font=("rainyhearts", 10),
                                  fg=C_GOLD, bg=C_DARK)
        self._p2_stat_lbl.place(x=p2_bar_x, y=88)
        self._p2_timer_lbl = Label(top, text="60",
                                   font=("rainyhearts", 26, "bold"),
                                   fg=C_P2, bg=C_DARK)
        self._p2_timer_lbl.place(x=p2_bar_x - 60, y=28)

        # ── MIDDLE ───────────────────────────────────────────
        mid_y     = TOP_H
        self._mid = Frame(self, bg=C_BG)
        self._mid.place(x=0, y=mid_y, width=W, height=MID_H)

        sprite_h = int(MID_H * 0.72)
        sprite_y = int(MID_H * 0.04)
        self._sprite_y  = sprite_y
        self._p1_base_x = int(W * 0.12)
        self._p2_base_x = int(W * 0.88)

        self._p1_sprite = Label(self._mid, bg=C_BG)
        self._p1_sprite.place(x=self._p1_base_x, y=sprite_y, anchor="n")

        self._p2_sprite = Label(self._mid, bg=C_BG)
        self._p2_sprite.place(x=self._p2_base_x, y=sprite_y, anchor="n")

        # Flash overlay — covers the whole middle area, normally hidden
        self._flash_overlay = Frame(self._mid, bg=C_BG)
        self._flash_overlay.place(x=0, y=0, width=W, height=MID_H)
        self._flash_overlay.lower()  # behind sprites by default

        eff_y = sprite_y + sprite_h + 4
        self._p1_buffs_lbl = Label(self._mid, text="", font=("rainyhearts", 11, "bold"),
                                   fg=C_BUFF, bg=C_BG, justify="left",
                                   wraplength=int(W * 0.3))
        self._p1_buffs_lbl.place(x=PAD, y=eff_y)
        self._p1_debuffs_lbl = Label(self._mid, text="", font=("rainyhearts", 11, "bold"),
                                     fg=C_DEBUFF, bg=C_BG, justify="left",
                                     wraplength=int(W * 0.3))
        self._p1_debuffs_lbl.place(x=PAD, y=eff_y + 22)

        self._p2_buffs_lbl = Label(self._mid, text="", font=("rainyhearts", 11, "bold"),
                                   fg=C_BUFF, bg=C_BG, justify="right",
                                   wraplength=int(W * 0.3))
        self._p2_buffs_lbl.place(x=W - PAD - int(W * 0.3), y=eff_y)
        self._p2_debuffs_lbl = Label(self._mid, text="", font=("rainyhearts", 11, "bold"),
                                     fg=C_DEBUFF, bg=C_BG, justify="right",
                                     wraplength=int(W * 0.3))
        self._p2_debuffs_lbl.place(x=W - PAD - int(W * 0.3), y=eff_y + 22)

        # ── BOTTOM ───────────────────────────────────────────
        bot_y = TOP_H + MID_H
        bot   = Frame(self, bg=C_PANEL)
        bot.place(x=0, y=bot_y, width=W, height=BOT_H)

        log_w     = int(W * 0.42)
        log_frame = Frame(bot, bg=C_DARK, relief="flat")
        log_frame.place(x=PAD, y=PAD, width=log_w, height=BOT_H - PAD * 2)

        self._battle_log = Text(log_frame, font=("rainyhearts", 12),
                                bg=C_DARK, fg="white", wrap="word",
                                state="disabled", relief="flat", bd=0,
                                padx=8, pady=6)
        self._battle_log.pack(fill="both", expand=True)
        self._battle_log.tag_config("p1",     foreground=C_P1)
        self._battle_log.tag_config("p2",     foreground=C_P2)
        self._battle_log.tag_config("system", foreground=C_GOLD)
        self._battle_log.tag_config("damage", foreground=C_RED)
        self._battle_log.tag_config("buff",   foreground=C_BUFF)
        self._battle_log.tag_config("debuff", foreground=C_DEBUFF)
        self._battle_log.tag_config("heal",   foreground=C_GREEN)

        skill_x = log_w + PAD * 3
        skill_w = W - skill_x - PAD
        btn_h   = max(36, (BOT_H - PAD * 3) // 4)

        self._skill_btns  = []
        self._skill_descs = []
        for i in range(4):
            row_y = PAD + i * (btn_h + 4)
            btn = Button(bot, text="", font=("rainyhearts", 11, "bold"),
                         bg=C_DARK, fg="white",
                         activebackground="#2a2a4a", activeforeground="white",
                         relief="flat", bd=0, cursor="hand2",
                         state="disabled", anchor="w", padx=10,
                         command=lambda idx=i + 1: self._on_skill_click(idx))
            btn.place(x=skill_x, y=row_y, width=int(skill_w * 0.38), height=btn_h)
            desc_lbl = Label(bot, text="", font=("Arial", 9),
                             fg=C_GREY, bg=C_PANEL, justify="left", anchor="w",
                             wraplength=int(skill_w * 0.58))
            desc_lbl.place(x=skill_x + int(skill_w * 0.40), y=row_y,
                           width=int(skill_w * 0.58), height=btn_h)
            self._skill_btns.append(btn)
            self._skill_descs.append(desc_lbl)

    # ── LOGGING ──────────────────────────────────────────────
    def _log(self, text, tag="system"):
        self._battle_log.config(state="normal")
        self._battle_log.insert("end", text + "\n", tag)
        self._battle_log.see("end")
        self._battle_log.config(state="disabled")

    def _flush_capture(self, tag="system"):
        lines = "".join(self._log_buffer).strip()
        self._log_buffer.clear()
        if lines:
            for line in lines.splitlines():
                line = line.strip()
                if not line:
                    continue
                lo = line.lower()
                if any(k in lo for k in ("took", "damage", "dmg", "executed", "evaded", "reflected")):
                    t = "damage"
                elif any(k in lo for k in ("gained buff", "immune", "invincible", "double", "enhanced",
                                           "regen", "jackpot", "covenant", "excalibur", "ba boost",
                                           "high counter", "immortality", "chrono", "time stop")):
                    t = "buff"
                elif any(k in lo for k in ("debuff", "bleeding", "sabotage", "blind", "vulnerable",
                                           "received debuff", "frozen", "burned")):
                    t = "debuff"
                elif any(k in lo for k in ("heal", "recovered", "iron will", "hp added", "regen activated",
                                           "heals", "sleep")):
                    t = "heal"
                else:
                    t = tag
                self._log(line, t)

    # ── ANIMATIONS ───────────────────────────────────────────
    def _cancel_anims(self):
        for j in self._anim_jobs:
            try:
                self.after_cancel(j)
            except Exception:
                pass
        self._anim_jobs.clear()

    def _play_attack_anim(self, attacker_side, defender_side, on_done):
        """
        Attacker lunges toward the defender, then snaps back.
        Defender flashes red on impact. A colour tint fades over the screen.
        """
        self._cancel_anims()

        cfg      = ANIM_CONFIG.get(self.p1_name if attacker_side == "p1" else self.p2_name,
                                   {"attack_color": "#ffffff", "hit_color": "#ff000033",
                                    "attack_offset": 60})
        offset   = cfg["attack_offset"]
        atk_lbl  = self._p1_sprite if attacker_side == "p1" else self._p2_sprite
        hit_lbl  = self._p2_sprite if attacker_side == "p1" else self._p1_sprite
        base_atk = self._p1_base_x if attacker_side == "p1" else self._p2_base_x
        base_hit = self._p2_base_x if attacker_side == "p1" else self._p1_base_x

        # Direction: p1 moves RIGHT, p2 moves LEFT
        direction = 1 if attacker_side == "p1" else -1

        STEP_MS   = 18
        STEPS_FWD = 6
        STEPS_BCK = 6

        def move_forward(step=0):
            if self.game_over:
                return
            if step < STEPS_FWD:
                nx = base_atk + direction * int(offset * (step + 1) / STEPS_FWD)
                atk_lbl.place(x=nx, y=self._sprite_y, anchor="n")
                j = self.after(STEP_MS, lambda: move_forward(step + 1))
                self._anim_jobs.append(j)
            else:
                # Impact — flash the hit sprite and screen
                _flash_hit()

        def _flash_hit():
            hit_lbl.config(bg="#ff4444")
            # Flash a thin color bar across the top of the battle area
            self._flash_overlay.config(bg=cfg["hit_color"])
            self._flash_overlay.place(x=0, y=0, width=self.W, height=8)
            self._flash_overlay.lift()
            j1 = self.after(80, lambda: _end_flash())
            self._anim_jobs.append(j1)

        def _end_flash():
            hit_lbl.config(bg=C_BG)
            self._flash_overlay.place(x=0, y=0, width=self.W, height=0)
            self._flash_overlay.lower()
            move_back()

        def move_back(step=0):
            if self.game_over:
                return
            if step < STEPS_BCK:
                nx = base_atk + direction * int(offset * (STEPS_BCK - step - 1) / STEPS_BCK)
                atk_lbl.place(x=nx, y=self._sprite_y, anchor="n")
                j = self.after(STEP_MS, lambda: move_back(step + 1))
                self._anim_jobs.append(j)
            else:
                # Snap back to base
                atk_lbl.place(x=base_atk, y=self._sprite_y, anchor="n")
                on_done()

        move_forward()

    def _play_hit_only_anim(self, defender_side, on_done):
        """
        For non-attack skills that still deal damage (e.g. drain, DoT).
        Defender shakes left-right briefly.
        """
        self._cancel_anims()
        hit_lbl  = self._p2_sprite if defender_side == "p2" else self._p1_sprite
        base_x   = self._p2_base_x if defender_side == "p2" else self._p1_base_x
        shakes   = [10, -10, 8, -8, 5, -5, 0]

        def shake(idx=0):
            if self.game_over:
                return
            if idx < len(shakes):
                hit_lbl.place(x=base_x + shakes[idx], y=self._sprite_y, anchor="n")
                j = self.after(30, lambda: shake(idx + 1))
                self._anim_jobs.append(j)
            else:
                hit_lbl.place(x=base_x, y=self._sprite_y, anchor="n")
                on_done()

        shake()

    # ── DISPLAY UPDATE ───────────────────────────────────────
    def _update_display(self):
        for side, char, fill, lbl, stat_lbl, bar_w in [
            ("p1", self.p1, self._p1_hp_fill, self._p1_hp_lbl, self._p1_stat_lbl, self._BAR_W),
            ("p2", self.p2, self._p2_hp_fill, self._p2_hp_lbl, self._p2_stat_lbl, self._BAR_W),
        ]:
            ratio = max(0.0, min(1.0, char.Hp / char.MaxHp))
            fill.place(width=max(0, int(bar_w * ratio)))
            if ratio > 0.5:
                fill.config(bg=C_P1 if side == "p1" else C_P2)
            elif ratio > 0.25:
                fill.config(bg="#ffaa00")
            else:
                fill.config(bg=C_RED)
            lbl.config(text=f"HP  {int(char.Hp)} / {char.MaxHp}")
            stat_lbl.config(text=self._get_unique_stat(char))

        self._refresh_sprite("p1", self.p1)
        self._refresh_sprite("p2", self.p2)

        for char, b_lbl, d_lbl in [
            (self.p1, self._p1_buffs_lbl, self._p1_debuffs_lbl),
            (self.p2, self._p2_buffs_lbl, self._p2_debuffs_lbl),
        ]:
            b_txt = "  ".join([f"[{k} {v}t]" for k, v in char.buffs.items()])
            d_txt = "  ".join([f"[{k} {v}t]" for k, v in char.debuffs.items()])
            b_lbl.config(text=b_txt if b_txt else "")
            d_lbl.config(text=d_txt if d_txt else "")

        if self.current_turn == 1:
            self._turn_lbl.config(
                text=f"▶  {self.p1_name}'s Turn  (Turn {self.turn_number})", fg=C_P1)
        else:
            self._turn_lbl.config(
                text=f"▶  {self.p2_name}'s Turn  (Turn {self.turn_number})", fg=C_P2)

        self._refresh_skill_buttons()

    def _get_unique_stat(self, char):
        name = char.Name
        if name == "Maruzen":
            return f"Sanity: {int(char.Sanity)}  |  Form: {char.Form}"
        elif name == "Zen":
            return f"Blood Rage: {int(char.blood_rage)}  |  Form: {char.Form}"
        elif name == "J.A.D.":
            return f"Ammo: {char.ammo} / 3  |  Form: {char.Form}"
        elif name == "Minos":
            return f"Luck: {char.luck}"
        return ""

    def _wrap_take_damage(self, char, tag):
        if not hasattr(char, "_orig_take_damage"):
            char._orig_take_damage = char.take_damage
        orig    = char._orig_take_damage
        log_buf = self._log_buffer

        def patched(dmg, enemy):
            hp_before = char.Hp
            orig(dmg, enemy)
            hp_after  = char.Hp
            actual    = hp_before - hp_after
            if actual > 0:
                buf_text = "".join(log_buf).lower()
                already  = any(k in buf_text for k in ("took", "damage", "dmg"))
                if not already:
                    log_buf.append(f"{char.Name} took {actual:.1f} damage!\n")

        char.take_damage = patched

    def _unwrap_take_damage(self, char):
        if hasattr(char, "_orig_take_damage"):
            char.take_damage = char._orig_take_damage
            del char._orig_take_damage

    def _refresh_sprite(self, side, char):
        lbl     = self._p1_sprite if side == "p1" else self._p2_sprite
        sprites = self._sprites[side]
        if char.Name == "Maruzen" and char.Form == "enraged":
            key = f"enraged_{side}"
        else:
            key = side
        if key in sprites:
            lbl.config(image=sprites[key])

    def _refresh_skill_buttons(self):
        current   = self.p1 if self.current_turn == 1 else self.p2
        char_name = current.Name
        form      = getattr(current, "Form", "normal")
        descs_map = SKILL_DESCS.get(char_name, {})
        descs     = descs_map.get(form) or descs_map.get("normal", [])

        active_color = C_P1 if self.current_turn == 1 else C_P2
        cd_color     = "#444455"

        for i, (btn, desc_lbl) in enumerate(zip(self._skill_btns, self._skill_descs)):
            skill_num  = i + 1
            cd         = current.cooldowns.get(skill_num, 0)
            skill_name, skill_desc = descs[i] if i < len(descs) else (f"Skill {skill_num}", "")
            btn_label  = skill_name.replace("\n", " ")

            if cd > 0:
                btn.config(text=f"  {btn_label}  (CD: {cd})",
                           bg=cd_color, fg="#888899", state="disabled")
                desc_lbl.config(text=skill_desc, fg="#888899")
            else:
                btn.config(text=f"  {btn_label}", bg=active_color, fg="white",
                           state="normal" if self.waiting_input else "disabled")
                desc_lbl.config(text=skill_desc, fg=C_GREY)

    # ── TIMER ────────────────────────────────────────────────
    def _start_timer(self):
        if self.game_over or self._paused:
            return
        if self.current_turn == 1:
            self.p1_time -= 1
            self._p1_timer_lbl.config(text=str(self.p1_time),
                                      fg=C_RED if self.p1_time <= 10 else C_P1)
            if self.p1_time <= 0:
                self._log("⏱  Player 1 ran out of time!", "p2")
                self._end_game(winner=2)
                return
        else:
            self.p2_time -= 1
            self._p2_timer_lbl.config(text=str(self.p2_time),
                                      fg=C_RED if self.p2_time <= 10 else C_P2)
            if self.p2_time <= 0:
                self._log("⏱  Player 2 ran out of time!", "p1")
                self._end_game(winner=1)
                return
        self._timer_job = self.after(1000, self._start_timer)

    def _stop_timer(self):
        if self._timer_job:
            self.after_cancel(self._timer_job)
            self._timer_job = None

    # ── PAUSE / RESUME ────────────────────────────────────────
    def _pause_game(self):
        """Halt the timer and disable skill buttons."""
        if self._paused or self.game_over:
            return
        self._paused = True
        self._stop_timer()
        # Dim skill buttons to signal paused state
        for btn in self._skill_btns:
            btn.config(state="disabled")
        self._turn_lbl.config(text="⏸  PAUSED", fg="#888899")
        from gui.MusicManager import music
        music.toggle_mute()

    def _resume_game(self):
        """Resume the timer and re-enable buttons if it was the player's turn."""
        if not self._paused or self.game_over:
            return
        self._paused = False
        self._start_timer()
        if self.waiting_input:
            self._refresh_skill_buttons()
        self._update_display()
        from gui.MusicManager import music
        if music.is_muted():
            music.toggle_mute()

    # ── SETTINGS PANEL ────────────────────────────────────────
    def _toggle_settings(self):
        if self.game_over:
            return
        if self._settings_panel and self._settings_panel.winfo_exists():
            self._close_settings()
        else:
            self._open_settings()

    def _open_settings(self):
        self._pause_game()

        PW, PH = min(460, self.W - 40), min(420, self.H - 40)
        panel  = Frame(self, bg=C_DARK, relief="flat", bd=0)
        panel.place(relx=0.5, rely=0.5, anchor="center", width=PW, height=PH)
        self._settings_panel = panel

        # Top colour stripe
        Frame(panel, bg=C_GOLD, height=4).pack(fill="x")

        # Title row
        title_row = Frame(panel, bg=C_DARK)
        title_row.pack(fill="x", padx=18, pady=(10, 4))
        Label(title_row, text="⚙  SETTINGS", font=("rainyhearts", 16, "bold"),
              fg=C_GOLD, bg=C_DARK).pack(side="left")
        Label(title_row, text="[ESC to close]", font=("rainyhearts", 9),
              fg="#444455", bg=C_DARK).pack(side="right")

        Frame(panel, bg="#2a2a3a", height=1).pack(fill="x", padx=18)

        # ── Turn timer section ────────────────────────────────
        Label(panel, text="Turn Timer  (seconds per player)",
              font=("rainyhearts", 11), fg=C_GREY, bg=C_DARK).pack(
              anchor="w", padx=20, pady=(14, 4))

        timer_row = Frame(panel, bg=C_DARK)
        timer_row.pack(fill="x", padx=20, pady=(0, 6))

        timer_var = IntVar(value=self._turn_duration)
        timer_lbl = Label(timer_row, text=str(self._turn_duration),
                          font=("rainyhearts", 22, "bold"),
                          fg="white", bg=C_DARK, width=4)
        timer_lbl.pack(side="left")

        def _update_timer_label(val):
            v = int(float(val))
            timer_var.set(v)
            timer_lbl.config(text=str(v))

        timer_slider = Scale(
            timer_row, from_=60, to=120, resolution=10,
            orient="horizontal", variable=timer_var,
            command=_update_timer_label,
            length=240, showvalue=False,
            bg=C_DARK, fg=C_GREY, troughcolor="#2a2a3a",
            highlightthickness=0, bd=0, sliderlength=14,
            activebackground=C_GOLD)
        timer_slider.pack(side="left", padx=10)

        Label(timer_row, text="60–120s",
              font=("rainyhearts", 9), fg="#444455", bg=C_DARK).pack(side="left")

        def _apply_timer():
            new_dur = timer_var.get()
            if new_dur == self._turn_duration:
                return
            self._turn_duration = new_dur
            # Apply to CURRENT player's remaining time — reset to new duration
            # so the change takes effect immediately next turn
            self.p1_time = new_dur
            self.p2_time = new_dur
            self._p1_timer_lbl.config(text=str(new_dur))
            self._p2_timer_lbl.config(text=str(new_dur))
            self._log(f"  ⚙  Turn timer set to {new_dur}s per player.", "system")

        Button(panel, text="Apply Timer",
               font=("rainyhearts", 10, "bold"),
               bg="#2a2a3a", fg=C_GOLD,
               activebackground="#3a3a4a", activeforeground=C_GOLD,
               relief="flat", bd=0, cursor="hand2",
               command=_apply_timer
               ).pack(anchor="w", padx=20, pady=(0, 10))

        Frame(panel, bg="#2a2a3a", height=1).pack(fill="x", padx=18)

        # ── Action buttons ────────────────────────────────────
        Label(panel, text="Actions",
              font=("rainyhearts", 11), fg=C_GREY, bg=C_DARK).pack(
              anchor="w", padx=20, pady=(12, 6))

        btn_cfg = dict(font=("rainyhearts", 12, "bold"),
                       relief="flat", bd=0, cursor="hand2",
                       padx=14, pady=6)

        act_row = Frame(panel, bg=C_DARK)
        act_row.pack(fill="x", padx=20, pady=(0, 6))

        Button(act_row, text="▶  Resume",
               bg="#1e3a1e", fg="#44cc44",
               activebackground="#2a4a2a", activeforeground="#44cc44",
               command=self._close_settings, **btn_cfg).pack(side="left", padx=(0, 8))

        Button(act_row, text="↺  Restart",
               bg="#2a1e1e", fg="#ff8844",
               activebackground="#3a2a2a", activeforeground="#ff8844",
               command=self._restart_battle, **btn_cfg).pack(side="left", padx=(0, 8))

        Button(act_row, text="⌂  Main Menu",
               bg="#1a1a2a", fg="#aaaacc",
               activebackground="#2a2a3a", activeforeground="white",
               command=self._quit_to_menu, **btn_cfg).pack(side="left")

        Frame(panel, bg="#2a2a3a", height=1).pack(fill="x", padx=18, pady=(8, 0))

        # ── Info row ──────────────────────────────────────────
        info_txt = (f"Turn {self.turn_number}  ·  "
                    f"{self.p1_name} {int(self.p1.Hp)}HP  vs  "
                    f"{self.p2_name} {int(self.p2.Hp)}HP")
        Label(panel, text=info_txt,
              font=("rainyhearts", 9), fg="#444455", bg=C_DARK).pack(
              anchor="w", padx=20, pady=(8, 0))

        # Bind Escape inside the panel too
        panel.bind("<Escape>", lambda e: self._close_settings())
        panel.focus_set()

    def _close_settings(self):
        if self._settings_panel and self._settings_panel.winfo_exists():
            self._settings_panel.destroy()
        self._settings_panel = None
        self._resume_game()
        self.focus_set()

    def _restart_battle(self):
        """Restart the current matchup from scratch."""
        if self._settings_panel and self._settings_panel.winfo_exists():
            self._settings_panel.destroy()
        self._settings_panel = None
        self._cancel_anims()
        self._stop_timer()
        self.game_over = False
        # Re-instantiate characters
        self.p1 = CHARACTER_MAP[self.p1_name]()
        self.p2 = CHARACTER_MAP[self.p2_name]()
        # Reset state
        self.current_turn  = 1
        self.turn_number   = 1
        self.waiting_input = False
        self._paused       = False
        self.p1_time       = self._turn_duration
        self.p2_time       = self._turn_duration
        self._p1_timer_lbl.config(text=str(self._turn_duration), fg=C_P1)
        self._p2_timer_lbl.config(text=str(self._turn_duration), fg=C_P2)
        # Re-enable skill buttons
        for btn in self._skill_btns:
            btn.config(state="disabled")
        # Clear the battle log
        self._battle_log.config(state="normal")
        self._battle_log.delete("1.0", "end")
        self._battle_log.config(state="disabled")
        self._log("↺  Battle restarted!", "system")
        self._update_display()
        self._start_timer()
        self.after(400, self._process_turn)
        self.focus_set()

    def _quit_to_menu(self):
        self._cancel_anims()
        self._stop_timer()
        if self._settings_panel and self._settings_panel.winfo_exists():
            self._settings_panel.destroy()
        self.controller.show_home()

    # ── TURN FLOW ────────────────────────────────────────────
    def _process_turn(self):
        if self.game_over or self._paused:
            return

        current = self.p1 if self.current_turn == 1 else self.p2
        enemy   = self.p2 if self.current_turn == 1 else self.p1
        tag     = "p1" if self.current_turn == 1 else "p2"

        # Reset the active player's clock to full duration each new turn
        if self.current_turn == 1:
            self.p1_time = self._turn_duration
            self._p1_timer_lbl.config(text=str(self.p1_time), fg=C_P1)
        else:
            self.p2_time = self._turn_duration
            self._p2_timer_lbl.config(text=str(self.p2_time), fg=C_P2)

        current.turn_counter += 1

        # ── FROZEN check — skip this turn entirely ────────────
        if current.has_debuff("Frozen"):
            current.debuffs["Frozen"] -= 1
            if current.debuffs["Frozen"] <= 0:
                del current.debuffs["Frozen"]
                self._log(f"  {current.Name} thawed out!", tag)
            else:
                self._log(f"  {current.Name} is frozen and cannot move! "
                          f"({current.debuffs['Frozen']} turns left)", tag)
            self._update_display()
            # Advance turn without any input or action
            self.current_turn = 2 if self.current_turn == 1 else 1
            if self.current_turn == 1:
                self.turn_number += 1
            self.after(800, self._process_turn)
            return
        
        # ── SLEEPING check — skip this turn entirely ──────────
        if current.has_buff("Sleeping"):
            current.buffs["Sleeping"] -= 1
            if current.buffs["Sleeping"] <= 0:
                del current.buffs["Sleeping"]
                self._log(f"  {current.Name} wakes up!", tag)
            else:
                self._log(f"  {current.Name} is sleeping and cannot move! "
                          f"({current.buffs['Sleeping']} turns left)", tag)
            self._update_display()
            # Advance turn without any input or action
            self.current_turn = 2 if self.current_turn == 1 else 1
            if self.current_turn == 1:
                self.turn_number += 1
            self.after(800, self._process_turn)
            return
        # ─────────────────────────────────────────────────────

        sys.stdout = self._log_capture
        current.check_transformation()
        sys.stdout = self._orig_stdout
        self._flush_capture(tag)

        self._update_display()
        self._log(f"── Turn {self.turn_number}  {current.Name} ──", tag)

        if self.mode == 1 and self.current_turn == 2:
            self.waiting_input = False
            self._refresh_skill_buttons()
            self.after(1200, lambda: self._bot_move(current, enemy))
        else:
            self.waiting_input = True
            self._refresh_skill_buttons()

    def _bot_move(self, bot, enemy):
        if self.game_over:
            return
        available = [i for i in range(1, 5) if bot.cooldowns.get(i, 0) == 0]
        move = random.choice(available) if available else 1
        self._execute_move(move, bot, enemy)

    def _on_skill_click(self, skill_num):
        if not self.waiting_input or self.game_over:
            return
        self.waiting_input = False
        for btn in self._skill_btns:
            btn.config(state="disabled")
        current = self.p1 if self.current_turn == 1 else self.p2
        enemy   = self.p2 if self.current_turn == 1 else self.p1
        self._execute_move(skill_num, current, enemy)

    def _execute_move(self, move, current, enemy):
        tag = "p1" if current is self.p1 else "p2"

        sys.stdout = self._log_capture
        move = current.debuff_checker(move, enemy)
        sys.stdout = self._orig_stdout
        self._flush_capture(tag)

        descs_map   = SKILL_DESCS.get(current.Name, {})
        form        = getattr(current, "Form", "normal")
        descs       = descs_map.get(form, descs_map.get("normal", []))
        skill_label = descs[move - 1][0].replace("\n", " ") if move - 1 < len(descs) else f"Skill {move}"
        self._log(f"  ➤  {current.Name} uses  {skill_label}", tag)

        # Decide which animation to play
        attacker_side = "p1" if current is self.p1 else "p2"
        defender_side = "p2" if attacker_side == "p1" else "p1"
        # Basic attacks (move 1) and most damage skills → full lunge
        # Buff-only skills → no anim needed, just execute
        is_damage_skill = move in (1, 2, 3, 4)  # All skills trigger anim; logic below refines

        def _do_execute():
            self._wrap_take_damage(self.p1, "p1")
            self._wrap_take_damage(self.p2, "p2")

            sys.stdout = self._log_capture
            result = current.use_skill(move, enemy)
            current.reduce_cooldowns()
            current.end_turn_checks()
            current.reduce_effects()
            enemy.end_of_round_effects(current)
            sys.stdout = self._orig_stdout

            self._unwrap_take_damage(self.p1)
            self._unwrap_take_damage(self.p2)

            self._flush_capture(tag)
            current.first_turn = False
            self._update_display()

            if not self.p1.is_alive():
                self.after(600, lambda: self._end_game(winner=2))
                return
            if not self.p2.is_alive():
                self.after(600, lambda: self._end_game(winner=1))
                return

            if result is True:
                self._log(f"  ★  {current.Name} gets a bonus turn!", tag)
                self.after(800, self._process_turn)
                return

            self.current_turn = 2 if self.current_turn == 1 else 1
            if self.current_turn == 1:
                self.turn_number += 1
            self.after(600, self._process_turn)

        # Snapshot HP before skill to decide anim type after
        enemy_hp_before = enemy.Hp

        # For move==1 (basic attack) always use lunge anim
        # For other moves, run execute first then check if damage was dealt → shake anim
        if move == 1:
            self._play_attack_anim(attacker_side, defender_side, _do_execute)
        else:
            # Play lunge for skills that typically deal damage; use hit-shake for the rest
            # We'll lunge for all damaging skills, then on_done will run _do_execute
            self._play_attack_anim(attacker_side, defender_side, _do_execute)

    # ── END GAME ─────────────────────────────────────────────
    def _end_game(self, winner):
        self._cancel_anims()
        self.game_over    = True
        self.waiting_input = False
        self._stop_timer()
        for btn in self._skill_btns:
            btn.config(state="disabled")

        if winner == 1:
            self._set_end_sprite("p1", self.p1, "win")
            self._set_end_sprite("p2", self.p2, "lose")
            winner_text  = f"🏆  {self.p1_name}  WINS!"
            winner_color = C_P1
        else:
            self._set_end_sprite("p1", self.p1, "lose")
            self._set_end_sprite("p2", self.p2, "win")
            winner_text  = f"🏆  {self.p2_name}  WINS!"
            winner_color = C_P2

        self._log("", "system")
        self._log(f"  {winner_text}", "system")

        banner = Frame(self, bg=C_DARK, relief="flat", bd=0)
        banner.place(relx=0.5, rely=0.5, anchor="center",
                     width=int(self.W * 0.42), height=int(self.H * 0.22))
        Frame(banner, bg=winner_color, height=5).pack(fill="x")
        Label(banner, text=winner_text, font=("rainyhearts", 26, "bold"),
              fg=winner_color, bg=C_DARK).pack(pady=(18, 6))
        Label(banner, text="Battle Over", font=("rainyhearts", 13),
              fg=C_GREY, bg=C_DARK).pack()
        Button(banner, text="Return to Menu",
               font=("rainyhearts", 13, "bold"),
               bg=winner_color, fg="white",
               activebackground=winner_color,
               relief="flat", cursor="hand2", bd=0,
               command=self.controller.show_home
               ).pack(pady=14, ipadx=16, ipady=6)

    def _set_end_sprite(self, side, char, outcome):
        sprites = self._sprites[side]
        if char.Name == "Maruzen" and char.Form == "enraged":
            key = f"enraged_{outcome}"
        else:
            key = outcome
        lbl = self._p1_sprite if side == "p1" else self._p2_sprite
        if key in sprites:
            lbl.config(image=sprites[key])


# ── stdout capture helper ─────────────────────────────────────
class _LogCapture(io.StringIO):
    def __init__(self, buf):
        super().__init__()
        self._buf = buf

    def write(self, s):
        self._buf.append(s)

    def flush(self):
        pass
