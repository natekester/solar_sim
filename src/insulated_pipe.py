import math


class InsulatedPipe:
    thermal_resistance: float = (
        0.18  # Watt / meter Kelvin - generally a good assumption
    )

    def __init__(
        self,
        length,
        outside_diameter,
        inner_diameter,
        insulation_thickness,
        flow_velocity,
        density_of_liquid=1000,
    ):
        self.length: float = length  # meters
        self.outside_diameter: float = outside_diameter  # meters
        self.inner_diameter: float = inner_diameter  # meters
        self.insulation_thickness: float = insulation_thickness  # again, meters
        self.flow_velocity: float = flow_velocity
        self.density_of_liquid = density_of_liquid

    def calc_mass_flow_rate(self) -> float:
        mass_flow_rate = (
            ((math.pi * self.inner_diameter**2) / 4)
            * self.density_of_liquid
            * self.flow_velocity
        )
        return mass_flow_rate

    def calc_pipe_thermal_resistance(self) -> float:
        pipe_therm_resistance = (
            math.log(
                (self.outside_diameter + self.insulation_thickness)
                / self.outside_diameter
            )
            * 2
            * math.pi
            * self.thermal_resistance
        )
        return pipe_therm_resistance

    def energy_loss(
        inlet_water_temp: int, environment_temp: int, dtime: float, self
    ) -> float:
        """
        This function determines the incoming energy of the solar panel

        Parameters:
        solar_irradiance (int): units of watts/m^2 - generally 0 to 4000 ish
        area (int): area in units of meters squared
        efficiency (float): efficiency of the panel. 0 to 1.
        dtime (float): time in seconds

        """
        water_specific_heat = 4.186  # kJ/kg*kelvin
        mass_flow_rate = self.calc_mass_flow_rate()
        pipe_thermal_resistance = self.calc_pipe_thermal_resistance()
        water_environment_temp_diff = inlet_water_temp - environment_temp
        pipe_length_flow_capacity = 1 - math.exp(
            -(
                self.length
                / water_specific_heat
                * mass_flow_rate
                * pipe_thermal_resistance
            )
        )
        createdEnergy = (
            water_specific_heat
            * mass_flow_rate()
            * water_environment_temp_diff
            * pipe_length_flow_capacity
        )

        return createdEnergy
