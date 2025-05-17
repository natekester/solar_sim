import pytest
from physical_components.insulated_pipe import InsulatedPipe
from physical_components.pump import Pump
from ..test_values import (
    thermal_resistance,
    density_of_liquid,
    outside_diameter,
    inner_diameter,
    insulation_thickness,
    water_specific_heat,
    flow_velocity,
)

# length(meters), flow_velocity, inlet_water_temp, environment_temp, dtime, solution
input = [
    ##if you change the constants on app.py, these will fail
    (
        50,
        99,
        21,
        60,
        532,
    ),  # 532 kJ lost over 50 meters of insulated pipe
    (50, 99, 21, 30, 532 / 2),  # half as much energy lost in half the time
    (5, 100, 21, 60, 54),  # 54 kJ lost
    (5, 21, 21, 60, 0),  # 0 energy loss if inlet temp is same as outside
]
# fun thought: 54 kj will raise a liter of water how much C?
# 1 liter is 1kg
# lets assume 190L tank or 190kg
# specific heat of water is 4.186 kJ/kg*c
# so 54kJ lost over 5 meters of insulated pipe running with boiling water
# 54kj/4.186 kj/kg*c -> 12.90 kg*c -> so it would change 10Liters of water ~1.3 degrees celsius?
# that feels way more reasonable than before. That is a very insulated pipe though - makes sense with numbers
# coming from heat transfer pipes.


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
