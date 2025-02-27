from .customTypes import Matrix as Matrix
from .states import mat2Vec as mat2Vec, vec2Mat as vec2Mat

def nBarThermal(angFreq: float, temp: float, hbar: float=..., kb: float=...) -> float: ...
def qubitPolarisation(freq: float, temp: float) -> float: ...
def HeatCurrent(Lindbladian: Matrix, Hamiltonian: Matrix, denMat: Matrix) -> float: ...
