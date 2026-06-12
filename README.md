# Blu Room Battlefield v1.0.0

**Enterprise-grade turn-based fighting game featuring 11 unique characters!**

## 🎮 What's New in v1.0.0

### Major Features
- ✅ **Fixed Bot AI Selection** - Bot now correctly selects a random character instead of mirroring player choice
- ✅ **In-Game Settings Panel** - Press `ESC` or click ⚙ button during battle
- ✅ **Configurable Turn Timer** - Adjust timer from 60-120 seconds per player
- ✅ **Pause/Resume System** - Pause the game anytime during battle
- ✅ **Battle Restart** - Restart current matchup without returning to menu
- ✅ **Enhanced UI/UX** - Professional visual design and smooth animations

### Game Modes
- **1 Player** - Battle against AI opponent (selects random character)
- **2 Player** - Local PvP with timer-based turns

### Characters (11 Total)
1. **Maruzen** - Sanity-driven brawler with Enraged transformation
2. **Zen** - Blood Rage swordsman with high damage potential
3. **Devourer** - Immortal life-draining predator
4. **J.A.D.** - Gun & blade duelist with ammo management
5. **Giga** - Armored tank with damage reflection
6. **Minos** - Luck-based wildcard fighter
7. **Pol** - Wind warrior with speed-scaled attacks
8. **Sed** - War maiden with Excalibur mode
9. **Russelle** - Iron sleeper with revival mechanic
10. **Sol Emberload** - Living flame that burns everything
11. **Hotori** - Time manipulator with freeze abilities

## 🎯 Controls

### Battle Controls
- **Mouse Click** - Select skills (4 skills per character)
- **ESC** - Open settings/pause menu
- **Skill Buttons** - Use character abilities (cooldown system)

### Navigation
- **Arrow Keys** - Navigate character select grid
- **Enter** - Confirm selection
- **ESC** - Go back

## ⚙️ Settings Panel (In-Game)

Access during battle by pressing `ESC` or clicking the ⚙ icon.

### Timer Configuration
- Adjust turn duration: 60-120 seconds
- Applies to both players
- Changes take effect immediately

### Actions
- **Resume** - Continue the battle
- **Restart** - Start over with same characters
- **Main Menu** - Return to main menu

## 🛠️ Technical Details

- **Engine**: Python 3.8+ with Tkinter
- **Graphics**: PIL/Pillow for image processing
- **Audio**: pygame mixer for background music
- **Resolution**: Responsive (1280x720 default)

## 📦 Installation

### Requirements
```
Python 3.8+
Pillow >= 9.0.0
pygame >= 2.0.0
```

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the game
python Main.py
```

## 🎨 Game Mechanics

### Turn System
- Players alternate turns
- Each turn has a configurable timer (60-120s)
- Running out of time = instant loss

### Skills
- 4 unique skills per character
- Cooldown system (varies by skill)
- Character-specific mechanics (forms, gauges, ammo, etc.)

### Buffs & Debuffs
- **Buffs**: Invincibility, High Counter, Regen, Enhanced, etc.
- **Debuffs**: Bleeding, Frozen, Blind, Vulnerable, Sabotage, etc.

### Special Mechanics
- **Transformations** (Maruzen's Enraged, Zen's Blood Rage)
- **Resource Management** (J.A.D.'s ammo, Zen's blood gauge)
- **Status Immunity** (certain buffs grant immunity)
- **DoT Effects** (Bleeding, Burning)

## 🏆 Game Tips

1. **Manage Cooldowns** - Plan your skill usage strategically
2. **Watch the Timer** - Don't run out of time!
3. **Counter Strategies** - Each character has strengths/weaknesses
4. **Use Buffs Wisely** - Invincibility and immunities are powerful
5. **Learn Transformations** - Some characters power up mid-battle

## 🐛 Known Issues

None reported in v1.0.0. Please report bugs via GitHub issues.

## 📜 License

Proprietary - All Rights Reserved

## 👨‍💻 Credits

**Development**: [Your Name/Team]
**Version**: 1.0.0
**Release Date**: June 2026

---

**Enjoy the battle! May the best fighter win! 🥊**
