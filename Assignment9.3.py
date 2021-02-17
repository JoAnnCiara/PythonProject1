

name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    line.rstrip()
    if len(line) == 0: contintue
    if not line.startswith("From:"):
        continue
    words = line.split()
    counts[words[1]] = counts.get(words[1], 0) + 1

bigcount = None
bigword = None

for key in counts:
    if bigcount is None: bigcount = counts[key]

    if bigcount < counts[key]:
        bigcount = counts[key]
        bigword = key

print(bigword, bigcount)













