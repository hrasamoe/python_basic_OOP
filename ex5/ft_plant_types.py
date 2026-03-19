class Plant():
  def _init__(self, name, height ) -> None:
    self.name = name
    self.height = height

  def grow(self) -> None:
    self.height += 1
    print(f"{self.name} grew 1cm")

  def get_info(self) -> str:
    return (f"{self.name}: {self.height}cm ")


class FloweringPlant(Plant):
  def __init__(self, name, height, color):
    super().__init__(name, height, )
    self.color = color

    def get_info() -> str:
      return (f"{self.name} {self.height}cm {self.color} flowers (blooming)")

class PrizeFlower(Plant):
  def __init__(self, name, height, prize):
    super().__init__(name, height)
    self.prize = prize

  def get_info(self):
    return super().get_info()