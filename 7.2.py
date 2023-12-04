# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total_value=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    value=line.split(":")[1].strip()
    valuef=float(value)
    total_value+=valuef
    count+=1
avg=total_value/count

print("Average spam confidence: {:.16f}".format(avg))
