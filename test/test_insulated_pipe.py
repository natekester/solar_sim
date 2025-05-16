import pytest
from insulated_pipe import InsulatedPipe
from pump import Pump
from app import (
    thermal_resistance,
    density_of_liquid,
    outside_diameter,
    inner_diameter,
    insulation_thickness,
    water_specific_heat,
    flow_velocity,
)

## Hard coded Assumptions for these tests to work
# thermal_resistance: float = 0.18  # Watt / meter Kelvin - generally a good assumption
# density_of_liquid = 1000  # # 1000 kg/m^3 normally for pure water (997 might be a lil' more accurate tho)
# outside_diameter = 0.0254  # 1" in meters - common pipe size
# inner_diameter = 0.0330  # 1.315" in meters
# insulation_thickness = 0.0254  # 1" of insulation
# water_specific_heat = 4.186  # kJ/kg*kelvin
# flow_velocity: float = 2  # 2 meters/second is common for pumps with 1" iDiameter


# length(meters), flow_velocity, inlet_water_temp, environment_temp, dtime, solution
input = [
    ##if you change the constants on app.py, these will fail
    (50, 102, 21, 60, 34800),  # 34800 kJ lost
    (50, 102, 21, 30, 34800 / 2),  # half as much energy lost in half the time
    (5, 100, 21, 60, 27100),  # 27100 kJ lost
    (5, 21, 21, 60, 0),  # 0 energy loss if inlet temp is same as outside
]
# fun thought: 27100 kj will raise a liter of water how much C?
# 1 liter is 1kg
# lets assume 190L tank or 190kg
# specific heat of water is 4.186 kJ/kg*c
# 34800/4.186 = 6473.960 kg*c -> divide by 190 -> 34 degrees celsius
# so the energy equivalent of pushing 100 degree water through ~15ft of insulated pipe
# over a minute is the same energy that it would take for a
# a 190L tank to lose 34 degrees? seems off


@pytest.mark.parametrize(
    "length, inlet_water_temp, environment_temp, dtime, solution",
    input,
)
def test_pipe_energy_loss(
    length,
    inlet_water_temp,
    environment_temp,
    dtime,
    solution,
):
    basicPump = Pump(inner_diameter, density_of_liquid, flow_velocity)

    ## the flow of the system impacts pipe energy loss
    insulated_pipe = InsulatedPipe(
        length,
        basicPump,
        thermal_resistance,
        density_of_liquid,
        outside_diameter,
        inner_diameter,
        insulation_thickness,
        water_specific_heat,
    )

    energy_lost = insulated_pipe.energy_loss(
        inlet_water_temp,
        environment_temp,
        dtime,
    )
    assert round(energy_lost) == solution
