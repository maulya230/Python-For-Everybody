# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for lines in fh:
    ly=lines.rstrip()
    print(ly.upper())
