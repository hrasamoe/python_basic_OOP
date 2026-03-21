class Plant:
  class _Stats:
    def __init__(self):
      self._grow_calls = 0
      self._age_calls = 0
      self._show_calls = 0

    def inc_grow(self):
      self._grow_calls += 1
    
    def inc_age(self):
      self._age_calls += 1
    
    def inc_show(self):
      self._show_calls += 1
    
  def __init__(self, name:str, height:float, days:int):
      self.name: str = name
      self.days: int = days
      self.height: float = height
      self._stats = Plant._Stats()

  def grow(self, amount = 2.1):
    self.height += amount
    self._stats.inc_grow()

  def age(self, amount = 1):
    self.days += amount
    self._stats.inc_age()
  
  def show(self):
    self._stats.inc_show()
    print(f"{self.name}: {round(self.height, 1)}"
          f"cm, {self.days} days old"
          )
  
  def display_stat(self):
      print(f"Stats: {self._stats._grow_calls} grow, {self._stats._age_calls} age"
            f", {self._stats._show_calls} show"
            )
  
  @staticmethod
  def is_older_than_year(days):
    return days > 365
  
  @classmethod
  def anonymous(cls):
    return cls("Unknown plant", 0.0, 0)

class Tree(Plant):
  def __init__(self, name, height, days, trunk_diameter: int):
    super().__init__(name, height, days)
    self.trunk_diameter:int = trunk_diameter
    self._shade_calls = 0
  
  def produce_shade(self):
    self._shade_calls += 1
    print(f"Tree {self.name} now produces a shade of"
          f" {round(self.height, 1)}cm long and"
          f" {round(self.trunk_diameter, 1)}cm wide"
          )

  def show(self):
    super().show()
    print(f" Trunk diameter: {round(self.trunk_diameter, 1)}cm")

  def display_stat(self):
    super().display_stat()
    print(f"{self._shade_calls} shade")

class Flower(Plant):
  def __init__(self, name, height, days, color: str):
    super().__init__(name, height, days)
    self.color: str = color
    self.bloom: bool = False
    

  def bloom(self):
    print(f"[asking {self.name} to grow and bloom]")
    self.bloom = True
  
  def display_stat(self):
    super().display_stat()

  def show(self):
    super().show()
    print(f" Color: {self.color}")
    if self.bloom:
      print(f"{self.name} is blooming beautifully!")
    else:
      print(f"{self.name} has not bloomed yet")

class Seed(Flower):
  def __init__(self, name, height, days, color):
    super().__init__(name, height, days, color)
    self.seeds = 0
  
  def bloom(self):
    super().bloom()
    self.seeds = 42
  
  def show(self):
    super().show()
    print(f"Seeds: {self.seeds}")

def display_plant_stat(Plant):
  print(f"[Statistics for {Plant.name}]")
  Plant.display_stat()

if __name__ == "__main__":
  print("=== Garden statistics ===")
  print("=== Check year old ===")
  print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
  print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

  print("\n=== Flower ===")
  rose = Flower("Rose", 15.0, 10, "red")
  rose.show()
  display_plant_stat(rose)
  # rose.display_stat()
  rose.grow(8)
  rose.show()
  # rose.display_stat()
  display_plant_stat(rose)