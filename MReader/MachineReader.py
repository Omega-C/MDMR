#stuff to make the json file
"""def parser(raw):
	lines=[l.strip().split("\t")[0].replace("*","") for l in raw.split("\n") if ("lett" not in l) and ("'" not in l)]
	lines=[l for n, l in enumerate(lines) if l not in lines[:n]]
	return(lines)

dContext={}
words=parser(open("words.txt","r").read().lower())

for word in words:
	items=[dContext[k] for k in (dContext.keys())]
	for c in range(len(word)):
		w=word[:c+1]
		if w not in items:
			dContext[word]=w
			break
	if word not in dContext:dContext[word]=word"""

text="""COME away, come away, death, 
   And in sad cypres let me be laid; 
Fly away, fly away, breath; 
   I am slain by a fair cruel maid. 
My shroud of white, stuck all with yew, 
   O prepare it! 
My part of death, no one so true 
   Did share it. """

import re

import json
dContext=json.load(open("words.json","r"))#or replace with a dict for defaults

CBool=lambda s:[c.isupper() for c in s]
CApply=lambda s,l:"".join([s[a].upper() if l[a] else s[a] for a in range(len(s))])
shft={}
work=list(c for c in re.split(r"(\W+)",text) if c!="")
words=set(c for c in work if re.match(r"(\w+)",c))
eff=2
effM=1.5

for word in words:
	cPattern=CBool(word)
	if word.lower() in dContext and len(dContext[word.lower()])<len(word)/effM:sh=dContext[word.lower()]#checks if whats in a shorthand dict is short enough
	else:sh=word[:int(len(word)/eff+(eff-1)/eff)]#improvised ceil
	shft[word]=f"**{CApply(sh,cPattern)}**{CApply(word[len(sh):],cPattern[len(sh):])}"#The formatting part
for i in range(len(work)):
	if work[i] in shft:work[i]=shft[work[i]]

print("".join(work))