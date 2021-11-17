# Typewriter
# ----------
# layout: str
# colour: str
# num_keys: int
# price: float

class Typewriter:
    def __init__(self, layout: str, colour: str, 
                  num_keys: int, price: float) -> None:
        self.layout = layout
        self.colour = colour
        self.num_keys = int
        self.price = price

# -------------------------------------------------------------------

# Napkin
# ------
# surface_area: float
# absorbancy_level: float
# brand: str

class Napkin:
    def __init__(self, surface_area: float, 
                  absorbancy_level: float, brand: str) -> None:
        self.surface_area = surface_area
        self.absorbancy_level = absorbancy_level
        self.brand = brand

# -------------------------------------------------------------------

# Chair
# -----
# max_supported_weight: float
# num_legs: int
# fabric: str

class Chair:
    def __init__(self, max_supported_weight: float, 
                  num_legs: int, fabric: str) -> None:
        self.max_supported_weight = max_supported_weight
        self.num_legs = num_legs
        self.fabric = fabric
