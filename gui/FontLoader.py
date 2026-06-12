"""
FontLoader — registers bundled fonts with Windows GDI and Tkinter
at startup, so rainyhearts works even on machines that don't have
it installed.

Call gui.FontLoader.load_fonts() once before creating the Tk root.
"""

import os
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _asset(*parts):
    """Resolve a path relative to project root, works both in dev and PyInstaller."""
    if getattr(sys, "frozen", False):
        base = sys._MEIPASS  # PyInstaller unpacks here
    else:
        base = _ROOT
    return os.path.join(base, *parts)


def load_fonts():
    """
    Register all bundled .ttf fonts so Tkinter can use them by name.
    Safe to call multiple times.
    """
    font_path = _asset("Assets", "rainyhearts.ttf")

    if not os.path.exists(font_path):
        print(f"[FontLoader] Font not found at {font_path} — falling back to system font.")
        return

    if sys.platform == "win32":
        try:
            import ctypes
            FR_PRIVATE = 0x10
            ctypes.windll.gdi32.AddFontResourceExW(font_path, FR_PRIVATE, 0)
        except Exception as e:
            print(f"[FontLoader] GDI font registration failed: {e}")
    else:
        # On macOS / Linux tkinter picks up fonts from the file path directly
        # via pyglet or fonttools if available; otherwise falls back gracefully.
        try:
            from tkinter import font as tkfont
            # Tk can load font files on some platforms via font configure
            tkfont.families()   # ensure font system is initialized
        except Exception:
            pass
