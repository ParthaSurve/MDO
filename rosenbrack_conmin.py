from openmdao.main.api import Assembly
from openmdao.lib.drivers.api import CONMINdriver
from openmdao.examples.simple.rosenbrack import Rosenbrack

class OptimizationUnconstrained(Assembly):
   
    def configure(self):

        # Create Optimizer instance
        self.add('driver', CONMINdriver())

        # Create Paraboloid component instances
        self.add('rosenbrack', Rosenbrack())

        # Iteration Hierarchy
        self.driver.workflow.add('rosenbrack')

        # SLSQP Flags
        self.driver.iprint = 1

        # Objective
        self.driver.add_objective('rosenbrack.f_xy')

        # Design Variables
        self.driver.add_parameter('rosenbrack.x', low=-50., high=50.)
        self.driver.add_parameter('rosenbrack.y', low=-50., high=50.)
	
	
	
	
        # CONMIN-specific Settings
        self.driver.itmax = 30
        self.driver.fdch = 0.00001
        self.driver.fdchm = 0.000001
        self.driver.ctlmin = 0.01
        self.driver.delfun = 0.001

if __name__ == "__main__":

    opt_problem = OptimizationUnconstrained()

    import time
    tt = time.time()

    opt_problem.run()

    print "\n"
    print "Minimum found at (%f, %f)" % (opt_problem.rosenbrack.x, \
                                     opt_problem.rosenbrack.y)
    print "Elapsed time: ", time.time()-tt, "seconds"

