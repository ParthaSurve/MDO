from __future__ import print_function

from openmdao.api import IndepVarComp, Component, Problem, Group, ScipyOptimizer

class Rosenbrock(Component):

    def __init__(self):
        super(Rosenbrock, self).__init__()

        # set up interface to the framework
        self.add_param('x', val=0.0)
        self.add_param('y', val=0.0)
        self.add_output('f_xy', shape=1)

    def solve_nonlinear(self, params, unknowns, resids):

        x = params['x']
        y = params['y']

        unknowns['f_xy'] = (1.0-x)**2 + 100*(y-x**2)**2

    def linearize(self, params, unknowns, resids):

        x = params['x']
        y = params['y']
        J = {}

        J['f_xy','x'] = 2.0*(1.0-x) + 100*2*(y-x**2)*2*x
        J['f_xy','y'] = 100*2*(y-x**2)
        return J

if __name__ == "__main__":
    
    top = Problem()

    root = top.root = Group()

    root.add('p1', IndepVarComp('x', 0.5))
    root.add('p2', IndepVarComp('y', 0.5))
    root.add('p', Rosenbrock())
    root.add('dp', Rosenbrock())

    root.connect('p1.x','p.x')
    root.connect('p2.y','p.y')

    top.driver = ScipyOptimizer()
    top.driver.options['optimizer'] = 'SLSQP'

    top.driver.add_desvar('p1.x', lower = -5.0, upper = 5.0)
    top.driver.add_desvar('p2.y', lower = -5.0, upper = 5.0)
    top.driver.add_objective('p.f_xy')

    top.setup()

    top['p1.x'] = 0.5
    top['p2.y'] = 0.5

    top.run()

    print('\n')
    print('Minimum of %f found at (%f, %f)' % (top['p.f_xy'], top['p.x'], top['p.y']))

    # print(top['p.f_xy'])

