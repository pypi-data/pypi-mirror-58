import pytest
from astropy import units as u
from astropy.tests.helper import assert_quantity_allclose

from poliastro.bodies import (
    Body,
    Earth,
    Jupiter,
    Mars,
    Mercury,
    Neptune,
    Saturn,
    Uranus,
    Venus,
)
from poliastro.threebody.soi import hill_radius, laplace_radius


@pytest.mark.parametrize(
    "body, expected_r_SOI",
    [
        (Mercury, 1.12e8),
        (Venus, 6.16e8),
        (Earth, 9.25e8),
        (Mars, 5.77e8),
        (Jupiter, 4.82e10),
        (Saturn, 5.48e10),
        (Uranus, 5.18e10),
        (Neptune, 8.66e10),
    ]
    # Data from Table A.2., Curtis "Orbital Mechanics for Engineering Students"
)
def test_laplace_radius(body, expected_r_SOI):
    if expected_r_SOI is not None:
        expected_r_SOI = expected_r_SOI * u.m

    r_SOI = laplace_radius(body)

    assert_quantity_allclose(r_SOI, expected_r_SOI, rtol=1e-1)


def test_laplace_radius_given_a():
    parent = Body(None, 1 * u.km ** 3 / u.s ** 2, "Parent")
    body = Body(parent, 1 * u.km ** 3 / u.s ** 2, "Body")
    r_SOI = laplace_radius(body, 1 * u.km)

    assert r_SOI == 1 * u.km


@pytest.mark.parametrize(
    "body, expected_r_SOI",
    [
        (Mercury, 2.24e8),
        (Venus, 1.03e9),
        (Earth, 1.49e9),
        (Mars, 1.07e9),
        (Jupiter, 5.28e10),
        (Saturn, 6.50e10),
        (Uranus, 7.01e10),
        (Neptune, 1.16e11),
    ],
)
def test_hill_radius(body, expected_r_SOI):
    if expected_r_SOI is not None:
        expected_r_SOI = expected_r_SOI * u.m

    r_SOI = hill_radius(body, e=0 * u.one)

    assert_quantity_allclose(r_SOI, expected_r_SOI, rtol=1e-1)


def test_hill_radius_given_a():
    parent = Body(None, 1 * u.km ** 3 / u.s ** 2, "Parent")
    body = Body(parent, 1 * u.km ** 3 / u.s ** 2, "Body")
    r_SOI = hill_radius(body, 1 * u.km, 0.25 * u.one)
    expected_r_SOI = 520.02096 * u.m
    assert_quantity_allclose(r_SOI, expected_r_SOI, rtol=1e-8)
