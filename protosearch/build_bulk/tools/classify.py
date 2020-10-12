from ase.io import read
from sys import argv
from protosearch.build_bulk.classification import PrototypeClassification

# Script to print structure prototype and parameters

atoms = read(argv[1])
PC = PrototypeClassification(atoms)

prototype, parameters = PC.get_classification()
print('Prototype:', prototype, '\nParameters:', parameters)
