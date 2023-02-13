import string
import re
# match and search
str1 = " she sells sea shells at sea shore"
p1 = "sea"
rep = "ocean"
ns = re.sub(p1, rep, str1)
print(ns)
