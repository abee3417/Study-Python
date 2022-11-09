infile = open("proverbs.txt", "r")
outfile = open("output.txt", "a")
i = 1
for line in infile:
    outfile.write("{} : {}".format(i, line))
    i += 1
infile.close()
outfile.close()
