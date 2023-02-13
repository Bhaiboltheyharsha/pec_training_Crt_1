from abc import ABC, abstractmethod
class marvel(ABC):
    @abstractmethod
    def hero_characters(self):
        pass
    @abstractmethod
    def villan_characters(self):
        pass
class ironman(marvel):
    def hero_characters(self):
        print("Ironman")
    def villan_characters(self):
        pass
class captian_america(marvel):
    def hero_characters(self):
        print("Captian America")
    def villan_characters(self):
        pass
class thanos(marvel):
    def villan_characters(self):
        print("Thanos")
    def hero_characters(self):
        pass
obj = thanos()
obj.villan_characters()