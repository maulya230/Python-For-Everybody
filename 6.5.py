text = "X-DSPAM-Confidence:    0.8475"
x=text.find(":")
n=text[x+1:]
print(float(n))
