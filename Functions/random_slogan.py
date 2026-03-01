import random

ss = random.choice(open("/Users/will/Dropbox/zettelkasten/L-Super Slogans 202012281549.md").readlines())
ss = ss.replace("\xa0", " ")

metta = random.choice(open("/Users/will/Dropbox/Projects/Capture DB/Metta.md").readlines())
metta = metta.replace("\xa0", " ")

question = random.choice(open("/Users/will/Dropbox/Projects/Capture DB/Open Ended Questions.md").readlines())
question = question.replace("\xa0", " ")

print(f"""
## Super Slogan
{ss}
## Metta 
- {metta} 
## Open-Ended Question
{question} 

""")
print('\n\n\n')