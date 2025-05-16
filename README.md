# SIMULATION MODEL

## Code Challenge Instructions

Physics Simulator Coding Exercise

Write a simple software simulation of the following system.

Minimum Requirements

1. The system should simulate the heat transfer from a solar panel to a storage tank
2. Use whichever coding language you wish
3. We will evaluate thermodynamic correctness, code approach, and results.

## Initial Thoughts

This is a very open ended project. Could go on forever. The 'simple software simulation' is somewhat contradictory to the statement of thermodynamic correctness (unless it's just simply saying units are correct?). I could have potentially modelled it as electrical components. Such as energy loss through wires vs pipes, etc. Might come back to that if the below doesn't pass my smell test.

### Thoughts on the thermodynamics

Energy In = Solar + Pump Friction (negligible) + outsideEnergy if negative gradient to environment (it's hotter outside than inside - shouldn't be the case in the sim) + friction of water within the pipe (negligible)

simplified as just: Energy In = solar input

Energy Out = -(pipe heat loss + tank heat loss)

Modelling the change in temperature with _flowing_ water would be quite tough.

In general the change in energy is a

change in energy = Energy In - Energy out over time

#### Solar/Heat Collector

immediate energy generated (Watt second or joules) = solar irradiance (W/m^2) _ Area of panel _ dt

#### Pipe heat loss

using the following study on heat transport pipelines:
https://link.springer.com/article/10.1007/s42452-022-05226-2

![pipe heat loss image](pipe-heat-loss.png)
Thermal resistance of the pipe:
𝑅=𝑙𝑛[(𝐷+𝛿)/𝐷]2𝜋𝜆

R: Thermal resistance per metre (m K W−1)
Insulation thermal conductivity: a decent value of λ = 0.18 W m−1 K−1.
D: outside diameter (meters)
𝛿: insulation thickness(meters)

Heat Loss Q:
𝑄= C𝑝 𝐺(𝑇𝑖 − 𝑇𝑠)[1−exp(−𝐿 / C𝑝 𝐺 𝑅)]

Q: kJ/s
With Cp being specific heat of water (assuming constant under pressure - eh good enough): 4.186 kJ/kg\*K
Specific heat at constant pressure (kJ kg−1 K−1)

L: pipeline length (meters)
Ti: Inlet temp of water (Celsius)
Ts: Environment temp or Surrounding Temp (Celsius)
G: the mass flow rate of the hot water (kg/s)

𝐺=(𝜋𝑑\**2/4)*𝜌𝑣
v is it's flow velocity (m per s)
d is inner diameter of the pipe (meters)
p is the density of the hot water (kg/m^3)

### Thought ProcessSystem Parts

In real life this gets incredibly complicated. In real life it can be quite a challenge to model the environment:

- weather
- sun cloud cover
- outside temperature
- latitude of the solar panel
- object obstructions
- angle of solar panel
- corrosion of the system based on the climate/etc
- and many more parameters

The pipes also get very complicated:

- insulation/conductance of the pipe
- the length/diameter of the pipe
- the heat capacity of the pipe
- does it cause turbulent or laminar flow?

The solar panel itself:
------ TODO ----
