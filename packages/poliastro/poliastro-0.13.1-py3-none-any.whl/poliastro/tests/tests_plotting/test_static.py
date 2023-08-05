import astropy.units as u
import matplotlib.pyplot as plt
import pytest

from poliastro.bodies import Earth, Jupiter, Mars
from poliastro.examples import iss
from poliastro.plotting.static import StaticOrbitPlotter
from poliastro.twobody.orbit import Orbit


def test_orbitplotter_has_axes():
    ax = "Unused axes"
    op = StaticOrbitPlotter(ax)
    assert op.ax is ax


def test_set_frame():
    op = StaticOrbitPlotter()
    p = [1, 0, 0] * u.one
    q = [0, 1, 0] * u.one
    w = [0, 0, 1] * u.one
    op.set_frame(p, q, w)

    assert op._frame == (p, q, w)


def test_axes_labels_and_title():
    ax = plt.gca()
    op = StaticOrbitPlotter(ax)
    ss = iss
    op.plot(ss)

    assert ax.get_xlabel() == "$x$ (km)"
    assert ax.get_ylabel() == "$y$ (km)"


def test_number_of_lines_for_osculating_orbit():
    op1 = StaticOrbitPlotter()
    ss = iss

    l1 = op1.plot(ss)

    assert len(l1) == 2


def test_legend():
    op = StaticOrbitPlotter()
    ss = iss
    op.plot(ss, label="ISS")
    legend = plt.gca().get_legend()

    ss.epoch.out_subfmt = "date_hm"
    label = f"{ss.epoch.iso} (ISS)"

    assert legend.get_texts()[0].get_text() == label


def test_color():
    op = StaticOrbitPlotter()
    ss = iss
    c = "#FF0000"
    op.plot(ss, label="ISS", color=c)
    ax = plt.gca()

    assert ax.get_legend().get_lines()[0].get_c() == c
    for element in ax.get_lines():
        assert element.get_c() == c


def test_plot_trajectory_sets_label():
    op = StaticOrbitPlotter()
    earth = Orbit.from_body_ephem(Earth)
    mars = Orbit.from_body_ephem(Mars)
    trajectory = earth.sample()
    op.plot(mars, label="Mars")
    op.plot_trajectory(trajectory, label="Earth")
    legend = plt.gca().get_legend()
    assert legend.get_texts()[1].get_text() == "Earth"


def test_dark_mode_plots_dark_plot():
    op = StaticOrbitPlotter(dark=True)
    assert op.ax.get_facecolor() == (0.0, 0.0, 0.0, 1.0)
    op = StaticOrbitPlotter()
    assert op.ax.get_facecolor() == (1.0, 1.0, 1.0, 1)


def test_redraw_makes_attractor_none():
    # TODO: Review
    op = StaticOrbitPlotter()
    op._redraw()
    assert op._attractor_radius is not None


def test_set_frame_plots_same_colors():
    # TODO: Review
    op = StaticOrbitPlotter()
    jupiter = Orbit.from_body_ephem(Jupiter)
    op.plot(jupiter)
    colors1 = [orb[2] for orb in op.trajectories]
    op.set_frame(*jupiter.pqw())
    colors2 = [orb[2] for orb in op.trajectories]
    assert colors1 == colors2


def test_redraw_keeps_trajectories():
    # See https://github.com/poliastro/poliastro/issues/518
    op = StaticOrbitPlotter()
    earth = Orbit.from_body_ephem(Earth)
    mars = Orbit.from_body_ephem(Mars)
    trajectory = earth.sample()
    op.plot(mars, label="Mars")
    op.plot_trajectory(trajectory, label="Earth")

    assert len(op.trajectories) == 2

    op.set_frame(*mars.pqw())

    assert len(op.trajectories) == 2


@pytest.mark.mpl_image_compare
def test_trail_plotting():
    fig, ax = plt.subplots()
    plotter = StaticOrbitPlotter(ax=ax)
    plotter.plot(iss, trail=True)

    return fig
