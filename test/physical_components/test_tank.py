import pytest
from physical_components.tank import Tank
from ..test_values import (
    density_of_liquid,
    water_specific_heat,
    volume,
    starting_temp,
    area,
    tank_heat_transfer_coff,
)

input_tests = [
    # test the zero irradiance case
    (1, 21),  # no real change from 1kj for 100L tank
    (1000, 23),  # 1000kj
    (2000, 26),
    (0, 21),  # still should be ambient
]


@pytest.mark.parametrize("energy_change, solution", input_tests)
def test_tank_temp_change(energy_change, solution):
    tank = Tank(
        volume,
        starting_temp,
        water_specific_heat,
        density_of_liquid,
        area,
        tank_heat_transfer_coff,
    )
    new_tank_temp = tank.temp_energy_change(energy_change)
    assert round(new_tank_temp) == solution
