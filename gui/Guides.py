from tkinter import Toplevel, Tk, Label, Text, Scrollbar, Frame, END, BOTH, RIGHT, Y
import os

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_GUIDES_PATH = os.path.join(_ROOT, "gui", "Guides.txt")


def guide():
    # Always open as a Toplevel over the existing root window
    try:
        root = Tk._default_root
        if root is None:
            raise RuntimeError("No root window")
        win = Toplevel(root)
    except Exception:
        # Fallback: standalone window (e.g. run directly)
        win = Tk()

    win.title("Guides — Bluroom Battlefield")
    win.geometry("860x680")
    win.configure(bg="#0a0a0f")
    win.resizable(True, True)

    # ── header ───────────────────────────────────────────────
    Label(win, text="CHARACTER GUIDES",
          font=("rainyhearts", 22, "bold"),
          fg="#3399ff", bg="#0a0a0f").pack(pady=(16, 4))
    Frame(win, bg="#3399ff", height=2).pack(fill="x", padx=40, pady=(0, 10))

    # ── scrollable text area ─────────────────────────────────
    container = Frame(win, bg="#0a0a0f")
    container.pack(fill=BOTH, expand=True, padx=20, pady=(0, 16))

    scrollbar = Scrollbar(container)
    scrollbar.pack(side=RIGHT, fill=Y)

    text_area = Text(
        container,
        font=("Consolas", 11),
        bg="#10101a", fg="#ccccdd",
        wrap="word",
        padx=18, pady=14,
        relief="flat", bd=0,
        yscrollcommand=scrollbar.set,
        state="normal",
    )
    text_area.pack(fill=BOTH, expand=True)
    scrollbar.config(command=text_area.yview)

    # ── load content ─────────────────────────────────────────
    try:
        with open(_GUIDES_PATH, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        content = f"[Guide file not found at {_GUIDES_PATH}]"
    except Exception as e:
        content = f"[Error reading guide: {e}]"

    # Basic formatting: bold "Character -" lines
    text_area.tag_config("header",  foreground="#ffd700", font=("rainyhearts", 14, "bold"))
    text_area.tag_config("skill",   foreground="#88ccff", font=("Consolas", 11, "bold"))
    text_area.tag_config("passive", foreground="#88ffcc", font=("Consolas", 11, "italic"))
    text_area.tag_config("normal",  foreground="#ccccdd")

    for line in content.splitlines(keepends=True):
        stripped = line.strip()
        if stripped.startswith("Character -") or stripped.startswith("Character–"):
            text_area.insert(END, "\n" + line, "header")
        elif stripped.startswith("Skill") or stripped.startswith("Basic attack"):
            text_area.insert(END, line, "skill")
        elif stripped.startswith("Passive"):
            text_area.insert(END, line, "passive")
        else:
            text_area.insert(END, line, "normal")

    text_area.config(state="disabled")

    # ── do NOT call mainloop() — let the parent window own the loop ──
    win.focus_set()
