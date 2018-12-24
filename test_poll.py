from poll import Poll
import string
from random import choice

import mlab

# 1. connect to database
mlab.connect()

# 2. Prepare data
q = "Hackathon an gi ?"
opts = [
    "Pizza",
    "Bami",
    "Pho xao",
]
alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
#print(choice(alphabet))
c = ""
for _ in range(6):
    c += choice(alphabet)
# print(c)
# 3. Create document
p = Poll(question=q, options=opts, code=c)

# 4. Save
p.save()
