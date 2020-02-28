# Protosearch
Software for enumerating crystal structure prototypes which can by used for active learning exploration with DFT and machine learning.

## Installation
Using the setup script:

```sh
$ python setup.py install
```
## Enumerating crystal structures from experimental prototypes:

Storing prototypes in an ASE db:
```py
from protosearch.build_bulk.oqmd_interface import OqmdInterface

O.store_enumeration(filename='FeO6.db',
                    chemical_formula='FeO6',
                    max_atoms=7,
                    fix_metal_ratio=False,
                    must_contain_nonmetal=False,
                    max_candidates=1)

```

## Enumerating crystal structures from theoretical prototypes:

This part of the code depends on the prototype Bulk Enumerator,
accessible upon request from Ankit Jain at `a_jain@iitb.ac.in`

Storing prototypes in an ASE db:

```py
from protosearch.build_bulk.enumeration import Enumeration, AtomsEnumeration

E = Enumeration("1_2",
                num_start=1,  # min number of atoms or wyckoffs
                num_end=3,  # max number of atoms or wyckoffs
                SG_start=20,  # first spacegroup, default is 1
                SG_end=22,  # last space group, default is 230
                num_type='atom'  # 'atom' or 'wyckoff'
                )
E.store_enumeration('1_2.db')
E = AtomsEnumeration(elements={'A': ['Fe'],
                               'B': ['O']},
                     spacegroups=[21])
E.store_atom_enumeration('1_2.db')


## Complete Active learnig loop

So far, this part requires access to TRI AWS computing resources

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