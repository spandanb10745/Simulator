from .simulation_settings import DELTA_TIME


class Component:
    """General model of an electrical component"""    
    
    def __init__(self, name, **junction_names):
        """
        name : str - name of component
        **junction_names : dict - key: pin name -> value: junction name
        """
        self.name = name
        self.junction_names = junction_names
        
    def get_junction_names(self):
        return self.junction_names.values()
    
    def connect(self, junctions):
        """
        Connects the component into the circuit by creating the appropriate
        fields (named after the pins) with Junction classes
        Parameters:
        junctions: dict - key: junction name -> value: Junction class
        """
        for pin, junction_name in self.junction_names.items():
            self.__dict__[pin] = junctions[junction_name]
    

class Resistor(Component):
    
    def __init__(self, name, r, pos, neg):
        """
        name : str - name of resistor
        r : float - resistance value
        pos : str - junction name connected to positive pin
        neg : str - junction name connected to negative pin
        """
        super().__init__(name, pos=pos, neg=neg)
        self.r = r        
        
    def simulation_step(self):
        self.i = (self.pos.v - self.neg.v) / self.r
        self.pos.add_current(self.i)
        self.neg.add_current(-self.i) 

        
class Capacitor(Component):
    
    def __init__(self, name, c, pos, neg):
        """
        name : str - name of capacitor
        c : float - capacitance value
        pos : str - junction name connected to positive pin
        neg : str - junction name connected to negative pin
        """
        super().__init__(name, pos=pos, neg=neg)
        self.c = c
        self.v = 0
        
    def simulation_step(self):
        """
        Capacitor modifies it's voltage according to the following equatation:
        I = C * dV / dt
        then sets voltage of it's junctions
        """ 
        i = self.pos.i - self.neg.i
        dv = -i * DELTA_TIME / self.c       
        self.v += dv
        
        self.pos.set_voltage(self.neg.v + self.v)
        # reset junction currents to zero
        self.pos.reset_current()
        self.neg.reset_current()        


class Inductor(Component):

    def __init__(self, name, l, pos, neg):
        """
        name : str - name of inductor
        l : float - induction value
        pos : str - junction name connected to positive pin
        neg : str - junction name connected to negative pin
        """
        super().__init__(name, pos=pos, neg=neg)
        self.l = l
        self.i = 0
        
    def simulation_step(self):
        """
        Inductor modifies it's current according to the following equatation:
        V = L * dI / dt
        then outputs this current to it's junctions        
        """ 
        v = self.pos.v - self.neg.v
        di = v * DELTA_TIME / self.l       
        self.i += di
        
        self.pos.add_current(self.i)
        self.neg.add_current(-self.i) 
        


        





        