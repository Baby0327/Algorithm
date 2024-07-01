import sys

n = int(sys.stdin.readline())

log = set()
for i in range(n):
    name, act = sys.stdin.readline().rstrip().split()
    if act == 'enter':
        log.add(name)
    elif act == 'leave':
        log.discard(name)

log = list(log)
log.sort(reverse=True)

for i in log:
    sys.stdout.write(i+'\n')