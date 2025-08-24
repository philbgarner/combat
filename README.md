# combat
Combat PyModule - A combat module for NakedMud, implements basic D20 style combat mechanics.

## Dependencies

It is recommended you use this module in combination with the gear module.  Without gear it will use fallbacks to calculate hit checks and damage with core stats only.

## Installation

### Option 1: Download and Extract
1. Download the gear module files
2. Extract to your `lib/pymodules/combat/` directory
3. Restart your MUD or reload Python modules

### Option 2: Git Submodule
```bash
cd lib/pymodules/
git submodule add <repository-url> combat
git submodule update --init --recursive
```

## Commands Added

The module adds these admin commands:

- **`combatconfig`** - Online configuration editor for combat settings (admin level required).

## Configuration Files

- **Runtime config**: `lib/misc/combat-config` - Active configuration (auto-created with defaults).
- **Backup config**: `lib/misc/combat.old` - Preserved original configuration

## What It Does

The combat module implements a basic D20 based DnD style combat system where players and mobiles roll to hit and then roll to do damage based on their character stats and equipment bonuses (if the gear submodule is installed).  It uses a persistent configuration that can be modified at runtime through menus.

The combat turn is documented in the CombatTurn.mermaid diagram in this repository.

### Hit Attack Roll

When you roll to hit a creature you roll a D20 and add your modifiers and compare it to the creature's armor class to see if it's the same or higher.

### Damage Rolls

If you successfully, hit you roll your damage dice and add any modifiers before applying resistances or vulnerability modifiers.

Once the calculated damage is applied to the creature, its health points are reduced by that amount and if they become zero or lower the mobile will be dead.

### Experience Points

Experience points will be divided among any players who were engaged in combat with the creature and were alive and present in the room when it died.

### API Functions

#### Hit Rolling Function

#### Damage Rolling Function

