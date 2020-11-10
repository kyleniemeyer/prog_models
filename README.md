# Prognostics Model Python Package

The NASA Prognostic Model Package is a python modeling framework focused on defining and building models for prognostics (computation of remaining useful life) of engineering systems, and provides a set of prognostics models for select components developed within this framework, suitable for use in prognostics applications for these components.

## Implementation

Each model must be a class extending either `prog_models.model` (for nominal models) or `prog_models.prognostics_model` (for prognostics, i.e. degredation model). Prognostics model implements a `simulate_to(time)` and `simulate_to_threshold` function for simulation.

## Directory Structure 

`prog_models/` - The prognostics model python package <br>
 |-`models/` - Example models <br>
 |-`model.py` - Physics-based model superclass of nominal system behavior <br>
 |-`prognostics_model.py` - Physics-based model superclass of degraded system behavior <br>
`example.py` - An example python script using prog_models <br>
`README.md` - The readme (this file)
`requirements.txt` - python library dependiencies required to be met to use this package. Install using `pip install -r requirements.txt`
`deriv_model_template.py` - Template for Derivative Model
`prog_model_template.py` - Template for Prognsotics Model

## Citing this repository
Use the following to cite this repository:

```
@misc{2020_nasa_prog_model,
    author    = {Christopher Teubert and Chetan Kulkarni},
    title     = {Prognostics Model Python Package},
    month     = Oct,
    year      = 2020,
    version   = {0.0.1},
    url       = {TBD}
    }
```

The corresponding reference should look like this:

C. Teubert, and C. Kulkarni, Prognostics Model Python Package, v0.0.1, Oct. 2020. URL TBD.

## Notices

Copyright © 2020 United States Government as represented by the Administrator of the National Aeronautics and Space Administration.  All Rights Reserved.

## Disclaimers

No Warranty: THE SUBJECT SOFTWARE IS PROVIDED "AS IS" WITHOUT ANY WARRANTY OF ANY KIND, EITHER EXPRESSED, IMPLIED, OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, ANY WARRANTY THAT THE SUBJECT SOFTWARE WILL CONFORM TO SPECIFICATIONS, ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR FREEDOM FROM INFRINGEMENT, ANY WARRANTY THAT THE SUBJECT SOFTWARE WILL BE ERROR FREE, OR ANY WARRANTY THAT DOCUMENTATION, IF PROVIDED, WILL CONFORM TO THE SUBJECT SOFTWARE. THIS AGREEMENT DOES NOT, IN ANY MANNER, CONSTITUTE AN ENDORSEMENT BY GOVERNMENT AGENCY OR ANY PRIOR RECIPIENT OF ANY RESULTS, RESULTING DESIGNS, HARDWARE, SOFTWARE PRODUCTS OR ANY OTHER APPLICATIONS RESULTING FROM USE OF THE SUBJECT SOFTWARE.  FURTHER, GOVERNMENT AGENCY DISCLAIMS ALL WARRANTIES AND LIABILITIES REGARDING THIRD-PARTY SOFTWARE, IF PRESENT IN THE ORIGINAL SOFTWARE, AND DISTRIBUTES IT "AS IS."

Waiver and Indemnity:  RECIPIENT AGREES TO WAIVE ANY AND ALL CLAIMS AGAINST THE UNITED STATES GOVERNMENT, ITS CONTRACTORS AND SUBCONTRACTORS, AS WELL AS ANY PRIOR RECIPIENT.  IF RECIPIENT'S USE OF THE SUBJECT SOFTWARE RESULTS IN ANY LIABILITIES, DEMANDS, DAMAGES, EXPENSES OR LOSSES ARISING FROM SUCH USE, INCLUDING ANY DAMAGES FROM PRODUCTS BASED ON, OR RESULTING FROM, RECIPIENT'S USE OF THE SUBJECT SOFTWARE, RECIPIENT SHALL INDEMNIFY AND HOLD HARMLESS THE UNITED STATES GOVERNMENT, ITS CONTRACTORS AND SUBCONTRACTORS, AS WELL AS ANY PRIOR RECIPIENT, TO THE EXTENT PERMITTED BY LAW.  RECIPIENT'S SOLE REMEDY FOR ANY SUCH MATTER SHALL BE THE IMMEDIATE, UNILATERAL TERMINATION OF THIS AGREEMENT.