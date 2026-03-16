#setup
votes: list = []
invalid_voters: set = set()
s_uniq = set()
counter = 0
invalid_votes = 0

vote = None
print("to stop, press   -999   ")

while True:
    vote = int(input("please enter your id: "))
    if vote == -999:
        break

    while vote > 100 or vote < 0:
        vote = int(input("invalid number, please enter your id: "))
    votes.append(vote)
    s_uniq.add(vote)
    counter += 1

valid_voters = set()

for vote in s_uniq:
    if votes.count(vote) > 1:
        invalid_voters.add(vote)
    else:
        valid_voters.add(vote)

#printing
print (f'you got {counter} voters over all')
print(f"Those are your valid voters: {valid_voters}")
print(f'you have {len(invalid_voters)} invalid voters: {invalid_voters}')
