import simtk.unit as units

from intermol.decorators import accepts_compatible_units
from intermol.forces.abstract_bond_type import AbstractBondType


class QuarticBondType(AbstractBondType):
    __slots__ = ['length', 'C2', 'C3', 'C4', 'order', 'c']

    @accepts_compatible_units(None, None, 
                              length=units.nanometers,
                              C2=units.kilojoules_per_mole * units.nanometers ** (-2),
                              C3=units.kilojoules_per_mole * units.nanometers ** (-3),
                              C4=units.kilojoules_per_mole * units.nanometers ** (-4),
                              order=None,
                              c=None)
    def __init__(self, bondingtype1, bondingtype2, 
                 length=0.0 * units.nanometers,
                 C2=0.0 * units.kilojoules_per_mole * units.nanometers ** (-2),
                 C3=0.0 * units.kilojoules_per_mole * units.nanometers ** (-3),
                 C4=0.0 * units.kilojoules_per_mole * units.nanometers ** (-4),
                 order=1, c=False):
        AbstractBondType.__init__(self, bondingtype1, bondingtype2, order, c)
        self.length = length
        self.C2 = C2
        self.C3 = C3
        self.C4 = C4


class QuarticBond(QuarticBondType):
    """
    stub documentation
    """
    def __init__(self, atom1, atom2, bondingtype1=None, bondingtype2=None, 
                 length=0.0 * units.nanometers,
                 C2=0.0 * units.kilojoules_per_mole * units.nanometers ** (-2),
                 C3=0.0 * units.kilojoules_per_mole * units.nanometers ** (-3),
                 C4=0.0 * units.kilojoules_per_mole * units.nanometers ** (-4),
                 order=1, c=False):
        self.atom1 = atom1
        self.atom2 = atom2
        QuarticBondType.__init__(self, bondingtype1, bondingtype2, 
                length=length,
                C2=C2,
                C3=C3,
                C4=C4,
                order=order, c=c)