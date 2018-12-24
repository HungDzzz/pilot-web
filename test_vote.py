import mlab
from vote import Vote
from poll import Poll

mlab.connect()

# from vote => poll

# vote = Vote.objects().first()
# print(vote.choice)
# print(vte.voter)

# poll = vote.poll
# print(poll.question)
# print(poll.options)
# from poll => vote
poll = Poll.objects(code="QBXXGV").first()
votes = Vote.objects(poll=poll)
for vote in votes:
    print(vote.name)
    print(vote.poll.question)
