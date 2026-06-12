# Quick Start Guide - Blu Room Battlefield v1.0.0

## ⚡ 60 Second Setup

### 1. Install (30 seconds)
```bash
pip install -r requirements.txt
```

### 2. Run (5 seconds)
```bash
python Main.py
```

### 3. Play! (Instant)
- Select game mode (1P or 2P)
- Choose your character
- Battle!

---

## 🎮 Essential Controls

| Action | Control |
|--------|---------|
| **Pause Game** | ESC or ⚙ button |
| **Use Skill** | Click skill button |
| **Navigate** | Mouse or Arrow Keys |
| **Confirm** | Enter or Click |

---

## ⚙️ Key Features You Should Know

### Pause Menu (Press ESC)
- **Timer Slider**: Adjust turn time 60-120s
- **Restart**: Quick rematch same characters
- **Resume**: Continue battle

### Turn Timer
- Default: 60 seconds per turn
- Resets each turn
- **Red = 10s left** ⚠️
- Timeout = **instant loss**

### Character Abilities
- 4 skills per character
- Cooldown system (shown on buttons)
- Character-specific resources (ammo, sanity, blood rage, etc.)

---

## 🏆 Quick Tips

1. **Don't timeout** - Watch your timer!
2. **Read cooldowns** - Grayed out = on cooldown
3. **Check battle log** - Shows damage, buffs, debuffs
4. **Use pause wisely** - Plan your strategy
5. **Bot picks random** - In 1P mode, bot won't copy you

---

## 🎯 Character Quick Reference

| Character | Type | Special Mechanic |
|-----------|------|------------------|
| Maruzen | Brawler | Sanity → Enraged |
| Zen | Swordsman | Blood Rage gauge |
| Devourer | Tank | Life drain + immortal |
| J.A.D. | Duelist | Gun/Hand dual stance |
| Giga | Tank | Reflects damage |
| Minos | Wildcard | Luck-based RNG |
| Pol | Warrior | Speed scaling |
| Sed | Summoner | Excalibur mode |
| Russelle | Tank | Revive mechanic |
| Sol Emberload | Mage | Fire DoT |
| Hotori | Specialist | Time Stop freeze |

---

## 🐛 Troubleshooting in 10 Seconds

**Game won't start?**
```bash
python --version  # Need 3.8+
pip install pillow pygame --upgrade
```

**Images missing?**
- Check Assets folder exists in game directory

**Music not playing?**
- Optional feature, game works without it

---

## 📖 Need More Help?

- **Full Guide**: See USER_GUIDE.md
- **Changes**: See CHANGELOG.md
- **Info**: See README.md

---

**Ready to battle? Launch Main.py and let's fight! 🥊**
