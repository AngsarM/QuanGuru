from .customTypes import Matrix as Matrix
from .evolution import Unitary as Unitary
from .operators import Jx as Jx, Jy as Jy, Jz as Jz, identity as identity, sigmax as sigmax, sigmay as sigmay, sigmaz as sigmaz

def xRotation(angle: float, sparse: bool=...) -> Matrix: ...
def yRotation(angle: float, sparse: bool=...) -> Matrix: ...
def zRotation(angle: float, sparse: bool=...) -> Matrix: ...
def qubRotation(xyz: str, angle: float, sparse: bool=...) -> Matrix: ...
def spinRotation(xyz: str, angle: float, j: float, sparse: bool=..., isDim: bool=...) -> Matrix: ...
