import random

ss = random.choice(open("/Users/will/Dropbox/zettelkasten/L-Super Slogans 202012281549.md").readlines())
ss = ss.replace("\xa0", " ")

print(f"""
## Super Slogan
{ss}
{'–'*5}
""")