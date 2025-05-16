import pytest
from insulated_pipe import InsulatedPipe

input = [
    (0, 1, 1, 1, 0),
]


@pytest.mark.parametrize("irradiance, area, efficiency, time, solution", input)
def test_pipe_energy_loss(
    length,
    outside_diameter,
    inner_diameter,
    insulation_thickness,
    flow_velocity,
    inlet_water_temp,
    environment_temp,
    dtime,
    solution,
):
    pipe = InsulatedPipe(
        length, outside_diameter, inner_diameter, insulation_thickness, flow_velocity
    )
    energy_lost = pipe.energy_loss(inlet_water_temp, environment_temp, dtime)
    assert energy_lost == solution
