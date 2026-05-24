from tkinter import *
from PIL import Image, ImageTk, ImageOps, ImageDraw, ImageFont
import os
import sys
import random
import threading

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

def asset(path):
    return os.path.join(_ROOT, path)

from characters.Maruzensky import Maruzen
from characters.Zen import Zen
from characters.Devourer import Devourer
from characters.JAD import JAD
from characters.Giga import Giga
from characters.Minos import Minos
from characters.Pol import Pol
from characters.Sed import Sed

CHARACTER_MAP = {
    "Maruzen": Maruzen,
    "Zen": Zen,
    "Devourer": Devourer,
    "J.A.D.": JAD,
    "Giga": Giga,
    "Minos": Minos,
    "Pol": Pol,
    "Sed": Sed,
}

CHARACTER_ASSETS = {
    "Maruzen": {
        "p1": "Assets/Game characters/MaruzenAssets/Maruzen_player1.png",
        "p2": "Assets/Game characters/MaruzenAssets/Maruzen_player2.png",
        "win": "Assets/Game characters/MaruzenAssets/Maruzen_win.png",
        "lose": "Assets/Game characters/MaruzenAssets/Maruzen_lose.png",
        "enraged_p1": "Assets/Game characters/MaruzenAssets/enraged_player1.png",
        "enraged_p2": "Assets/Game characters/MaruzenAssets/enraged_player2.png",
        "enraged_win": "Assets/Game characters/MaruzenAssets/enraged_win.png",
        "enraged_lose": "Assets/Game characters/MaruzenAssets/enraged_lose.png",
    },
    "Zen": {
        "p1": "Assets/Game characters/ZenAssets/zen_p1.png",
        "p2": "Assets/Game characters/ZenAssets/zen_p2.png",
        "win": "Assets/Game characters/ZenAssets/zen_win.png",
        "lose": "Assets/Game characters/ZenAssets/zen_lose.png",
    },
    "J.A.D.": {
        "p1": "Assets/Game characters/JADAssets/JAD_p1.png",
        "p2": "Assets/Game characters/JADAssets/JAD_p2.png",
        "win": "Assets/Game characters/JADAssets/JAD_win.png",
        "lose": "Assets/Game characters/JADAssets/JAD_lose.png",
    },
    "Giga": {
        "p1": "Assets/Game characters/GigaAssets/Giga_p1.png",
        "p2": "Assets/Game characters/GigaAssets/Giga_p2.png",
        "win": "Assets/Game characters/GigaAssets/Giga_win.png",
        "lose": "Assets/Game characters/GigaAssets/Giga_lose.png",
    },
    "Minos": {
        "p1": "Assets/Game characters/MinosAssets/Minos_p1.png",
        "p2": "Assets/Game characters/MinosAssets/Minos_p2.png",
        "win": "Assets/Game characters/MinosAssets/Minos_win.png",
        "lose": "Assets/Game characters/MinosAssets/Minos_lose.png",
    },
    "Sed": {
        "p1": "Assets/Game characters/SedAssets/p1_sed.png",
        "p2": "Assets/Game characters/SedAssets/p2_sed.png",
        "win": "Assets/Game characters/SedAssets/win_sed.png",
        "lose": "Assets/Game characters/SedAssets/lose_sed.png",
    },
}

