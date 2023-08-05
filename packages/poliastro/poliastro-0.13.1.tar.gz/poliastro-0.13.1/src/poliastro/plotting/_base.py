from collections import namedtuple
from itertools import cycle
from typing import List

import numpy as np
import plotly.colors
from astropy import units as u
from astropy.coordinates import CartesianRepresentation
from plotly.graph_objects import Figure

from poliastro.plotting.util import BODY_COLORS, generate_label
from poliastro.util import norm


class Trajectory(namedtuple("Trajectory", ["trajectory", "state", "label", "color"])):
    pass


class BaseOrbitPlotter:
    """
    Parent Class for the 2D and 3D OrbitPlotter Classes based on Plotly.
    """

    def __init__(self, figure=None):
        self._figure = figure or Figure()
        self._layout = None

        self._trajectories = []  # type: List[Trajectory]

        self._attractor = None
        self._attractor_radius = np.inf * u.km

        self._color_cycle = cycle(plotly.colors.DEFAULT_PLOTLY_COLORS)

    @property
    def trajectories(self):
        return self._trajectories

    def _set_attractor(self, attractor):
        if self._attractor is None:
            self._attractor = attractor
        elif attractor is not self._attractor:
            raise NotImplementedError(
                f"Attractor has already been set to {self._attractor.name}."
            )

    def set_attractor(self, attractor):
        """Sets plotting attractor.

        Parameters
        ----------
        attractor : ~poliastro.bodies.Body
            Central body.

        """
        self._set_attractor(attractor)

    def _redraw_attractor(self):
        # Select a sensible value for the radius: realistic for low orbits,
        # visible for high and very high orbits
        min_radius = min(
            [
                trajectory.represent_as(CartesianRepresentation).norm().min() * 0.15
                for trajectory, _, _, _ in self._trajectories
            ]
            or [0 * u.m]
        )
        radius = max(self._attractor.R.to(u.km), min_radius.to(u.km))
        # TODO: Remove previously plotted sphere?
        self._plot_sphere(
            radius,
            BODY_COLORS.get(self._attractor.name, "#999999"),
            self._attractor.name,
        )

        self._attractor_radius = radius

    def _plot_point(self, radius, color, name, center=None):
        raise NotImplementedError

    def _plot_sphere(self, radius, color, name, center=None):
        raise NotImplementedError

    def plot_trajectory(self, trajectory, *, label=None, color=None):
        """Plots a precomputed trajectory.

        An attractor must be set first.

        Parameters
        ----------
        trajectory : ~astropy.coordinates.CartesianRepresentation
            Trajectory to plot.
        label : string, optional
        color : string, optional

        """
        if self._attractor is None:
            raise ValueError(
                "An attractor must be set up first, please use "
                "set_attractor(Major_Body) or plot(orbit)."
            )
        else:
            if color is None:
                color = next(self._color_cycle)

            trace = self._plot_trajectory(trajectory, str(label), color, False)

            self._trajectories.append(
                Trajectory(trajectory, None, label, trace.line.color)
            )

        if not self._figure._in_batch_mode:
            return self.show()

    def _plot_trajectory(self, trajectory, label, color, dashed):
        raise NotImplementedError

    def plot(self, orbit, *, label=None, color=None):
        """Plots state and osculating orbit in their plane.

        Parameters
        ----------
        orbit : ~poliastro.twobody.orbit.Orbit
            Orbit to plot.
        label : string, optional
            Label of the orbit.
        color : string, optional
            Color of the line and the position.

        """
        if color is None:
            color = next(self._color_cycle)

        self._set_attractor(orbit.attractor)

        label = generate_label(orbit, label)
        trajectory = orbit.sample()

        trace = self._plot_trajectory(trajectory, label, color, True)

        self._trajectories.append(
            Trajectory(trajectory, orbit.r, label, trace.line.color)
        )

        # Redraw the attractor now to compute the attractor radius
        self._redraw_attractor()

        # Plot required 2D/3D shape in the position of the body
        radius = min(
            self._attractor_radius * 0.5, (norm(orbit.r) - orbit.attractor.R) * 0.5
        )  # Arbitrary thresholds
        self._plot_point(radius, color, label, center=orbit.r)

        if not self._figure._in_batch_mode:
            return self.show()

    def _prepare_plot(self):
        if self._attractor is not None:
            self._redraw_attractor()

        self._figure.layout.update(self._layout)

    def show(self):
        """Shows the plot in the Notebook.

        Updates the layout and returns the underlying figure.

        """
        self._prepare_plot()
        return self._figure
