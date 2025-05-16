import math


class Pump:
    def __init__(self, inner_diameter, density_of_liquid, flow_velocity):
        self.mass_flow_rate: float = (
            ((math.pi * inner_diameter**2) / 4)
            * density_of_liquid
            * flow_velocity  # represents the velocity (meters/second)
        )

    # for now, not going to worry about setters or getters for this.
