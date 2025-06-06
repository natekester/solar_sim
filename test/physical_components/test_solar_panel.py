import pytest
from physical_components.solar_panel import SolarPanel

input_tests = [
    # test the zero irradiance case
    (0, 1, 1, 1, 0),
    # test the 2000 w/m^2 irradiance, 1 meter^2 solar panel, 1 sec -> 2000Ws (Joules)
    (2, 1, 1, 1, 2),
    # test the 2000 w/m^2 irradiance, 2 meter^2 solar panel, 1 sec -> 2000Ws (Joules)
    (2, 2, 1, 1, 4),
    # test the 3000 w/m^2 irradiance, 1 meter^2 solar panel, 1 sec -> 3000Ws (Joules)
    (3, 1, 1, 1, 3),
    # test the 4001 w/m^2 irradiance, 1 meter^2 solar panel, 1 sec -> 4000Ws (Joules)
    (4, 1, 1, 0.5, 2),
]


@pytest.mark.parametrize("irradiance, area, efficiency, time, solution", input_tests)
def test_generate_solar_energy(irradiance, area, efficiency, time, solution):

    energy_created = SolarPanel.energy_created(irradiance, area, efficiency, time)
    assert energy_created == solution


def test_solar_throws_error_for_neg_irradiance():
    with pytest.raises(Exception):
        SolarPanel.energy_created(-1, 1, 1, 1)


def test_solar_throws_error_for_neg_time():
    with pytest.raises(Exception):
        SolarPanel.energy_created(1, 1, 1, -1)
