#Author: Elias Anderssen Dalan
#NOTE: There is definetly a better way to solve this problem, but it works for all problems provided in KJM3000
def calculate_fragments(exact_mass, tol = 1E-3, printFragments = True):
    """
    Parameters:
    -----------

    exact_mass: 
    Exact mass of the fragment obtained from mass spectrometry.

    Returns:
    --------

    fragments - A nested list containing sets of porrible fragment masses and their chemichal formulas.
    """
    #Exact mass of the most abundant isotopes opes the possible elements.
    mH = 1.007825
    mC = 12.0
    mO = 15.994915
    mS = 31.972074
    mCl = 34.968855

    #Number of possible elements inside of the fragment:

    nH = int(exact_mass / 2) + 2
    nC = nH
    nO = int(exact_mass / mO) + 1
    nS = int(exact_mass / mS) + 1
    nCl = int(exact_mass / mCl) + 1

    fragments = []
    elements = ["C", "H", "O", "S", "Cl"]

    for nh in range(nH):
        for nc in range(1, nC):
            for no in range(nO):
                for ns in range(nS):
                    for ncl in range(nCl):
                        fragment = nh * mH + nc * mC + no * mO + ns * mS + ncl * mCl 

                        if abs(fragment - exact_mass) < tol:
                            n_elements = [nc, nh, no, ns, ncl]
                            formula = f""
                            for el, n in zip(elements, n_elements):
                                if n != 0:
                                    formula += f"{el}{n}"
                            fragments.append([fragment, formula])

                            if printFragments:
                                print(f"{formula} with mass: {fragment}")
    return fragments