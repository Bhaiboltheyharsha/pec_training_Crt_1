from translate import Translator
obj = Translator(from_lang="english", to_lang="hindi")
new_name = obj.translate("guna")
print(new_name)