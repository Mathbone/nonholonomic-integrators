# nonholonomic-integrators
This repository is the beginnings of my dissertation code. The dissertation will focus on using non-holonomic integrators to answer the following question: "A unicyclist will lean into the turn when taking turns at high speed. Does this maneuver decrease the time to make the turn or is it for the purposes of increasing stability?"

The master branch is the simplest working form of the integrator, as an initial value problem.

The "coll" branch is focused on adding a boundary value collocation from which the optimization can then be added.

I am currently looking at taking a more object oriented approach to avoid having to pass the SymPy objects around.
