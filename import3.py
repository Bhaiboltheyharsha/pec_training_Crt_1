import re
p = r"[aeiou]"
if re.search(p, "gun"):
    print("matchy vowel")
else:
    print("not found")
