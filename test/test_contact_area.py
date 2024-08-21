import numpy as np
from shapely.geometry import Polygon
from pyroll.core import Profile, PassSequence, RollPass, Roll, CircularOvalGroove, ThreeRollPass


def test_plotted_contact_area():
    import pyroll.zouhar_contact

    p: Profile = Profile.round(
        diameter=30e-3,
        temperature=1200 + 273.15,
        strain=0,
        material=["C45", "steel"],
        flow_stress=100e6
    )

    ps: PassSequence = PassSequence(
        [
            RollPass(
                label="Oval I",
                roll=Roll(
                    groove=CircularOvalGroove(
                        depth=8e-3,
                        r1=6e-3,
                        r2=40e-3
                    ),
                    nominal_radius=160e-3,
                    rotational_frequency=1
                ),
                gap=2e-3
            )])

    ps.solve(p)
    rp = ps[0]

    coords = (
        (-rp.out_profile.width / 2, 0),
        (-rp.out_profile.width / 2, rp.roll.contact_length * rp.zouhar_contact_c2),
        (-rp.zouhar_contact_in_width * rp.zouhar_contact_c1 / 2, rp.roll.contact_length),
        (rp.zouhar_contact_in_width * rp.zouhar_contact_c1 / 2, rp.roll.contact_length),
        (rp.out_profile.width / 2, rp.roll.contact_length * rp.zouhar_contact_c2),
        (rp.out_profile.width / 2, 0),
        (-rp.out_profile.width / 2, 0)
    )

    area_from_zouhar = rp.roll.contact_area
    area_as_poly = Polygon(coords)

    assert np.isclose(area_from_zouhar, area_as_poly.area, rtol=1e-3)


def test_plotted_contact_area_3fold():
    import pyroll.zouhar_contact

    p: Profile = Profile.round(
        diameter=20e-3,
        temperature=1200 + 273.15,
        material=["C45", "Steel"],
        length=1,
        flow_stress=100e6
    )

    ps: PassSequence = PassSequence(
        [
            ThreeRollPass(
                label="Pass1",
                roll=Roll(
                    groove=CircularOvalGroove(
                        r1=1e-3,
                        r2=12e-3,
                        depth=3.3e-3,
                        pad_angle=30
                    ),
                    nominal_radius=150e-3,
                    rotational_frequency=1,
                ),
                inscribed_circle_diameter=18e-3
            )])

    ps.solve(p)
    rp = ps[0]

    out_width = rp.out_profile.contact_lines[1].width

    coords = (
        (-out_width / 2, 0),
        (-out_width / 2, rp.roll.contact_length * rp.zouhar_contact_c2),
        (-rp.zouhar_contact_in_width * rp.zouhar_contact_c1 / 2, rp.roll.contact_length),
        (rp.zouhar_contact_in_width * rp.zouhar_contact_c1 / 2, rp.roll.contact_length),
        (out_width / 2, rp.roll.contact_length * rp.zouhar_contact_c2),
        (out_width / 2, 0),
        (-out_width / 2, 0)
    )

    area_from_zouhar = rp.roll.contact_area
    area_as_poly = Polygon(coords)

    assert np.isclose(area_from_zouhar, area_as_poly.area, rtol=1e-3)


test_plotted_contact_area()

test_plotted_contact_area_3fold()
