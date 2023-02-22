import numpy as np 
import scipy as sp

"""
This is an attempt at a Hartree-Fock solver for any type of quantum system. You can find information about the theory behind
this code in a notebook also located in this repository.
If you want to use it you will need to provide an xyz-file describing
the atoms positions in your system. The file needs to be formatted like
this:

N_atoms
Atom_name (this is optional)
atom_one x_atom_one y_atom_one z_atom_one
atom_two x_atom_two y_atom_two z_atom_two
...
"""

def read_xyz(file_name):
    """
    Reads an xyz file.

    Parameters:
    -----------
    file_name - the path to the xyz-file.

    Returns:
    --------
    n_atoms: The number of atoms
    atom_type: List containing the different atom species.
    atom_positions: Matrix containing the atoms positions. atom_positions[i] returns positions to corresponding atom_type[i].
    molecule_name: This is optional. If it is empty it will return nothing.
    """
    file = open(file_name)


    for i, line in enumerate(file):
        if i == 0:
            try:
                n_atoms = int(line)
                atom_type = []
                atom_positions = np.zeros((n_atoms, 3))
            except:
                print("Something went wrong! Are you sure you your file is formatted right?")
        elif i == 1:
            if line == "":
                molecule_name = None
            else:
                molecule_name = line.split()[0] 
        else:
            words = line.split()
            atom_type.append(words[0])
            atom_pos = [float(words[j]) for j in range(1, 4)]
            atom_pos = np.array(atom_pos)
            atom_positions[i-2] = atom_pos

    if molecule_name == None:
        return n_atoms, atom_type, atom_positions 
    
    else:
        return n_atoms, atom_type, atom_positions, molecule_name

def translate_to_PYSCF(atom_types, atom_positions):
    """
    After reading atom positions from an xyz file this function will translate it into the string you have to pass into pyscf if
    you want to build a molecule. This is how you build a molecule:

    from pyscf import gto

    gto.M(atom = position_string, ...)

    Parameters:
    -----------
    atom_types: list of atoms got from using read_xyz.
    atom_positions: array of atom positions. atom_positions[i] contains a 3d vector with xyz-positions corresponding to atom_types[i]

    Returns:
    --------
    position_string: the string you pass into pyscf when building a molecule.
    """

    position_string = ""

    for atom_type, atom_pos in zip(atom_types, atom_positions):
        position_string += f"{atom_type} {atom_pos[0]} {atom_pos[1]} {atom_pos[2]}; "
    
    #Need to remove the last "; " for it to work in pySCF.
    position_string = [position_string[i] for i in range(0, len(position_string) - 2)]

    return position_string

n_atoms, atom_type, atom_positions, molecule_name = read_xyz("HeH.txt")
