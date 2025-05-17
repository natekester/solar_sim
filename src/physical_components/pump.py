import math


class Pump:
    """
    Very basic pump approx that determines mass flow rate.
    All sorts of factors would change this - length of pipe, height differences, etc.

    This could be extended later, or built with creational patterns that allow for other pumps in the system.
    """

    def __init__(self, inner_diameter, density_of_liquid, flow_velocity):
        self.mass_flow_rate: float = (
            ((math.pi * inner_diameter**2) / 4)
            * density_of_liquid
            * flow_velocity  # represents the velocity (meters/second)
        )

    # for now, not going to worry about setters or getters for this.
