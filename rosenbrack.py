from openmdao.main.api import Component
from openmdao.lib.datatypes.api import Float


class Rosenbrack(Component):


    # set up interface to the framework
    x = Float(0.0, iotype='in', desc='The variable x')
    y = Float(0.0, iotype='in', desc='The variable y')

    f_xy = Float(0.0, iotype='out', desc='F(x,y)')


    def execute(self):
       
        x = self.x
        y = self.y

       
        self.f_xy = (1.0-x)**2 + 100*(y-x**2)**2



