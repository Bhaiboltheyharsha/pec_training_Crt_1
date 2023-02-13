class industry:
    def job(self):
        print("any empolyment")
class software_industry:
    def job(self):
        print("software jobs")
class empolyee(industry,software_industry):
    pass
obj = empolyee()
obj.job()