# Copyright © 2021 United States Government as represented by the Administrator of the
# National Aeronautics and Space Administration.  All Rights Reserved.

"""
This example shows the use of the LinearModel class, a subclass of PrognosticsModel for models that can be described as a linear time series. 

The model is used in a simulation, and the state is printed every second
"""

import numpy as np
from prog_models import LinearModel
        
class ThrownObject(LinearModel):
    """
    Model that simulates an object thrown into the air without air resistance

    Events (2)
        | falling: The object is falling
        | impact: The object has hit the ground

    Inputs/Loading: (0)

    States: (2)
        | x: Position in space (m)
        | v: Velocity in space (m/s)

    Outputs/Measurements: (1)
        | x: Position in space (m)

    Keyword Args
    ------------
        process_noise : Optional, float or dict[Srt, float]
          Process noise (applied at dx/next_state). 
          Can be number (e.g., .2) applied to every state, a dictionary of values for each 
          state (e.g., {'x1': 0.2, 'x2': 0.3}), or a function (x) -> x
        process_noise_dist : Optional, str
          distribution for process noise (e.g., normal, uniform, triangular)
        measurement_noise : Optional, float or dict[Srt, float]
          Measurement noise (applied in output eqn).
          Can be number (e.g., .2) applied to every output, a dictionary of values for each
          output (e.g., {'z1': 0.2, 'z2': 0.3}), or a function (z) -> z
        measurement_noise_dist : Optional, str
          distribution for measurement noise (e.g., normal, uniform, triangular)
        g : Optional, float
            Acceleration due to gravity (m/s^2). Default is 9.81 m/s^2 (standard gravity)
        thrower_height : Optional, float
            Height of the thrower (m). Default is 1.83 m
        throwing_speed : Optional, float
            Speed at which the ball is thrown (m/s). Default is 40 m/s
    """

    inputs = []  # no inputs, no way to control
    states = [
        'x',     # Position (m) 
        'v'      # Velocity (m/s)
        ]
    outputs = [
        'x'      # Position (m)
    ]
    events = [
        'impact' # Event- object has impacted ground
    ]

    # These are the core of the linear model. 
    # Linear models defined by the following equations:
    #   * dx/dt = Ax + Bu + E
    #   * z = Cx + D
    #   * event states = Fx + G
    A = np.array([[0, 1], [0, 0]]) # dx/dt = Ax + Bu + E
    E = np.array([[0], [-9.81]]) # Acceleration due to gravity (m/s^2)
    C = np.array([[1, 0]]) # z = Cx + D
    F = None # Will override method

    # The Default parameters. Overwritten by passing parameters dictionary into constructor
    default_parameters = {
        'thrower_height': 1.83,  # m
        'throwing_speed': 40,  # m/s
        'g': -9.81  # Acceleration due to gravity in m/s^2
    }

    def initialize(self, u=None, z=None):
        return self.StateContainer({
            'x': self.parameters['thrower_height'],  # Thrown, so initial altitude is height of thrower
            'v': self.parameters['throwing_speed']  # Velocity at which the ball is thrown - this guy is a professional baseball pitcher
            })
    
    # This is actually optional. Leaving thresholds_met empty will use the event state to define thresholds.
    #  Threshold = Event State == 0. However, this implementation is more efficient, so we included it
    def threshold_met(self, x):
        return {
            'falling': x['v'] < 0,
            'impact': x['x'] <= 0
        }

    def event_state(self, x): 
        x_max = x['x'] + np.square(x['v'])/(-self.parameters['g']*2) # Use speed and position to estimate maximum height
        return {
            'falling': np.maximum(x['v']/self.parameters['throwing_speed'],0),  # Throwing speed is max speed
            'impact': np.maximum(x['x']/x_max,0) if x['v'] < 0 else 1  # 1 until falling begins, then it's fraction of height
        }

def run_example():
    m = ThrownObject()
    def future_loading(t, x=None):
        return m.InputContainer({})  # No loading 
    m.simulate_to_threshold(future_loading, print = True, save_freq=1, threshold_keys='impact', dt=0.1)

# This allows the module to be executed directly 
if __name__ == '__main__':
    run_example()
