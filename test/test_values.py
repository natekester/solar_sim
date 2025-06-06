# This file is a copy of the values.py file
# So if you change the values.py file the tests still pass.


thermal_resistance: float = (
    0.00018  # kJ / meter Kelvin(or celsius) second - generally a good assumption
)
density_of_liquid = 1000  # # 1000 kg/m^3 normally for pure water (997 might be a lil' more accurate tho)
outside_diameter = 0.0254  # 1" in meters - common pipe size
inner_diameter = 0.0330  # 1.315" in meters
insulation_thickness = 0.0254  # 1" of insulation
water_specific_heat = 4.186  # kJ/kg*celsius(or kelvin)
flow_velocity: float = 2  # 2 meters/second is common for pumps with 1" iDiameter
volume: float = 0.100  # we'll say around 100 liters or 0.1 meter cubed
tank_area: float = 1.4  # ~1.4 square meters for 100 liter tank
starting_temp = 21  # ~room temp is where we will start
current_tank_temp = 21  # ~room temp is where we will start
environment_temp = 21  # ~room temp is where we will start
tank_heat_transfer_coff = 0.0003  # kW/m^2K assuming really good insulation
solar_irradiance = (
    1  # 4 kw is pretty high, should be fun to start. real world would not
)
area = 1  # meter square
efficiency = 0.7  # heat captures can get up there to 70%
length_of_pipe = 5  # 5 meters of pipe?

# using some NSRDB data for lat: 41.92 long: -110.49 for a few days
# using csvs/NSRDB API and Pandas df would make sense for long term app
daily_irradiance = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    294,
    721,
    878,
    940,
    966,
    964,
    934,
    864,
    710,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    386,
    812,
    951,
    1012,
    1036,
    1033,
    1000,
    929,
    771,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    323,
    762,
    909,
    956,
    978,
    973,
    942,
    877,
    719,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    350,
    771,
    914,
    974,
    985,
    986,
    952,
    873,
    706,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    228,
    681,
    833,
    908,
    938,
    948,
    917,
    847,
    683,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]
