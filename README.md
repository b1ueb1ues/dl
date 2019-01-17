# I have changed all the png to jpg for less storage uses, developers need to rebase or clone again. 

# dragalia lost sim and analysis


## Running
python adv/[someone].py [loglevel(-1,0,1,2)]

python adv/mikoto.py

python adv/maribelle.py 1

...

## Folders
- core: simulate engine
- adv: Try to simulate adventurer's damage. Contains charactor unique skill process function, ActionList(like APL in simcraft for wow), and you can change default equip to specific one.
- conf: configure of default skill data to simulate, read frame data from framedata folder, configure default wp/dragon equiped.
- wep: Contains config of weapons' frame and damage data.
- module: Contains bleed now, TODO: add energy.
- framedata: Pictures that have frames number in it. Source of data in adventures and weapons config.
- mechanics: The study of DL's mechanics, Lots of test data, formula,  (Warning: lots of Chinese inside)

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
- dodge  
(comming soon)


#### build-in condition
- s1.charged    
skill's sp now
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
right after s2 proc (the moment as soon as possible you can cast next skill) 
- sx=3  
right after s3 proc (if you are doing normal attack, wait for the cancel timing)  
that is useful for skill shorter than 1.9s. In that case, even the skill end, you cannot find you skill button in the sreen but can only tap attack to wait the button comeback.  
PS: auto control unit don't have that limit

