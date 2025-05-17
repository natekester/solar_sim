import math
from physical_components.pump import Pump


class InsulatedPipe:
    """a class to represent an insulated pipe and its energy loss with flowing liquid"""

    def __init__(
        self,
        length,
        pump: Pump,
        thermal_resistance,
        density_of_liquid,
        outside_diameter,
        inner_diameter,
        insulation_thickness,
        water_specific_heat,
    ):
        self.length: float = length  # meters
        self.pump = pump
        self.thermal_resistance = thermal_resistance
        self.density_of_liquid = density_of_liquid
        self.outside_diameter = outside_diameter
        self.inner_diameter = inner_diameter
        self.insulation_thickness = insulation_thickness
        self.water_specific_heat = water_specific_heat
        self.pipe_thermal_resistance = self.__calc_pipe_thermal_resistance()

    def __calc_pipe_thermal_resistance(self) -> float:
        """
        Private: Calculate the pipe's thermal resistance

        returns kJ / meter kelvin
        """
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
        self, inlet_water_temp: int, environment_temp: int, dtime: float
    ) -> float:
        """
        This method determines the energy loss of the insulated pipe

        Parameters:
        inlet_water_temp (int): generally 25+ celsius
        environment_temp (int): generally 0-25 celsius
        dtime (float): change of time in seconds to calculate energy loss

        Returns:
        Kilojoules of energy lost
        """
        mass_flow_rate = self.pump.mass_flow_rate
        water_environment_temp_diff = inlet_water_temp - environment_temp
        pipe_length_flow_capacity = 1 - math.exp(
            -(
                self.length
                / self.water_specific_heat
                * mass_flow_rate
                * self.pipe_thermal_resistance
            )
        )
        lost_energy_per_second = (
            self.water_specific_heat
            * mass_flow_rate
            * water_environment_temp_diff
            * pipe_length_flow_capacity
        )  # kJ/s

        lost_energy = lost_energy_per_second * dtime

        return lost_energy
