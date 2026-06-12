# Blu Room Battlefield - User Guide

## Table of Contents
1. [Getting Started](#getting-started)
2. [Game Modes](#game-modes)
3. [Character Selection](#character-selection)
4. [Battle System](#battle-system)
5. [Settings & Controls](#settings--controls)
6. [Character Guide](#character-guide)
7. [Tips & Strategies](#tips--strategies)
8. [Troubleshooting](#troubleshooting)

---

## Getting Started

### Installation

1. **Install Python 3.8+** (if not already installed)
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Game**:
   ```bash
   python Main.py
   ```

### Main Menu

When you launch the game, you'll see:
- **1 Player** - Fight against AI bot
- **2 Player** - Local PvP battle
- **Guides** - View character information
- **Exit** - Close the game

---

## Game Modes

### 1 Player Mode (vs Bot)
- Select your character
- Bot automatically chooses a random different character
- Battle with configurable turn timer
- Perfect for practice!

### 2 Player Mode (Local PvP)
- Player 1 selects character first
- Player 2 selects second
- Take turns making moves
- Timer runs for each player's turn

---

## Character Selection

### Navigation
- **Mouse Click** - Select character thumbnail
- **Arrow Keys** - Navigate grid
- **Enter** - Confirm selection
- **ESC** - Go back

### Character Preview
- Left panel shows selected character
- Character name and description displayed
- Bottom bar shows both players' selections

---

## Battle System

### Battle UI Layout

```
┌─────────────────────────────────────────────┐
│  P1 Info   [HP Bar]  [Timer]   VS   [Timer]  [HP Bar]   P2 Info  │
│                           ⚙ Settings                              │
├─────────────────────────────────────────────┤
│                                             │
│     [P1 Sprite]           [P2 Sprite]      │
│                                             │
│     Buffs/Debuffs        Buffs/Debuffs     │
│                                             │
├─────────────────────────────────────────────┤
│  Battle Log        │  Skill 1  Description │
│  (Scrollable)      │  Skill 2  Description │
│                    │  Skill 3  Description │
│                    │  Skill 4  Description │
└─────────────────────────────────────────────┘
```

### Turn Structure

1. **Turn Start** - Player's turn begins, timer resets
2. **Select Skill** - Click one of 4 skill buttons
3. **Execute** - Animation plays, effects apply
4. **End Turn** - Cooldowns reduce, DoT ticks
5. **Next Turn** - Other player's turn begins

### Timer System

- Each player gets configured time (60-120s default 60s)
- Timer resets at start of YOUR turn
- **Red Warning** at 10 seconds remaining
- Running out of time = **instant loss**

---

## Settings & Controls

### In-Game Settings (Press ESC or ⚙)

#### Turn Timer Configuration
- **Slider**: 60-120 seconds per turn
- **Resolution**: 10-second increments
- **Apply Button**: Confirms timer change
- Changes affect both players immediately

#### Action Buttons
- **Resume (▶)** - Return to battle
- **Restart (↺)** - Restart with same characters
- **Main Menu (⌂)** - Return to main menu

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| ESC | Open/Close Settings |
| Click Skills | Use character ability |
| Mouse Click | Interact with UI |

---

## Character Guide

### 1. Maruzen (Sanity-Driven Brawler)

**Resource**: Sanity (0-100)
**Transformation**: Enraged (when Sanity ≤ 0)

**Normal Form Skills**:
1. **Why Would I Fight?** - Restore +10 sanity, 10% bonus turn
2. **Please Slap Me** - Heal last damage taken, -20 sanity
3. **Invincible** - Immune to damage 2 turns, -30 sanity
4. **Sanity Implosion** - Deal sanity/2 dmg, lose sanity/2

**Enraged Form Skills**:
1. **Payback** - 1-3 hits, 5% MaxHP each
2. **Manipulation** - Surrender chance (scales with turns)
3. **Death Wish** - 30 + (100-sanity)/5 damage
4. **System Sabotage** - Inflict Sabotage debuff 2 turns

**Strategy**: Manage sanity carefully. Enraged form is powerful but risky.

---

### 2. Zen (Blood Rage Swordsman)

**Resource**: Blood Rage Gauge (0-100)
**Mechanics**: High damage when gauge is full

**Skills**:
1. **Gale Strike** - 5 dmg or full ATK (if Blood Rage active)
2. **A Lost Cause** - 0.2x ATK, +40 Blood Rage
3. **A Silent Plead** - High Counter buff 3 turns
4. **Death Slash** - 1x ATK, halve Blood Rage

**Strategy**: Build Blood Rage with skill 2, unleash with skill 4.

---

### 3. Devourer (Immortal Predator)

**Mechanics**: Life drain and immortality

**Skills**:
1. **Slash** - 20 + 0.1x ATK, Regen 5 HP/turn
2. **Lemme Suck 'Em** - Drain 20% enemy current HP
3. **Lethal Claw** - 20 dmg + Bleeding 2 turns
4. **Immortality** - Cannot die for 2 turns

**Strategy**: Use immortality wisely, drain when enemy has high HP.

---

### 4. J.A.D. (Gun & Blade Duelist)

**Resource**: Ammo (0-3)
**Stances**: Gun Form / Hand Form

**Gun Form Skills**:
1. **Gunshot** - 0.3x ATK, costs 1 ammo
2. **Gunho** - Clear enemy buffs & self debuffs
3. **Long Shot** - Costs 2 ammo, 10% headshot chance
4. **Mist** - Costs 3 ammo, Blind enemy 2 turns

**Hand Form Skills** (when out of ammo):
1. **Knife Slash** - 0.2x ATK
2. **Gunho** - Clear enemy buffs & self debuffs
3. **Backstab** - 0.4x ATK
4. **Throat Cutter** - 15% instant execution chance

**Strategy**: Manage ammo carefully. Gunho is available in both forms.

---

### 5. Giga (Armored Tank)

**Mechanics**: Damage reflection and stat buffs

**Skills**:
1. **Shield Bash** - 0.5x ATK, reflects 30% damage taken
2. **Double Damage** - Next attack deals 2x damage
3. **Invincible** - Immune to damage 2 turns
4. **Enhanced** - Double all stats 2 turns

**Strategy**: Stack buffs for massive damage, use invincibility to survive.

---

### 6. Minos (Luck-Based Wildcard)

**Resource**: Luck stat (increases with skill 2)

**Skills**:
1. **Lucky Strike** - Random 1-999 damage based on luck
2. **Dunca Tonca** - +5 luck permanently
3. **Take It All** - 50% SE Immunity+Regen OR 50% Vulnerable
4. **Immortality** - Cannot die 2 turns

**Strategy**: Build luck early, pray to RNG gods.

---

### 7. Pol (Wind Warrior)

**Mechanics**: Speed-scaled damage, Wind Covenant

**Skills**:
1. **Gale Slash** - 20 + 0.1x SPD damage
2. **Stance: Unyielding** - High Counter 3 turns
3. **Drive: Windcharge** - 0.2x ATK + 0.3x SPD damage
4. **Wind Maiden Hael** - Covenant of Wind, clear debuffs

**Strategy**: Speed is key. Use Covenant for sustained power.

---

### 8. Sed (War Maiden Summoner)

**Mechanics**: Excalibur mode with stat boosts

**Skills**:
1. **Gale Slash** - 20 + 0.1x SPD damage
2. **Serene Posture** - BA Boost 3 turns
3. **Warhammer Onslaught** - 0.6x ATK damage
4. **War Maiden Ei-ram** - Excalibur buff, clear debuffs

**Strategy**: Build up to Excalibur mode for maximum power.

---

### 9. Russelle (Iron Sleeper)

**Mechanics**: Damage reduction, revival

**Skills**:
1. **Iron Fist** - 20 + 0.5x ATK, 80% dmg reduction
2. **Deep Sleep** - Heal 30% MaxHP, Sleeping buff
3. **Mutual Vulnerability** - Both take 20% more damage
4. **Last Stand** - Revive from 0 HP once (infinite CD)

**Strategy**: Tank damage, use Last Stand as last resort.

---

### 10. Sol Emberload (Living Flame)

**Mechanics**: Fire DoT specialist

**Skills**:
1. **Ember Strike** - ATK + Burned 2 turns
2. **Sol Kick** - ATK + 25 damage
3. **Smoke Veil** - Blind enemy, heal 15 HP
4. **Inferno Burst** - 2x ATK + Burned 3 turns

**Strategy**: Stack burning effects for massive DoT damage.

---

### 11. Hotori (Time Manipulator)

**Mechanics**: Time control and chrono effects

**Skills**:
1. **Basic Attack** - 15 dmg, 20% bonus turn
2. **Chrono Shift** - Recover last damage as HP
3. **Godspeed** - Deal 30% of enemy current HP
4. **Time Stop** - Freeze enemy 4 turns, reset cooldowns

**Strategy**: Time Stop is OP. Use wisely.

---

## Tips & Strategies

### General Tips
1. **Watch Cooldowns** - Plan 2-3 turns ahead
2. **Timer Management** - Don't rush, but don't waste time
3. **Read Battle Log** - Important info appears here
4. **Learn Counters** - Each character has weaknesses
5. **Use Pause** - Think strategy without time pressure

### Advanced Strategies
1. **Buff Stacking** - Some characters can combine buffs
2. **DoT Combos** - Bleeding + Burning = massive damage
3. **Cooldown Resets** - Hotori's Time Stop resets her cooldowns
4. **Resource Management** - Don't spam high-cost skills
5. **Transformation Timing** - Know when forms trigger

### Common Mistakes
1. **Ignoring Timer** - Most common cause of loss
2. **Spamming Skill 1** - Basic attacks won't win
3. **Poor Cooldown Management** - Left with no skills
4. **Forgetting Debuffs** - Check status effects
5. **Not Using Settings** - Adjust timer to your pace

---

## Troubleshooting

### Game Won't Start
- Check Python version (3.8+)
- Install dependencies: `pip install -r requirements.txt`
- Verify all asset files are present

### Images Not Loading
- Check Assets folder exists
- Verify image file paths
- Run from correct directory

### Music Not Playing
- Install pygame: `pip install pygame`
- Check Assets/Music folder
- Music can be muted via settings

### Performance Issues
- Close other applications
- Lower screen resolution
- Disable animations (not yet implemented)

### Controls Not Working
- Click to focus game window
- Check keyboard/mouse connection
- Restart game

---

## FAQ

**Q: Can I play online?**
A: Not in v1.0.0. Local multiplayer only.

**Q: How do I unlock characters?**
A: All 11 characters available from start.

**Q: Can I customize controls?**
A: Not yet. Default controls only in v1.0.0.

**Q: Is there a tutorial?**
A: In-game Guides menu shows character info.

**Q: Can I save replays?**
A: Not in v1.0.0. Future feature.

**Q: How do I report bugs?**
A: Contact developer or create GitHub issue.

---

**Enjoy the game! Good luck in the Blu Room Battlefield! 🥊**
