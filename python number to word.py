# Check Examples
numberText = {
	"1" : "one",
	"2" : "two",
	"3" : "three",
	"4" : "four",
	"5" : "five",
	"6" : "six",
	"7" : "seven",
	"8" : "eight",
	"9" : "nine",
	"0" : "zero"
}	
number = input ("number : ")
num = str(number)
numberString = ""
for x in num:
	word = numberText[x]
	numberString += word+ " "
print(numberString)
