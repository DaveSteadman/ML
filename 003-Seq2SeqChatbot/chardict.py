import json

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# create numbers 1..x and assume no deletions

def chardict_id_for_char(cdict, ch):
    if (ch in cdict):
        return cdict[ch]
    else:
        nextid = len(cdict) + 1 
        cdict[ch] = nextid
        return nextid

def chardict_addchar(cdict, ch):
    if ch not in cdict:
        nextid = len(cdict) + 1 
        cdict[ch] = nextid

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Create and query a reverse dictionary so we can extract the words from the Ids.

def chardict_reverse_dict(cdict):
    rev_cdict = dict(zip(cdict.values(), cdict.keys())) 
    return rev_cdict

def chardict_word_for_id(rev_cdict, chid):
    if (chid in rev_cdict):
        return rev_cdict[chid]
    else:
        return '#'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Save / Load functions

def chardict_serialise(cdict, filename):
    with open(filename, 'w') as file:
        file.write(json.dumps(cdict))
    
def chardict_deserialise(filename):
    cdict = {}
    with open(filename, 'r') as file:
        cdict = json.loads(file.read())
    return cdict

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def chardict_standardprepop():
    cdict = {}

    lletters = "abcdefghijklmnopqrstuvwxyz"
    uletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers  = "1234567890"
    punct    = " !?£$€^&*()[]{}<>-=;:@#~,._+¬/\|"

    for eachch in lletters:
        chardict_id_for_char(cdict, eachch)
    for eachch in uletters:
        chardict_id_for_char(cdict, eachch)
    for eachch in numbers:
        chardict_id_for_char(cdict, eachch)
    for eachch in punct:
        chardict_id_for_char(cdict, eachch)

    chardict_id_for_char(cdict, '\n')
    chardict_id_for_char(cdict, '\t')
    
    return cdict 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
