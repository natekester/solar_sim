from pump import Pump
from insulated_pipe import InsulatedPipe


## Hard coded Assumptions
thermal_resistance: float = (
    0.00018  # kJ / meter Kelvin(or celsius) second - generally a good assumption
)
density_of_liquid = 1000  # # 1000 kg/m^3 normally for pure water (997 might be a lil' more accurate tho)
outside_diameter = 0.0254  # 1" in meters - common pipe size
inner_diameter = 0.0330  # 1.315" in meters
insulation_thickness = 0.0254  # 1" of insulation
water_specific_heat = 4.186  # kJ/kg*celsius(or kelvin)
flow_velocity: float = 2  # 2 meters/second is common for pumps with 1" iDiameter


def solar_tank_thermodynamics():
    length_of_pipe = 5  # 5 meters of pipe?

    ## creating the flow of the system
    basicPump = Pump(inner_diameter, density_of_liquid, flow_velocity)

    ## the flow of the system impacts pipe energy loss
    insulatedPipe = InsulatedPipe(
        length_of_pipe,
        basicPump,
        thermal_resistance,
        density_of_liquid,
        outside_diameter,
        inner_diameter,
        insulation_thickness,
        water_specific_heat,
    )

    return tank_temp


if __name__ == "__main__":
    solar_tank_thermodynamics()
