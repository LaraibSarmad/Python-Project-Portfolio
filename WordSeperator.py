Word = "StopAndSmellTheRoses"

i = 0

result = ""

for c in Word:

    if c.isupper() and i > 0:

        result += " "

        result += c.lower()

    else:

        result += c

    i += 1


print (result)