import numpy

from dichalcogenides.dichalcogenide import UpperValenceBand

class Superconductor():
    """Superconductor.

    Uses upper valence band energies by default.
    """

    def __init__(self, model, energy=None):
        self.model = model
        if not energy: self._energy = UpperValenceBand(self.model)

    @property
    def model(self):
        """The model for this superconductor.

        :return: The model.
        :rtype: Model
        """
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def Δk(self):
        """The superconducting parameter :math:`Δ_\\mathbf{k}`
        as a function of the energy :math:`E`.

        :return: :math:`Δ(E)`
        :rtype: func
        """
        # pylint: disable=no-self-use
        raise NotImplementedError

    @property
    def μ(self):
        return self._energy.μ

    @property
    def λk_bounds(self):
        ξ = self._energy.ξ_bounds
        return lambda Δk: (-10 * Δk, 10 * Δk)

    @property
    def ξ(self):
        return lambda Δk, λk: numpy.sqrt(λk**2 - Δk**2)

    def trig(self, name):
        ξ = self.ξ

        fn = {}
        fn['sin 2β'] = lambda Δk, λk: - abs(Δk) / λk
        fn['cos 2β'] = lambda Δk, λk: - ξ(Δk, λk) / λk
        fn['sin^2 β'] = lambda Δk, λk: (1 / 2) * (1 - ξ(Δk, λk) / λk)
        fn['cos^2 β'] = lambda Δk, λk: (1 / 2) * (1 + ξ(Δk, λk) / λk)

        return fn[name]

    def trig_e(self, name):
        μ = self.μ
        Δk = self.Δk
        λk = lambda e: numpy.sqrt((e - μ)**2 + Δk(e))
        return lambda e: self.trig(name)(Δk(e), λk(e))