SKILL_DESCRIPTIONS = {
    "Maruzen": {
        "normal": {
            1: "Basic: Restore sanity, 10% bonus turn",
            2: "Heal last damage taken, -20 sanity",
            3: "Invincible for 2 turns, -30 sanity",
            4: "Deal sanity/2 damage, lose sanity/2",
        },
        "enraged": {
            1: "Payback: 1-3 hits, 5% MaxHP each",
            2: "Manipulation: Surrender chance",
            3: "Death Wish: 30+ damage based on sanity",
            4: "Sabotage: Block enemy skills 2 turns",
        }
    },
    "Zen": {
        "normal": {
            1: "Lost Cause: 0.2x ATK, +40 blood rage",
            2: "Silent Plead: Counter for 3 turns",
            3: "Death Slash: 1x ATK, halve blood rage",
            4: "Basic: 5 DMG or full ATK if enraged",
        }
    },
    "J.A.D.": {
        "Gun": {
            1: "Gunho: Clear enemy buffs & self debuffs",
            2: "Long Shot: 2 ammo, near-kill headshot",
            3: "Mist: 3 ammo, blind enemy 2 turns",
            4: "Basic: 0.3x ATK, -1 ammo",
        },
        "Hand": {
            1: "Gunho: Clear enemy buffs & self debuffs",
            2: "Backstab: 0.4x ATK",
            3: "Throat Cutter: 15% execute chance",
            4: "Basic: 0.2x ATK",
        }
    },
    "Giga": {
        "normal": {
            1: "Double Damage: Next attack 2x",
            2: "Invincible: Immune 2 turns",
            3: "Enhanced: Double stats 2 turns",
            4: "Basic: 0.5x ATK",
        }
    },
    "Minos": {
        "normal": {
            1: "Basic: 0.5x ATK",
            2: "Skill 1: Placeholder",
            3: "Skill 2: Placeholder",
            4: "Skill 3: Placeholder",
        }
    },
    "Sed": {
        "normal": {
            1: "Basic: 0.5x ATK",
            2: "Skill 1: Placeholder",
            3: "Skill 2: Placeholder",
            4: "Skill 3: Placeholder",
        }
    },
    "Pol": {
        "normal": {
            1: "Basic: 0.5x ATK",
            2: "Skill 1: Placeholder",
            3: "Skill 2: Placeholder",
            4: "Skill 3: Placeholder",
        }
    },
    "Devourer": {
        "normal": {
            1: "Basic: 0.5x ATK",
            2: "Skill 1: Placeholder",
            3: "Skill 2: Placeholder",
            4: "Skill 3: Placeholder",
        }
    },
}

C_BG = "#ffffff"
C_PANEL = "#f0f0f0"
C_P1 = "#3399ff"
C_P2 = "#ff4444"
C_GOLD = "#ffd700"
C_DARK = "#1a1a2e"
C_GREY = "#666666"


def preload_battle_assets_bg(p1_name, p2_name, sprite_h):
    result = {"p1": {}, "p2": {}}
    
    for player, char_name in [("p1", p1_name), ("p2", p2_name)]:
        assets = CHARACTER_ASSETS.get(char_name, {})
        for state in ["p1", "p2", "win", "lose"]:
            path = assets.get(state)
            if path and os.path.exists(asset(path)):
                try:
                    img = Image.open(asset(path)).convert("RGBA")
                    img.thumbnail((int(sprite_h * 0.8), sprite_h), Image.Resampling.LANCZOS)
                    result[player][state] = img
                except Exception as e:
                    print(f"Error loading {path}: {e}")
        
        if char_name == "Maruzen":
            for state in ["enraged_p1", "enraged_p2", "enraged_win", "enraged_lose"]:
                path = assets.get(state)
                if path and os.path.exists(asset(path)):
                    try:
                        img = Image.open(asset(path)).convert("RGBA")
                        img.thumbnail((int(sprite_h * 0.8), sprite_h), Image.Resampling.LANCZOS)
                        result[player][state] = img
                    except Exception as e:
                        print(f"Error loading {path}: {e}")
    
    return result


