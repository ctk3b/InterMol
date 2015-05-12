import simtk.unit as units

from intermol.decorators import accepts_compatible_units
from intermol.forces.abstract_bond_type import AbstractBondType


class QuarticBreakableBondType(AbstractBondType):
    __slots__ = ['k', 'B1', 'B2', 'Rc', 'U0', 'order', 'c']

    @accepts_compatible_units(None, None, 
                              k=units.kilojoules_per_mole * units.nanometers ** (-4),
                              B1=units.nanometers,
                              B2=units.nanometers,
                              Rc=units.nanometers,
                              U0=units.kilojoules_per_mole,
                              order=None,
                              c=None)
    def __init__(self, bondingtype1, bondingtype2, 
                 k=0.0 * units.kilojoules_per_mole * units.nanometers ** (-4),
                 B1=0.0 * units.nanometers,
                 B2=0.0 * units.nanometers,
                 Rc=0.0 * units.nanometers,
                 U0=0.0 * units.kilojoules_per_mole,
                 order=1, c=False):
        AbstractBondType.__init__(self, bondingtype1, bondingtype2, order, c)
        self.k = k
        self.B1 = B1
        self.B2 = B2
        self.Rc = Rc
        self.U0 = U0
