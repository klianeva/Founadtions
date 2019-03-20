#Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;

#-A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~

#-Every smiling face must have a smiling mouth that should be marked with either ) or D.

#No additional characters are allowed except for those mentioned.

#Valid smiley face examples:
#:) :D ;-D :~)
smilies = [":)", "nsd", ":-)", ":D"]

def count_smileys(smilies):
	eyes = [":", ";"]
	nose = ["-", "~"]
	mouth = [")", "D"]
	i = 0
	for smile in smilies:
		if len(smile) == 2:
			if smile[0] in eyes and smile[1] in mouth:
				i+=1
		elif len(smile) == 3:
			if smile[0] in eyes and smile[1] in nose and smile[2] in mouth:
				i+=1
		else:
			print("I don't know")
	print(i)

count_smileys(smilies)