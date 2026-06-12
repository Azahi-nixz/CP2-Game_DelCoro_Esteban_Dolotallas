# 🎮 Blu Room Battlefield (BrB)

A competitive turn-based battle game featuring 11 unique characters with distinct abilities, built with Python and Tkinter.

## 🌟 Features

### Game Mechanics
- **Turn-based Combat System** - Strategic gameplay with attack, defend, and special ability options
- **11 Unique Characters** - Each with custom stats, special abilities, and visual assets
- **Three Game Modes**:
  - **PvP (Player vs Player)** - Battle against a friend locally
  - **PvE (Player vs Bot)** - Face off against AI opponents
  - **Bot vs Bot** - Watch AI battles unfold
- **Dynamic Combat**:
  - Normal attacks with critical hit chances
  - Defensive stance to reduce incoming damage
  - Character-specific special abilities
  - Real-time health tracking

### Quality of Life Features
- **In-Game Settings Menu**:
  - Pause/Resume functionality
  - Restart match option
  - Adjustable match timer (60s, 90s, 120s)
- **Complete Character Selection** with visual previews
- **How to Play Guide** - Built-in tutorial system
- **Professional UI** with custom graphics and animations
- **Music & Sound** - Immersive audio experience

## 📦 Installation

### Option 1: Download Windows Executable (Recommended)
1. Go to [Releases](https://github.com/Azahi-nixz/CP2-Game_DelCoro_Esteban_Dolotallas/releases)
2. Download `BluRoomBattlefield_v1.0.0_Windows.zip`
3. Extract the ZIP file
4. Run `BluRoomBattlefield.exe`
5. Play!

**No Python installation required!**

### Option 2: Run from Source
```bash
# Clone the repository
git clone https://github.com/Azahi-nixz/CP2-Game_DelCoro_Esteban_Dolotallas.git
cd CP2-Game_DelCoro_Esteban_Dolotallas

# Install dependencies
pip install -r requirements.txt

# Run the game
python Main.py
```

## 🎯 Character Roster

The game features 11 unique characters, each with their own:
- **Custom Stats** - HP, Attack, Defense, and Speed
- **Special Abilities** - Unique powers that can turn the tide of battle
- **Visual Design** - Multiple sprite states (idle, win, lose)
- **Strategic Playstyles** - From tanks to glass cannons

### Featured Characters:
- **Devourer** - High damage dealer
- **Emberload** - Balanced fighter
- **Enzo** - Speed specialist
- **Giga** - Tank with high HP
- **JAD** - Technical fighter
- **Maruzen** - Strategic character with rage mode
- **Minos** - Heavy hitter
- **Pol** - Defensive specialist
- **Russel** - Versatile combatant
- **Sed** - Control-focused character
- **Zen** - Precision striker

## 🎮 How to Play

1. **Main Menu**:
   - Select game mode (PvP, PvE, or Bot vs Bot)
   - Access How to Play guide
   - Exit game

2. **Character Selection**:
   - Player 1 selects their character
   - Player 2 (or bot) selects their character
   - Review character previews

3. **Battle Phase**:
   - **Attack** - Deal damage to opponent
   - **Defend** - Reduce incoming damage
   - **Special** - Use unique character ability
   - Watch the timer - Make decisions quickly!

4. **In-Game Settings**:
   - Press "Settings" during battle
   - Pause the game
   - Adjust match timer
   - Restart or continue

5. **Victory Conditions**:
   - Reduce opponent's HP to 0
   - Have more HP when timer runs out

## 🛠️ Technical Details

### Built With
- **Python 3.13**
- **Tkinter** - GUI framework
- **Pillow (PIL)** - Image processing
- **Pygame** - Audio handling
- **PyInstaller** - Executable creation

### Project Structure
```
CP2-brb/
├── Main.py                 # Entry point
├── characters/             # Character classes
│   ├── Characters.py       # Base character class
│   ├── Devourer.py
│   ├── Giga.py
│   └── ... (other characters)
├── gui/                    # UI components
│   ├── Interface.py        # Main menu
│   ├── CharacterSelect.py  # Character selection screen
│   ├── BattleScene.py      # Combat interface
│   ├── Guides.py           # Tutorial system
│   ├── FontLoader.py       # Font management
│   └── MusicManager.py     # Audio system
└── Assets/                 # Graphics and audio
    ├── Game characters/    # Character sprites
    ├── Music/             # Background music
    └── Fonts/             # Custom fonts
```

### System Requirements
- **OS**: Windows 10/11
- **RAM**: 4GB minimum
- **Storage**: 150MB free space
- **Display**: 1280x720 minimum resolution

## 🚀 Development

### Setting Up Development Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run in development mode
python Main.py
```

### Building Executable
```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller BluRoomBattlefield.spec

# Find executable in dist/ folder
```

## 📝 Version History

### v1.0.0 (Current)
- ✅ 11 playable characters
- ✅ Complete GUI system
- ✅ PvP, PvE, and Bot vs Bot modes
- ✅ In-game settings menu
- ✅ Adjustable match timer
- ✅ Pause/Resume functionality
- ✅ Professional asset integration
- ✅ Music and sound effects
- ✅ Windows executable build

## 👥 Credits 
**Project**: CP2 - Game Development  
**Course**: Computer Programming 2  

### Special Thanks
- Character art and design contributors
- Music and sound effect sources
- Beta testers and feedback providers

## 📄 License

This project is developed as part of academic coursework.

## 🐛 Known Issues

- First-run Windows SmartScreen warning (normal for unsigned .exe files)
- Timer adjustment requires game restart to take effect

## 🤝 Contributing

This is an academic project, but feedback and suggestions are welcome!

## 📧 Contact

For questions, issues, or feedback:
- GitHub: [@Azahi-nixz](https://github.com/Azahi-nixz)
- Repository: [CP2-Game_DelCoro_Esteban_Dolotallas](https://github.com/Azahi-nixz/CP2-Game_DelCoro_Esteban_Dolotallas)

---

**Enjoy the battle! May the best fighter win! 🏆**
