# dragalia lost sim and analysis


## Running
python adv/[someone].py [loglevel(-1,0,1,2)]

python adv/mikoto.py

python adv/maribelle.py 1

...

## Folders
- core: simulate engine
- adv: Try to simulate adventurer's damage. Contains frame data, skill data, ActionList(acl like simulate for wow)
- wep: Contains config of weapons' frame and damage data.
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
    action()
if condition2 or condition3==4:
    action2()
```
