import re

my_sample = "Learning Regular Expressions"

#n = re.search("ar", my_sample)
#print(n)
#print(n.span())
#print(n.string)
#print(n.group())

#n = re.findall("ar", my_sample)
#n = re.split("ar", my_sample)
n = re.sub("ar", "15", my_sample)
print(n)