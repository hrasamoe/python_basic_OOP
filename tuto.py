from typing import List


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name  } grew 1cm")

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color: str = color

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, points: int) -> None:
        super().__init__(name, height, color)
        self.points: int = points

    def get_info(self) -> str:
        return f"{super().get_info()}, Prize points: {self.points}"


class GardenManager:
    total_gardens: int = 0

    class GardenStats:
        def __init__(self) -> None:
            self.plants_added: int = 0
            self.total_growth: int = 0

        def record_growth(self, amount: int) -> None:
            self.total_growth += amount

        def record_plant(self) -> None:
            self.plants_added += 1

    def __init__(self, owner: str) -> None:
        self.owner: str = orner
        self.plants: List[Plant] = []
        self.stats: GardenManager.GardenStats = self.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        self.stats.record_plant()
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.record_growth(1)

    def report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")

        regular = flowering = prize = 0

        for plant in self.plants:
            print(f"- {plant.get_info()}")
            if isinstance(plant, PrizeFlower):
                prize += 1
            elif isinstance(plant, FloweringPlant):
                flowering += 1
            else:
                regular += 1

        print(f"Plants added: {self.stats.plants_added}, Total growth: {self.stats.total_growth}cm")
        print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")

    @classmethod
    def create_garden_network(cls, owners: List[str]) -> List["GardenManager"]:
        return [cls(owner) for owner in owners]

    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0

    @staticmethod
    def calculate_score(garden: "GardenManager") -> int:
        score = 0
        for plant in garden.plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.points
        return score