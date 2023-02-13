class whatsapp:
    features="chats"
    user_experience="Normal"
class version1(whatsapp):
    features = "status","chats"
    user_experience = "Good"
class version2(version1):
    features = "calls"
    user_experience = "excellent"
class version3(version2):
    pass
print(version3.user_experience)
print(version3.features)
