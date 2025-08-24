"""
combat.py

Python functions for checking hit success and calculating damage.
"""

import random
import re

import random
import re
from typing import Tuple

def parse_dice(term: str) -> Tuple[int, int, int]:
    """
    Parse a dice expression like 'XdY+N' (whitespace allowed around symbols).

    Returns:
        (num_dice, sides, modifier)

    Examples:
        >>> parse_dice("1d20")
        (1, 20, 0)
        >>> parse_dice(" 2 d 6 + 3 ")
        (2, 6, 3)
    """
    term = term.replace(" ", "")
    m = re.fullmatch(r"(\d+)d(\d+)(?:\+(\d+))?", term, re.IGNORECASE)
    if not m:
        raise ValueError(f"Invalid dice expression: {term!r}")
    num_dice = int(m.group(1))
    sides = int(m.group(2))
    modifier = int(m.group(3)) if m.group(3) else 0
    if num_dice < 1 or sides < 1:
        raise ValueError("num_dice and sides must be >= 1")
    return num_dice, sides, modifier


def roll(term: str) -> int:
    """
    Roll dice based on a term like "1d20+4".

    Supports:
      - XdY  (roll X dice with Y sides)
      - Optional +N modifier
      - Whitespace around symbols

    Examples:
        >>> roll("1d20")        # random between 1 and 20
        >>> roll("1d20 + 4")    # random between 5 and 24
        >>> roll("3d6+2")       # random between 5 and 20
    """
    num_dice, sides, modifier = parse_dice(term)
    total = sum(random.randint(1, sides) for _ in range(num_dice))
    return total + modifier


def attack_roll(attack_modifier: int, target_ac: int) -> dict:
    """
    Perform a D&D attack roll.

    Returns:
        {
            "d20": int,              # raw d20 result
            "total": int,            # d20 + modifier
            "hit": bool,
            "critical_hit": bool,    # natural 20
            "automatic_miss": bool   # natural 1
        }

    Examples:
        >>> attack_roll(5, 15)  # +5 vs AC 15
        {'d20': 12, 'total': 17, 'hit': True, 'critical_hit': False, 'automatic_miss': False}
    """
    d20 = roll("1d20")
    total = d20 + attack_modifier

    critical_hit = (d20 == 20)
    automatic_miss = (d20 == 1)

    if automatic_miss:
        return {"d20": d20, "total": total, "hit": False, "critical_hit": False, "automatic_miss": True}
    if critical_hit:
        return {"d20": d20, "total": total, "hit": True, "critical_hit": True, "automatic_miss": False}

    hit = (total >= target_ac)
    return {"d20": d20, "total": total, "hit": hit, "critical_hit": False, "automatic_miss": False}


def damage_roll(term: str, critical: bool = False) -> dict:
    """
    Roll weapon/spell damage using roll(), with 5e crits (double dice, add modifier once).

    Args:
        term: Dice expression like "1d8+3", "2d6 + 4".
        critical: If True, roll all damage dice twice.

    Returns:
        {
            "total": int,
            "critical": bool,
            "expression_used": str  # the rebuilt expression actually rolled
        }

    Examples:
        >>> damage_roll("1d8+3")              # normal hit, 4–11
        >>> damage_roll("1d8 + 3", True)      # crit, 5–19
        >>> damage_roll("2d6")                # normal, 2–12
        >>> damage_roll("2d6", critical=True) # crit, 4–24
    """
    num_dice, sides, modifier = parse_dice(term)

    if critical:
        num_dice *= 2

    expr = f"{num_dice}d{sides}" + (f"+{modifier}" if modifier else "")
    total = roll(expr)

    return {"total": total, "critical": critical, "expression_used": expr}
