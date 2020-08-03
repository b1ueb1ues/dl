# Web DPS Simc App

Deployed here: https://wildshinobu.pythonanywhere.com/

Demo here: https://wildshinobu.pythonanywhere.com/ui/dl_simc.html

Flask app on top of the python sim.

# Routes

## /simc_adv_test

Takes POST requests containing adventurer name + configuration and runs DPS sim then return the output.

### General Inputs:
* adv - the adventurer name, this is required
* wp1 - first wyrmprint
* wp2 - second wyrmprint
* dra - dragon
* wep - weapon
* ex - EX abilities/co-abilities, valid inputs are k(blade), r(wand), b(bow), d(dagger), m(crit damage)
* acl - ACL that defines adventurer script, see main README
* teamdps - base team dps value, used for team buff sim
If any input other than adv is not supplied, the sim will use default values defined in the adv.py files.
Certain special adventurers are not allowed to change ACL or WP, for example EHJP GCleo

### Affliction Related Inputs: poison, paralysis, burn, blind, bog, stun, freeze, sleep
* afflict_res_{affliction} - sets the resist for a certain affliction
* sim_afflict_type - sets the type of a fake affliction that deals no damage but activates punishers
* sim_afflict_time - sets the amount of time said fake affliction exists for

### Simulated Buff Inputs
* sim_buff_str - sets the amount of adventurer STR buff/debuff to apply for the duration of the sim
* sim_buff_def - sets the amount of enemy DEF buff/debuff to apply for the duration of the sim

### Returned JSON
* test_output - the basic output of dps sim, using verbose=-2
* extra - extra info not expressed in the test output, includes % team buff and # of team energy
* extra_no_cond - same thing but for the conditionless sim
* logs - detailed logs of the sim timeline

## /simc_adv_slotlist

Takes POST or GET requests containing adventurer name, and return the default configuration for them.

### Returned JSON Dict
* adv
  * name - adventurer name
  * ele - element
  * wt - weapon type
  * pref_dra - preferred dragon
  * pref_wep - preferred weapon
  * pref_wp - preferred wp1 and wp2
  * acl - current ACL
  * afflict_res - affliction resist, set for adventurer that can inflict a certain affliction
  * no_config - configuration options that are disabled for this adventurer
* dragons - list of dragons of the same element as the adventurer
* weapons - list of weapons of the same element as the adventurer

## /simc_adv_wp_list

Takes POST or GET requests and returns a list of adventurer and wyrmprints

### Returned JSON Dict
* adv - list of adventurers
* amulets - list of wyrmprints