class BattleScene(Frame):
    def __init__(self, master, controller, mode, p1_name, p2_name, preloaded=None):
        super().__init__(master, bg=C_BG)
        self.place(relwidth=1, relheight=1)
        
        self.controller = controller
        self.mode = mode
        self.p1_name = p1_name
        self.p2_name = p2_name
        
        self.p1 = CHARACTER_MAP[p1_name]()
        self.p2 = CHARACTER_MAP[p2_name]()
        
        self.current_turn = 1
        self.turn_number = 1
        self.game_over = False
        self.waiting_for_input = False
        
        self.p1_time = 60
        self.p2_time = 60
        self.timer_job = None
        
        self._sprites = {"p1": {}, "p2": {}}
        self._img_refs = {}
        
        self.update_idletasks()
        self.W = master.winfo_width() or 1280
        self.H = master.winfo_height() or 720
        
        self._build_ui()
        
        if preloaded:
            self._convert_sprites(preloaded)
        
        self._update_display()
        self._start_timer()
        
        self.after(500, self._process_turn)
    
    def _build_ui(self):
        W, H = self.W, self.H
        
        top_h = max(80, int(H * 0.12))
        top = Frame(self, bg=C_DARK)
        top.place(x=0, y=0, width=W, height=top_h)
        
        p1_w = int(W * 0.35)
        Label(top, text="PLAYER 1", font=("rainyhearts", 12, "bold"),
              fg=C_P1, bg=C_DARK).place(x=20, y=10)
        self._p1_timer_lbl = Label(top, text="60", font=("rainyhearts", 20, "bold"),
                                    fg=C_P1, bg=C_DARK)
        self._p1_timer_lbl.place(x=20, y=35)
        
        self._p1_hp_bg = Frame(top, bg="#333333")
        self._p1_hp_bg.place(x=100, y=20, width=p1_w - 120, height=30)
        self._p1_hp_bar = Frame(top, bg=C_P1)
        self._p1_hp_bar.place(x=100, y=20, width=p1_w - 120, height=30)
        self._p1_hp_lbl = Label(top, text="", font=("Arial", 10, "bold"),
                                fg="white", bg=C_P1)
        self._p1_hp_lbl.place(x=100, y=20, width=p1_w - 120, height=30)
        
        Label(top, text="VS", font=("rainyhearts", 18, "bold"),
              fg=C_GOLD, bg=C_DARK).place(x=W//2, y=top_h//2, anchor="center")
        
        p2_x = W - p1_w
        Label(top, text="PLAYER 2", font=("rainyhearts", 12, "bold"),
              fg=C_P2, bg=C_DARK).place(x=p2_x + 20, y=10)
        self._p2_timer_lbl = Label(top, text="60", font=("rainyhearts", 20, "bold"),
                                    fg=C_P2, bg=C_DARK)
        self._p2_timer_lbl.place(x=p2_x + 20, y=35)
        
        self._p2_hp_bg = Frame(top, bg="#333333")
        self._p2_hp_bg.place(x=p2_x + 100, y=20, width=p1_w - 120, height=30)
        self._p2_hp_bar = Frame(top, bg=C_P2)
        self._p2_hp_bar.place(x=p2_x + 100, y=20, width=p1_w - 120, height=30)
        self._p2_hp_lbl = Label(top, text="", font=("Arial", 10, "bold"),
                                fg="white", bg=C_P2)
        self._p2_hp_lbl.place(x=p2_x + 100, y=20, width=p1_w - 120, height=30)
        
        sprite_y = top_h + 20
        sprite_h = int(H * 0.45)
        
        self._p1_sprite = Label(self, bg=C_BG)
        self._p1_sprite.place(x=int(W * 0.15), y=sprite_y, anchor="center")
        
        self._p2_sprite = Label(self, bg=C_BG)
        self._p2_sprite.place(x=int(W * 0.85), y=sprite_y, anchor="center")
        
        turn_y = sprite_y + sprite_h - 50
        self._turn_lbl = Label(self, text="PLAYER 1'S TURN",
                               font=("rainyhearts", 16, "bold"),
                               fg=C_P1, bg=C_BG)
        self._turn_lbl.place(x=W//2, y=turn_y, anchor="center")
        
        buff_y = sprite_y + sprite_h + 10
        buff_h = max(60, int(H * 0.08))
        
        self._p1_effects = Label(self, text="", font=("Arial", 9),
                                 fg=C_GREY, bg=C_BG, justify="left",
                                 wraplength=int(W * 0.35))
        self._p1_effects.place(x=int(W * 0.05), y=buff_y, width=int(W * 0.35), height=buff_h)
        
        self._p2_effects = Label(self, text="", font=("Arial", 9),
                                 fg=C_GREY, bg=C_BG, justify="right",
                                 wraplength=int(W * 0.35))
        self._p2_effects.place(x=int(W * 0.6), y=buff_y, width=int(W * 0.35), height=buff_h)
        
        log_y = buff_y + buff_h + 10
        log_h = max(80, int(H * 0.12))
        log_frame = Frame(self, bg=C_PANEL)
        log_frame.place(x=int(W * 0.1), y=log_y, width=int(W * 0.8), height=log_h)
        
        self._battle_log = Text(log_frame, font=("Arial", 9), bg=C_PANEL,
                                fg=C_DARK, wrap="word", state="disabled",
                                relief="flat", height=4)
        self._battle_log.pack(fill="both", expand=True, padx=5, pady=5)
        
        btn_y = H - 100
        btn_w = 180
        btn_h = 70
        gap = 15
        total_w = 4 * btn_w + 3 * gap
        start_x = (W - total_w) // 2
        
        self._skill_btns = []
        for i in range(4):
            btn = Button(self, text=f"Skill {i+1}", font=("rainyhearts", 10, "bold"),
                        bg=C_DARK, fg="white", relief="raised", bd=2,
                        cursor="hand2", state="disabled",
                        command=lambda idx=i+1: self._on_skill_click(idx))
            btn.place(x=start_x + i * (btn_w + gap), y=btn_y, width=btn_w, height=btn_h)
            self._skill_btns.append(btn)
    
    def _convert_sprites(self, preloaded):
        for player in ["p1", "p2"]:
            for state, pil_img in preloaded[player].items():
                self._sprites[player][state] = ImageTk.PhotoImage(pil_img)
    
    def _log(self, message):
        self._battle_log.config(state="normal")
        self._battle_log.insert("end", message + "\n")
        self._battle_log.see("end")
        self._battle_log.config(state="disabled")
    
    def _update_display(self):
        # Update HP bars
        p1_ratio = max(0, self.p1.Hp / self.p1.MaxHp)
        p2_ratio = max(0, self.p2.Hp / self.p2.MaxHp)
        
        p1_w = int((self.W * 0.35 - 120) * p1_ratio)
        p2_w = int((self.W * 0.35 - 120) * p2_ratio)
        
        self._p1_hp_bar.place(width=max(0, p1_w))
        self._p2_hp_bar.place(width=max(0, p2_w))
        
        self._p1_hp_lbl.config(text=f"{int(self.p1.Hp)}/{self.p1.MaxHp}")
        self._p2_hp_lbl.config(text=f"{int(self.p2.Hp)}/{self.p2.MaxHp}")
        
        self._update_sprite("p1", self.p1)
        self._update_sprite("p2", self.p2)
        
        p1_buffs = ", ".join([f"{k}({v})" for k, v in self.p1.buffs.items()]) or "None"
        p1_debuffs = ", ".join([f"{k}({v})" for k, v in self.p1.debuffs.items()]) or "None"
        self._p1_effects.config(text=f"Buffs: {p1_buffs}\nDebuffs: {p1_debuffs}")
        
        p2_buffs = ", ".join([f"{k}({v})" for k, v in self.p2.buffs.items()]) or "None"
        p2_debuffs = ", ".join([f"{k}({v})" for k, v in self.p2.debuffs.items()]) or "None"
        self._p2_effects.config(text=f"Buffs: {p2_buffs}\nDebuffs: {p2_debuffs}")
        
        if self.current_turn == 1:
            self._turn_lbl.config(text=f"PLAYER 1'S TURN (Turn {self.turn_number})", fg=C_P1)
        else:
            self._turn_lbl.config(text=f"PLAYER 2'S TURN (Turn {self.turn_number})", fg=C_P2)
        
        current_player = self.p1 if self.current_turn == 1 else self.p2
        for i, btn in enumerate(self._skill_btns):
            skill_num = i + 1
            cd = current_player.cooldowns.get(skill_num, 0)
            
            desc = self._get_skill_desc(current_player, skill_num)
            
            if cd > 0:
                btn.config(text=f"Skill {skill_num}\n(CD: {cd})\n{desc}",
                          state="disabled", bg="#555555")
            else:
                btn.config(text=f"Skill {skill_num}\n{desc}",
                          state="normal", bg=C_DARK)
    
    def _get_skill_desc(self, player, skill_num):
        char_name = player.Name
        form = getattr(player, "Form", "normal")
        
        descs = SKILL_DESCRIPTIONS.get(char_name, {})
        form_descs = descs.get(form, descs.get("normal", {}))
        
        return form_descs.get(skill_num, "")
    
    def _update_sprite(self, player_side, character):
        sprite_lbl = self._p1_sprite if player_side == "p1" else self._p2_sprite
        sprites = self._sprites[player_side]
        
        if character.Name == "Maruzen" and character.Form == "enraged":
            state = f"enraged_{player_side}"
        else:
            state = player_side
        
        if state in sprites:
            sprite_lbl.config(image=sprites[state])
    
    def _start_timer(self):
        if self.game_over:
            return
        
        if self.current_turn == 1:
            self.p1_time -= 1
            self._p1_timer_lbl.config(text=str(self.p1_time))
            if self.p1_time <= 0:
                self._log("Player 1 ran out of time!")
                self._end_game(winner=2)
                return
        else:
            self.p2_time -= 1
            self._p2_timer_lbl.config(text=str(self.p2_time))
            if self.p2_time <= 0:
                self._log("Player 2 ran out of time!")
                self._end_game(winner=1)
                return
        
        self.timer_job = self.after(1000, self._start_timer)
    
    def _process_turn(self):
        if self.game_over:
            return
        
        current = self.p1 if self.current_turn == 1 else self.p2
        enemy = self.p2 if self.current_turn == 1 else self.p1
        
        current.turn_counter += 1
        current.check_transformation()
        
        self._log(f"\n=== Turn {self.turn_number} - {current.Name}'s turn ===")
        self._log(current.stats())
        
        self._update_display()
        
        if self.mode == 1 and self.current_turn == 2:
            self.after(1500, lambda: self._bot_move(current, enemy))
        else:
            self.waiting_for_input = True
            for btn in self._skill_btns:
                if current.cooldowns.get(self._skill_btns.index(btn) + 1, 0) == 0:
                    btn.config(state="normal")
    
    def _bot_move(self, bot, enemy):
        available = [i for i in range(1, 5) if bot.cooldowns.get(i, 0) == 0]
        if available:
            move = random.choice(available)
            self._execute_move(move, bot, enemy)
    
    def _on_skill_click(self, skill_num):
        if not self.waiting_for_input or self.game_over:
            return
        
        current = self.p1 if self.current_turn == 1 else self.p2
        enemy = self.p2 if self.current_turn == 1 else self.p1
        
        for btn in self._skill_btns:
            btn.config(state="disabled")
        
        self.waiting_for_input = False
        self._execute_move(skill_num, current, enemy)
    
    def _execute_move(self, move, current, enemy):
        self._log(f"{current.Name} uses Skill {move}!")
        
        move = current.debuff_checker(move, enemy)
        
        result = current.use_skill(move, enemy)
        
        current.reduce_cooldowns()
        
        current.end_turn_checks()
        current.reduce_effects()
        
        enemy.end_of_round_effects(current)
        
        current.first_turn = False
        
        self._update_display()
        
        if not self.p1.is_alive():
            self.after(1000, lambda: self._end_game(winner=2))
            return
        elif not self.p2.is_alive():
            self.after(1000, lambda: self._end_game(winner=1))
            return
        
        if result is True:
            self._log(f"{current.Name} gets a bonus turn!")
            self.after(1000, self._process_turn)
        else:
            self.current_turn = 2 if self.current_turn == 1 else 1
            if self.current_turn == 1:
                self.turn_number += 1
            self.after(1500, self._process_turn)
    
    def _end_game(self, winner):
        """End the game and show winner"""
        self.game_over = True
        if self.timer_job:
            self.after_cancel(self.timer_job)
        
        # Update sprites to win/lose
        if winner == 1:
            if "win" in self._sprites["p1"]:
                self._p1_sprite.config(image=self._sprites["p1"]["win"])
            if "lose" in self._sprites["p2"]:
                self._p2_sprite.config(image=self._sprites["p2"]["lose"])
            winner_text = "PLAYER 1 WINS!"
            winner_color = C_P1
        else:
            if "lose" in self._sprites["p1"]:
                self._p1_sprite.config(image=self._sprites["p1"]["lose"])
            if "win" in self._sprites["p2"]:
                self._p2_sprite.config(image=self._sprites["p2"]["win"])
            winner_text = "PLAYER 2 WINS!"
            winner_color = C_P2
        
        self._log(f"\n{'='*40}\n{winner_text}\n{'='*40}")
        
        # Show winner banner
        banner = Frame(self, bg=C_DARK, relief="raised", bd=5)
        banner.place(relx=0.5, rely=0.5, anchor="center", width=500, height=200)
        
        Label(banner, text=winner_text, font=("rainyhearts", 28, "bold"),
              fg=winner_color, bg=C_DARK).pack(pady=30)
        
        Button(banner, text="Return to Menu", font=("rainyhearts", 14),
               bg=winner_color, fg="white", cursor="hand2",
               command=self.controller.show_home).pack(pady=10)
