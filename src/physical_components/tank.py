import math


class Tank:
    def __init__(
        self,
        volume,
        starting_temp,
        water_specific_heat,
        density_of_liquid,
        area,
        heat_transfer_coefficient,
    ):
        self.temp = starting_temp
        self.volume = volume
        self.water_specific_heat = water_specific_heat
        self.density_of_liquid = density_of_liquid
        self.liquid_weight = self.volume * self.density_of_liquid
        self.area = area
        self.heat_transfer_coefficient = heat_transfer_coefficient

    def energy_loss(
        self,
        environment_temp,
        dt,
    ) -> float:
        """
        energy lost will be in kJ
        """
        energy_lost = (
            self.heat_transfer_coefficient * (self.temp - environment_temp) * dt
        )
        return energy_lost

    def temp_energy_change(self, kilo_joules):
        print(
            "kilJoules",
            kilo_joules,
            "\n specific heat:",
            self.water_specific_heat,
            "\n liquid weight:",
            self.liquid_weight,
        )
        temp_change = (kilo_joules / self.water_specific_heat) / self.liquid_weight
        self.temp = self.temp + temp_change
        print("temp_change", temp_change)
        return self.temp
