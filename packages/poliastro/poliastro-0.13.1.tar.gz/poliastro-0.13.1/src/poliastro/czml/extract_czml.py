from typing import Any, List

import numpy as np
from astropy import units as u
from astropy.coordinates import CartesianRepresentation
from astropy.time import Time, TimeDelta
from czml3.core import Packet, Preamble
from czml3.enums import InterpolationAlgorithms, ReferenceFrames
from czml3.properties import (
    Billboard,
    Clock,
    Color,
    Label,
    Material,
    Path,
    Position,
    SolidColorMaterial,
)
from czml3.types import IntervalValue, TimeInterval

from poliastro.czml.utils import ellipsoidal_to_cartesian
from poliastro.twobody.propagation import propagate

PIC_SATELLITE = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAADJSURBVDhPnZHRDcMgEEMZjVEYpaNklIzSEfLfD4qNnXAJSFWfhO7w2Zc0Tf9QG2rXrEzSUeZLOGm47WoH95x3Hl3jEgilvDgsOQUTqsNl68ezEwn1vae6lceSEEYvvWNT/Rxc4CXQNGadho1NXoJ+9iaqc2xi2xbt23PJCDIB6TQjOC6Bho/sDy3fBQT8PrVhibU7yBFcEPaRxOoeTwbwByCOYf9VGp1BYI1BA+EeHhmfzKbBoJEQwn1yzUZtyspIQUha85MpkNIXB7GizqDEECsAAAAASUVORK5CYII="
PIC_GROUNDSTATION = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAACvSURBVDhPrZDRDcMgDAU9GqN0lIzijw6SUbJJygUeNQgSqepJTyHG91LVVpwDdfxM3T9TSl1EXZvDwii471fivK73cBFFQNTT/d2KoGpfGOpSIkhUpgUMxq9DFEsWv4IXhlyCnhBFnZcFEEuYqbiUlNwWgMTdrZ3JbQFoEVG53rd8ztG9aPJMnBUQf/VFraBJeWnLS0RfjbKyLJA8FkT5seDYS1Qwyv8t0B/5C2ZmH2/eTGNNBgMmAAAAAElFTkSuQmCC"


