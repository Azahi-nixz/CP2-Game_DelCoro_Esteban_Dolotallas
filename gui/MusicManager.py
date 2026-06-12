

import os

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

try:
    import pygame
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
    pygame.mixer.init()
    _PYGAME_OK = True
except Exception as e:
    print(f"[MusicManager] pygame unavailable – music disabled. ({e})")
    _PYGAME_OK = False

_SUPPORTED_EXT = (".ogg", ".mp3", ".wav", ".flac")

_SLOT_FILES = {
    "menu":   ["menu.ogg",   "menu.mp3",   "default.mp3"],
    "select": ["select.ogg", "select.mp3", "default.mp3"],
    "battle": ["battle.ogg", "battle.mp3", "default.mp3"],
}


def _slot_path(filename: str) -> str:
    return os.path.join(_ROOT, "Assets", "Music", filename)


class _MusicManager:
    def __init__(self):
        self._volume      = 0.5
        self._pre_mute    = 0.5
        self._paused      = False
        self._current     = None
        self._custom_path = None
        self._custom_name = None

    # ── internal ─────────────────────────────────────────────
    def _load_and_play(self, path: str, key: str, fadein_ms: int = 1000):
        """Load a file and start looping it."""
        if not _PYGAME_OK:
            return False
        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(self._volume)
            pygame.mixer.music.play(loops=-1, fade_ms=fadein_ms)
            self._current = key
            self._paused  = False
            return True
        except Exception as e:
            print(f"[MusicManager] Cannot play {path}: {e}")
            return False

    # ── slot playback ─────────────────────────────────────────
    def _play_slot(self, slot: str, fadein_ms: int = 1000):
        # If a custom track is active, keep it playing across screens
        if self._custom_path and os.path.exists(self._custom_path):
            if self._current == f"custom:{self._custom_path}":
                return   # custom track already running — don't interrupt
        if self._current == slot and not self._paused:
            return       # same slot already looping — don't restart
        for fname in _SLOT_FILES.get(slot, []):
            path = _slot_path(fname)
            if os.path.exists(path):
                self._load_and_play(path, slot, fadein_ms)
                return
        # File missing — silence
        self._current = None

    def play_menu(self):
        self._play_slot("menu")

    def play_select(self):
        self._play_slot("select")

    def play_battle(self):
        self._play_slot("battle")

    # ── custom track ──────────────────────────────────────────
    def load_custom(self, path: str):
        if not _PYGAME_OK:
            return False
        if not os.path.isfile(path):
            print(f"[MusicManager] File not found: {path}")
            return False
        ext = os.path.splitext(path)[1].lower()
        if ext not in _SUPPORTED_EXT:
            print(f"[MusicManager] Unsupported format: {ext}")
            return False
        self._custom_path = path
        self._custom_name = os.path.basename(path)
        return self._load_and_play(path, f"custom:{path}")

    def clear_custom(self):
        self._custom_path = None
        self._custom_name = None
        self._current     = None

    def get_custom_name(self):
        return self._custom_name

    def has_custom(self) -> bool:
        return self._custom_path is not None

    # ── volume / pause ────────────────────────────────────────
    def set_volume(self, vol: float):
        self._volume = max(0.0, min(1.0, vol))
        if _PYGAME_OK and not self._paused:
            pygame.mixer.music.set_volume(self._volume)

    def get_volume(self) -> float:
        return self._volume

    def toggle_mute(self):
        """Pause or unpause playback."""
        if not _PYGAME_OK:
            return
        if self._paused:
            pygame.mixer.music.unpause()
            pygame.mixer.music.set_volume(self._volume)
            self._paused = False
        else:
            self._volume_before_pause = pygame.mixer.music.get_volume()
            pygame.mixer.music.pause()
            self._paused = True

    def is_muted(self) -> bool:
        return self._paused

    def stop(self, fadeout_ms: int = 500):
        if not _PYGAME_OK:
            return
        pygame.mixer.music.fadeout(fadeout_ms)
        self._current = None
        self._paused  = False

    # ── file browser helper ───────────────────────────────────
    @staticmethod
    def scan_music_folder() -> list[str]:
        """Return list of full paths for all audio files in Assets/Music/."""
        folder = os.path.join(_ROOT, "Assets", "Music")
        if not os.path.isdir(folder):
            return []
        return sorted(
            os.path.join(folder, f)
            for f in os.listdir(folder)
            if os.path.splitext(f)[1].lower() in _SUPPORTED_EXT
        )


music = _MusicManager()
