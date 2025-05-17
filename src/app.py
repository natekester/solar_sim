import numpy as np
import matplotlib.pyplot as plt
import math

from physical_components.pump import Pump
from physical_components.insulated_pipe import InsulatedPipe
from physical_components.solar_panel import SolarPanel
from physical_components.tank import Tank
from values import (
    daily_irradiance,
    environment_temp,
    current_tank_temp,
    tank_area,
    volume,
    flow_velocity,
    water_specific_heat,
    insulation_thickness,
    inner_diameter,
    outside_diameter,
    density_of_liquid,
    tank_heat_transfer_coff,
    length_of_pipe,
    area,
    thermal_resistance,
    efficiency,
)


def simulate_solar_tank_thermodynamics(
    daily_irradiance=daily_irradiance,
    environment_temp=environment_temp,
    current_tank_temp=current_tank_temp,
    tank_area=tank_area,
    volume=volume,
    flow_velocity=flow_velocity,
    water_specific_heat=water_specific_heat,
    insulation_thickness=insulation_thickness,
    inner_diameter=inner_diameter,
    outside_diameter=outside_diameter,
    density_of_liquid=density_of_liquid,
    tank_heat_transfer_coff=tank_heat_transfer_coff,
    area=area,
    efficiency=efficiency,
):
    """
    Function to simulate a solar panel, insulated pipe, and tank

    Creates a graph of the tank temperature
    """
    ## creating the flow of the system
    basic_pump = Pump(inner_diameter, density_of_liquid, flow_velocity)

    ## the flow of the system impacts pipe energy loss
    pipe = InsulatedPipe(
        length_of_pipe,
        basic_pump,
        thermal_resistance,
        density_of_liquid,
        outside_diameter,
        inner_diameter,
        insulation_thickness,
        water_specific_heat,
    )

    # the solar panel class to determine energy creation
    solar_panel = SolarPanel()

    # the water tank - determines minor energy loss and energy storage
    tank = Tank(
        volume,
        current_tank_temp,
        water_specific_heat,
        density_of_liquid,
        tank_area,
        tank_heat_transfer_coff,
    )

    dt = 20  # setting it up in second increments
    fraction_of_min = dt / 60
    seconds_in_5_days = 86400 * 5
    time = np.arange(0, seconds_in_5_days, dt)  # time in 1 min bites over 5 days
    tank_temp_over_time = np.zeros_like(time)
    tank_temp_over_time[0] = current_tank_temp
    min_passed = 0
    for i in range(1, len(time)):
        min_passed = min_passed + fraction_of_min
        hour = math.floor(min_passed / 60)
        if hour + 1 > len(daily_irradiance):
            print("You've reached the end of your data. Graphing.")
            break

        # daily irradiance data is hourly and in watts
        # get the solar irradiance in kw every hour
        solar_irradiance = daily_irradiance[hour] / 1000

        energy_lost_pipe = pipe.energy_loss(current_tank_temp, environment_temp, dt)
        energy_lost_tank = tank.energy_loss(environment_temp, dt)

        energy_lost = energy_lost_pipe + energy_lost_tank

        # you would technically lose efficiency as the water to env temp gradient changed
        # but this is a simple model, so it's going to be constant
        energy_added = solar_panel.energy_created(
            solar_irradiance, area, efficiency, dt
        )

        energy_delta = energy_added - energy_lost

        current_tank_temp = tank.temp_energy_change(energy_delta)

        tank_temp_over_time[i] = current_tank_temp

    plt.plot(time / 60 / 60 / 24, tank_temp_over_time)
    plt.xlabel("Time (days)")
    plt.ylabel("Tank Temperature (°C)")
    plt.title("Enclosed 100L Tank Temp")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    simulate_solar_tank_thermodynamics()
