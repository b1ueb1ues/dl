# dragalia lost sim and analysis

## Running
Python 3.7+

```
python adv/[someone].py [loglevel(-4,-3,-2,-1,0,1,2)] [teamdps] [mass]
```
or
```
./sim [someone] [loglevel(-4,-3,-2,-1,0,1,2)] [teamdps] [mass]
```
or
```
./sim.bat [someone] [loglevel(-4,-3,-2,-1,0,1,2)] [teamdps] [mass]
```

loglevel:
- 0: default report
- 1: detailed log
- 2: python code transpiled from ACL
- -2: CSV format
- -5: sim with 100% affliction

- python adv/mikoto.py

show basic result of Mikoto's simulation

- python adv/maribelle.py 1

show result and combo loop of Maribelle

- python adv/gala_sarisse.py -2 180 10000
show result of Gala Sarisse for 180s with 10000 team dps

## Folders
- core: simulate engine
- adv: Try to simulate adventurer's damage. Contains charactor unique skill process function, ActionList(like APL in simcraft for wow), and you can change default equip to specific one.
- conf: configure of default skill data to simulate, read frame data from framedata folder, configure default wp/dragon equiped.
- wep: Contains config of weapons' frame and damage data.
- module: Contains bleed now.
- framedata: Pictures that have frames number in it. Source of data in adventures and weapons config.
- mechanics: The study of DL's mechanics, Lots of test data, formula,  (Warning: lots of Chinese inside)
- slot: defination of weapons, amulets(wrymprints), dragons.
- abilities: defination abilities.

## Acl syntax
```
# a = b
`action, condition
`action2, condition2 or condithon3=4
# c = d
```
after # is prepare language, prepare language will execute before action language

after ` is action you want to do when condition is true, if this action can't be execute, then passthrough next action

this acl will be translate into
```
a=b
c=d
if condition:
    if action():
        break
if condition2 or condition3==4:
    if action2():
        break
```
#### build-in action
- s1  
skill1
- s2  
skill2
- s3  
weapon skill
- fs  
forse strike
- fsf 
forse strike(failed)
- dodge  
dodge

#### build-in condition
- s1.charged >= s1.sp  
Skill 1 is ready.
- s2.charged > 2000:  
S2 is charged more than 2000sp.
- cancel  
At the timing that c1~c5 and fs just have dealt damage(shot the missile for ranged unit)
- x  
At the timing that c1~c5 just have dealt damage(shot the missile for ranged unit)
- fsc  
At the timing that fs just have dealt damage(shot the missile for ranged unit)
- sp  
At the timing of sp gain. (usefull for ranged dps to acknowledge their missile hitting target)
- seq=1  
At the timing from c1 to c2, any event can trigger that.
- seq=5  
At the timing from c5 to c5 recovery
- s=2  
Right after s2 proc (the moment as soon as possible you can cast next skill) 
- sx=3  
Right after s3 proc. If you are doing normal attack, wait for the cancel timing.  
that is useful for skill shorter than 1.9s. In that case, even if the skill end, you cannot find you skill button in the sreen but can only tap attack to wait the button comeback.  
PS: auto controled unit don't have that limit
- now()<10  
the simulation time less than 10 seconds.
- pin='prep'
after skill prep (happened at sim start for those who have a skill prep)

## Rotation method
use acl 
```
`rotation
```
add conf.rotation and conf.rotation\_init  
rotation\_init will do only once before rotation
the rotation will reset to the beginning if it ends
```
conf['rotation'] = "c4fsc4fss1c4fsc4fss1c3s2c4fsc4fss1c1s3"
```
space, linefeed, tabulators are ignored in the rotation  
you can make a readable rotation like this
```
conf['rotation'] = """
    c4fs c4fs s1
    c4fs c4fs s1
    c3 s2
    c4fs c4fs s1
    c1 s3
    """
```


# Adventurer ability information

Adventurer passives are programmed in their individual `adv/advname.py`
modules.

- Each ability is named `a1`, etc., records a tuple of `(name, value, cond)`
- See `dl.ability.Ability` for how name translates

# Acronyms

The code uses a lot of abbreviations.  Here is a decoder ring for
many of them:

- att - attack (as in attack modifier)
- x - basic attack (as part of, e.g., a C5 combo)
- fs - force strike
- fsf - force strike (failed)
- s (as in s1, s2) - skill
- ex - ex-skill(co-abilities)
- buff - buff
- iv - interval
- dot - damage over time
- m (as in mtype, morder) - modifier
- crit - critical
- ac - action
- sp - skill points
- pin - the moment when think() been called
- cb - callback
- spd - speed
- acl - access control list (not really, just a DSL for specifying adventurer behavior, like apl in wow simc)
- dmg - damage
- wt - weapon type
- slots.c - character
- slots.w - weapon
- slots.d - dragon
- slots.a - amulet(wyrmprints)
- `a_` (as in `a_s1`) - denotes an action
- `l_` (as in `l_x`) - denotes a listener
- `m_` (as in `m_condition`) - denotes a Python module
- solid - computes the expected value of a modifier (this is the one
  that actually gets used)
- rand - randomly samples based on the probability
- coef - coefficient
- proc - https://gaming.stackexchange.com/questions/122163/what-does-proc-mean

# Adventurer stats

Adventurer stats are stored in `conf/adv\_data.csv` and read into the
`Conf` object (`conf/csv2conf.py`).  All skill damage assumes full
upgrades.

- `sX\_hitdmg` how much percent damage skill X hits for (not used yet)
- `sX\_hits` how many hits the skill does (not used yet)
- `sX\_sp` SP cost of the skills
- `sX\_dmgpc` this is most likely just `sX\_hitdmg * sX\_hits`, but this is the real column we use, 
   since there is some skill that deals 3 hits of 255% and 1 hit of 319% veronica for example.)
- `sX\_buff` describes what buff the skill gives.  Buff is described
  as semicolon separated list:
  - Target of the buff ('team', 'self', 'debuff'); this can e
    omitted in which case you get an ordinary 'Buff'
  - The rest of the buff arguments, as defined by the Buff/Teambuff/etc
    classes.  Typically, these arguments are:
    - Value of the buff
    - Duration of the buff
    - Optional modifier type of the buff (e.g., att, x, fs, s, crit; defaults to att)
    - Optional modifier order of the buff (e.g., rate, chance, buff;
      defaults to chance for crit modifiers, and buff otherwise)
