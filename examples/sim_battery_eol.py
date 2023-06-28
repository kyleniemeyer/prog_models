# Copyright © 2021 United States Government as represented by the Administrator of the
# National Aeronautics and Space Administration.  All Rights Reserved.

"""
Example of a battery being simulated until End of Life (EOL). Battery capacity decreases with use. In this case, EOL is defined as when the battery capacity falls below some acceptable threshold (i.e., what we define as useful capacity). 
"""

import matplotlib.pyplot as plt
from prog_models.models import BatteryElectroChem as Battery

def run_example(): 
    # Step 1: Create a model object
    batt = Battery()

    # Step 2: Define future loading function
    # Here we're using a function designed to charge until 0.95, 
    # then discharge until 0.05
    load = 1

    def future_loading(t, x=None):
        nonlocal load 

        # Rule for loading after initialization
        if x is not None:
            # Current event state in the form {'EOD': <(0, 1)>, 'InsufficientCapacity': <(0, 1)>}
            event_state = batt.event_state(x)
            if event_state["EOD"] > 0.95:
                load = 1  # Discharge
            elif event_state["EOD"] < 0.05:
                load = -1  # Charge
        # Rule for loading at initialization
        return batt.InputContainer({'i': load})

    # Step 3: Simulate to Capacity is insufficient Threshold
    print('\n\n------------------------------------------------')
    print('Simulating to threshold\n\n')
    options = {
        'save_freq': 1000,  # Frequency at which results are saved
        'dt': 2,  # Timestep
        'threshold_keys': ['InsufficientCapacity'],  # Simulate to InsufficientCapacity
        'print': True
    }
    simulated_results = batt.simulate_to_threshold(future_loading, **options)

    # Step 4: Plot Results
    simulated_results.inputs.plot(ylabel='Current drawn (amps)')
    simulated_results.event_states.plot(ylabel='Event States', labels={'EOD': 'State of Charge (SOC)', 'InsufficientCapacity': 'State of Health (SOH)'})
    plt.ylim([0, 1])

    plt.show()

# This allows the module to be executed directly 
if __name__ == '__main__':
    run_example()
