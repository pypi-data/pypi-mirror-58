"""
********************************************************************************
compas_rhino.artists
********************************************************************************

.. currentmodule:: compas_rhino.artists

Artists for visualising (painting) COMPAS objects in Rhino.

Primitive Artists
=================

.. autosummary::
    :toctree: generated/
    :nosignatures:

    PointArtist
    LineArtist
    FrameArtist


Shape Artists
=============

.. autosummary::
    :toctree: generated/
    :nosignatures:

    BoxArtist


Data Structure Artists
======================

.. autosummary::
    :toctree: generated/
    :nosignatures:

    MeshArtist
    NetworkArtist
    VolMeshArtist

"""
from __future__ import absolute_import

from .artist import Artist

from .primitiveartist import PrimitiveArtist  # noqa: F401
from .pointartist import PointArtist
from .lineartist import LineArtist
from .frameartist import FrameArtist
from .networkartist import *  # noqa: F401 F403
from .meshartist import *  # noqa: F401 F403
from .volmeshartist import *  # noqa: F401 F403
from .boxartist import *  # noqa: F401 F403

from compas.geometry import Frame
from compas.geometry import Line
from compas.geometry import Point
from compas.geometry import Box
from compas.datastructures import Mesh

Artist.register(Point, PointArtist)
Artist.register(Frame, FrameArtist)
Artist.register(Line, LineArtist)
Artist.register(Box, LineArtist)
Artist.register(Mesh, LineArtist)

__all__ = [name for name in dir() if not name.startswith('_')]