class CZMLExtractor:
    """A class for extracting orbitary data to Cesium"""

    def __init__(
        self, start_epoch, end_epoch, N, ellipsoid=None, pr_map=None, scene3D=True
    ):
        """
        Orbital constructor

        Parameters
        ----------
        start_epoch: ~astropy.time.core.Time
            Starting epoch
        end_epoch: ~astropy.time.core.Time
            Ending epoch
        N: int
            Default number of sample points.
            Unless otherwise specified, the number
            of sampled data points will be N when calling
            add_orbit()
        scene3D: bool
            Determines the scene mode. If set to true, the scene
            is set to 3D mode, otherwise it's the orthographic
            projection.
        """
        self.packets = []  # type: List[Packet]

        self.cust_prop = [ellipsoid, pr_map, scene3D]

        self.orbits = []  # type: List[Any]
        self.N = N
        self.i = 0
        self.gs_n = 0

        self.start_epoch = Time(start_epoch, format="isot")
        self.end_epoch = Time(end_epoch, format="isot")

        self._init_czml_()

        self._change_custom_params(*self.cust_prop)

    def _init_orbit_packet_cords_(self, i, rtol):
        """

        Parameters
        ----------
        i: int
            Index of referenced orbit
        rtol: float
            Maximum relative error permitted
        Returns
        -------
        coordinate list
        """
        cart_cords = []  # type: List[float]

        h = (self.end_epoch - self.orbits[i][2]).to(u.second) / self.orbits[i][1]

        # Get rounding factor given the relative tolerance
        rf = 0
        while rtol < 1:
            rtol *= 10
            rf += 1

        for k in range(self.orbits[i][1] + 2):
            position = propagate(self.orbits[i][0], TimeDelta(k * h), rtol=rtol)

            cords = position.represent_as(CartesianRepresentation).xyz.to(u.meter).value
            cords = np.insert(cords, 0, h.value * k, axis=0)

            # flatten list
            cart_cords += list(map(lambda x: round(x[0], rf), cords.tolist()))

        return cart_cords

    def _init_czml_(self):
        """
        Only called at the initialization of the extractor
        Builds packets.
        """
        pckt = Preamble(
            name="document_packet",
            clock=IntervalValue(
                start=self.start_epoch.value,
                end=self.end_epoch.value,
                value=Clock(currentTime=self.start_epoch.value, multiplier=60),
            ),
        )
        self.packets.append(pckt)

    def _change_custom_params(self, ellipsoid, pr_map, scene3D):
        """
        Change the custom properties package.
        Parameters
        ----------
        ellipsoid: list(int)
            Defines the attractor ellipsoid. The list must have three numbers
            representing the radii in the x, y and z axis
        pr_map: str
            A URL to the projection of the defined ellipsoid (UV map)
        """

        if ellipsoid is None:
            ellipsoid = [6378137.0, 6378137.0, 6356752.3142451793]
        if pr_map is None:
            pr_map = (
                "https://upload.wikimedia.org/wikipedia/commons/c/c4/Earthmap1000x500compac.jpg",
            )

        custom_props = {
            "custom_attractor": True,
            "ellipsoid": [{"array": ellipsoid}],
            "map_url": pr_map,
            "scene3D": scene3D,
        }

        pckt = Packet(id="custom_properties", properties=custom_props)

        self.packets.append(pckt)

    def add_ground_station(
        self,
        pos,
        id_description=None,
        label_fill_color=None,
        label_font=None,
        label_outline_color=None,
        label_text=None,
        label_show=True,
    ):
        """
        Adds a ground station

        Parameters
        ----------
        orbit: poliastro.Orbit
            Orbit to be added
        pos: list [~astropy.units]
            coordinates of ground station
            [u v] ellipsoidal coordinates (0 elevation)

        Id parameters:
        -------------

        id_description: str
            Set ground station description

        Label parameters
        ----------

        label_fill_color: list (int)
            Fill Color in rgba format
        label_outline_color: list (int)
            Outline Color in rgba format
        label_font: str
            Set label font style and size (CSS syntax)
        label_text: str
            Set label text
        label_show: bool
            Indicates whether the label is visible
        """
        if (
            len(pos) == 2
            and isinstance(pos[0], u.quantity.Quantity)
            and isinstance(pos[0], u.quantity.Quantity)
        ):
            u0, v0 = pos
            if self.cust_prop[0]:
                a, b = self.cust_prop[0][:1]  # get semi-major and semi-minor axises
            else:
                a, b = 6378137.0, 6378137.0
            pos = list(map(lambda x: x.value, ellipsoidal_to_cartesian(a, b, u0, v0)))
        else:
            raise TypeError(
                "Invalid coordinates. Coordinates must be of the form [u, v] where u, v are astropy units"
            )

        pckt = Packet(
            id="GS" + str(self.gs_n),
            description=id_description,
            availability=TimeInterval(start=self.start_epoch, end=self.end_epoch),
            position=Position(cartesian=pos),
            label=Label(
                show=label_show,
                text=label_text,
                font=label_font if label_font is not None else "11pt Lucida Console",
                fillColor=Color(rgba=label_fill_color)
                if label_fill_color is not None
                else None,
                outlineColor=Color(rgba=label_outline_color)
                if label_outline_color is not None
                else None,
            ),
            billboard=Billboard(image=PIC_GROUNDSTATION, show=True),
        )

        self.packets.append(pckt)
        self.gs_n += 1

    def add_orbit(
        self,
        orbit,
        rtol=1e-10,
        N=None,
        id_name=None,
        id_description=None,
        path_width=None,
        path_show=None,
        path_color=None,
        label_fill_color=None,
        label_outline_color=None,
        label_font=None,
        label_text=None,
        label_show=None,
    ):
        """
        Adds an orbit

        Parameters
        ----------
        orbit: poliastro.Orbit
            Orbit to be added
        rtol: float
            Maximum relative error permitted
        N: int
            Number of sample points

        Id parameters:
        -------------

        id_name: str
            Set orbit name
        id_description: str
            Set orbit description

        Path parameters
        ---------------

        path_width: int
            Path width
        path_show: bool
            Indicates whether the path is visible
        path_color: list (int)
            Rgba path color

        Label parameters
        ----------

        label_fill_color: list (int)
            Fill Color in rgba format
        label_outline_color: list (int)
            Outline Color in rgba format
        label_font: str
            Set label font style and size (CSS syntax)
        label_text: str
            Set label text
        label_show: bool
            Indicates whether the label is visible

        """

        if N is None:
            N = self.N

        if orbit.epoch < Time(self.start_epoch):
            orbit = orbit.propagate(self.start_epoch - orbit.epoch)
        elif orbit.epoch > Time(self.end_epoch):
            raise ValueError(
                "The orbit's epoch cannot exceed the constructor's ending epoch"
            )

        if rtol <= 0 or rtol >= 1:
            raise ValueError(
                "The relative tolerance must be a value in the range (0, 1)"
            )

        self.orbits.append([orbit, N, orbit.epoch])
        cartesian_cords = self._init_orbit_packet_cords_(self.i, rtol=rtol)

        start_epoch = Time(min(self.orbits[self.i][2], self.start_epoch), format="isot")

        pckt = Packet(
            id=self.i,
            name=id_name,
            description=id_description,
            availability=TimeInterval(start=self.start_epoch, end=self.end_epoch),
            position=Position(
                interpolationDegree=5,
                interpolationAlgorithm=InterpolationAlgorithms.LAGRANGE,
                referenceFrame=ReferenceFrames.INERTIAL,
                cartesian=cartesian_cords,
                epoch=start_epoch.value,
            ),
            path=Path(
                show=path_show,
                width=path_width,
                material=Material(
                    solidColor=SolidColorMaterial(color=Color(rgba=path_color))
                )
                if path_color is not None
                else Material(
                    solidColor=SolidColorMaterial(color=Color(rgba=[255, 255, 0, 255]))
                ),
                resolution=120,
            ),
            label=Label(
                text=label_text,
                font=label_font if label_font is not None else "11pt Lucida Console",
                show=label_show,
                fillColor=Color(rgba=label_fill_color)
                if label_fill_color is not None
                else Color(rgba=[255, 255, 0, 255]),
                outlineColor=Color(rgba=label_outline_color)
                if label_outline_color is not None
                else Color(rgba=[255, 255, 0, 255]),
            ),
            billboard=Billboard(image=PIC_SATELLITE, show=True),
        )

        self.packets.append(pckt)

        self.i += 1
