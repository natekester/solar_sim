class SolarPanel:
    """Basic solar panel model to show energy creation from solar irradiance, area, efficiency, and change in time"""

    @staticmethod
    def energy_created(
        solar_irradiance: int, area: int, efficiency: float, dtime: float
    ) -> float:
        """
        This function determines the incoming energy of the solar panel

        Parameters:
        solar_irradiance (int): units of kilowatts/m^2 - generally 0 to 4 ish
        area (int): area in units of meters squared
        efficiency (float): efficiency of the panel. 0 to 1.
        dtime (float): time in seconds

        return kilojoules of energy
        """
        createdEnergy = solar_irradiance * area * dtime * efficiency
        if efficiency > 1 or efficiency < 0:
            raise Exception("Error: efficiency should be a num between 0 and 1")
        if createdEnergy < 0:
            raise Exception("Error: solar panel generated negative energy")

        return createdEnergy
