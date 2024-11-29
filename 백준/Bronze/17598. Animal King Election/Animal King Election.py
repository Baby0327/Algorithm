vote = [input() for _ in range(9)]
print("Tiger" if vote.count("Tiger") > 4 else "Lion")