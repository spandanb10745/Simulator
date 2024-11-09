from simulator import circuit
# from simulator import component_list
from simulator import components
# from simulator import junction
from simulator import measurement
# from simulator import misc
# from simulator import simulation_settings
from simulator import sources

circuit = circuit.Circuit()  

circuit.add(sources.DCVoltageSource(name='V1', v = 5, pos ='1', neg = 'GND'))
circuit.add(components.Resistor(name='R1', r=3000, pos='1', neg='2')) 
circuit.add(components.Inductor(name='L1', l=5*10e-2, pos='2', neg='GND'))
circuit.add(measurement.Voltmeter(name='VM', pos='2', neg='GND'))
circuit.add(measurement.ISenseResistor(name='I1', resistor_name='R1')) 

circuit.simulate(simulation_time=500)