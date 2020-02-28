# Protosearch
Software for enumerating crystal structure prototypes which can by used for active learning exploration with DFT and machine learning.


## Installation
Using the setup script:

```sh
$ python setup.py install
```
## Enumerating crystal structures

The example below enumerates structures from experimental prototypes, taken as the ICSD entries in the OQMD database. The script below generates the structures and stores them in an ASE db.
```py

from protosearch.build_bulk.oqmd_interface import OqmdInterface

O = OqmdInterface(source='icsd',
                  atom_proximity=0.9,
                  fix_metal_ratio=False,
                  required_elements=[],
                  max_candidates=1)

O.store_enumeration(filename='FeO6.db',
                    chemical_formula='FeO6',
                    max_atoms=7)

```

Protosearch can also enumerate theoretical prototypes from a bottom up approach. This depends on the prototype Bulk Enumerator, accessible upon request from Ankit Jain (`a_jain@iitb.ac.in`).

Protosearch uses a Gaussian Process accelerated genetic algorithm to optimize free Wyckoff parameters and lattice angles for crystallographic prototypes. Good estimates for metal oxides are obtained by using the Ewald Energy as a measure of structure fitness. For metallic systems, the density of the structure is used as a fitness function.

The example below generates a set of theoretical TiO_2 prototypes and stores them in an ASE db.

```py
from protosearch.build_bulk.enumeration import Enumeration, AtomsEnumeration

E = Enumeration("1_2",
                num_start=1,  # min number of atoms or wyckoffs
                num_end=3,  # max number of atoms or wyckoffs
                SG_start=20,  # first spacegroup, default is 1
                SG_end=22,  # last space group, default is 230
                num_type='atom'  # enumeration type is 'atom' or 'wyckoff'
                )
E.store_enumeration('1_2.db')
E = AtomsEnumeration(elements={'A': ['Ti'],
                               'B': ['O']},
                     spacegroups=[21])
E.store_atom_enumeration('1_2.db')
```

## Active learning exploration

An automated framework for running calculations on TRI AWS computing resources has been implemented.
Initializing an active learning loop, including automated structure generation, is done in the script
below.

```py
from protosearch.active_learning.active_learning import ActiveLearningLoop

ALL = ActiveLearningLoop(chemical_formulas=['AB'],
                         elements = {'A': ['Cu', 'Ca'],
                                     'B': ['O']},
                         min_wyckoff=1,
                         max_wyckoff=4,
                         structure_source=['icsd', 'prototypes'],
                         enumeration_type='wyckoff',
                         batch_size=5)

ALL.run()
```