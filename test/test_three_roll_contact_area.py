import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
import pytest
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

import pyroll.core as pr


@pytest.fixture(scope="module")
def main_fig():
    fig = make_subplots(rows=2, cols=4)
    yield fig
    fig.update_layout(title="Contact Areas for Different Profiles")
    fig.show()


@pytest.fixture(scope="module", autouse=True)
def subplot_index():
    index = {'count': 0}
    yield index


ips = {
    "round": pr.Profile.round(diameter=20e-3, temperature=1200 + 273.15, material=["C45", "Steel"], length=1, flow_stress=100e6)
}

gs = {
    "flat": pr.FlatGroove(usable_width=20e-3, pad_angle=30),
    "oval1": pr.CircularOvalGroove(r1=1e-3, r2=12e-3, depth=3.3e-3, pad_angle=30),
    "oval2": pr.CircularOvalGroove(r1=1e-3, r2=12e-3, depth=3.3e-3, pad_angle=30),
    "round1": pr.RoundGroove(r1=1e-3, r2=9.6e-3, depth=4.3e-3, pad_angle=30),
    "round2": pr.RoundGroove(r1=1e-3, r2=8.9e-3, depth=3.9e-3, pad_angle=30),
}

combinations = [
    (gs["flat"], gs["flat"], ips["round"]),
    (gs["oval1"], gs["oval2"], ips["round"]),
    (gs["round1"], gs["round2"], ips["round"]),
    (gs["round1"], gs["oval2"], ips["round"]),
    (gs["round1"], gs["flat"], ips["round"]),
    (gs["oval1"], gs["flat"], ips["round"]),
    (gs["round1"], gs["flat"], ips["round"]),
    (gs["oval1"], gs["flat"], ips["round"]),
]


@pytest.mark.parametrize("g_one, g_two, ip", combinations)
def test_plot_contact_areas(g_one, g_two, ip, main_fig, subplot_index):

    import pyroll.zouhar_contact

    ps = pr.PassSequence([
        pr.ThreeRollPass(
            label="Pass1",
            roll=pr.Roll(
                groove=g_one,
                nominal_radius=150e-3,
                rotational_frequency=1,
            ),
            inscribed_circle_diameter=18e-3
        ),
        pr.ThreeRollPass(
            label="Pass2",
            roll=pr.Roll(
                groove=g_two,
                nominal_radius=150e-3,
                rotational_frequency=1,
            ),
            inscribed_circle_diameter=17e-3
        )
    ])

    rp = ps.solve(ip)

    assert ps[0].has_cached("zouhar_contact_c1")

    fig = ps[-1].plot()

    ca = contact_area(ps[-1])
    x_coords, y_coords = ca.exterior.xy

    x_coords = list(x_coords)
    y_coords = list(y_coords)

    fig.add_trace(go.Scatter(
        x=x_coords,
        y=y_coords,
        mode="lines",
        fill="toself",
        line=dict(color="green"),
        fillcolor="rgba(0, 255, 0, 0.3)",
        name="Contact Area"
    ))

    idx = subplot_index['count']
    row = (idx // 4) + 1
    col = (idx % 4) + 1

    subplot_index['count'] += 1

    for trace in fig.data:
        main_fig.add_trace(trace, row=row, col=col)

    area_from_zouhar = ps[-1].roll.contact_area

    assert np.isclose(area_from_zouhar, ca.area, rtol=1e-3)


def contact_area(rp):
    out_width = rp.out_profile.contact_lines.geoms[1].width

    coords = (
        (-out_width / 2, - rp.roll.contact_length / 2),
        (-out_width / 2, rp.roll.contact_length * rp.zouhar_contact_c2 - rp.roll.contact_length / 2),
        (-rp.zouhar_contact_in_width * rp.zouhar_contact_c1 / 2, rp.roll.contact_length / 2),
        (rp.zouhar_contact_in_width * rp.zouhar_contact_c1 / 2, rp.roll.contact_length / 2),
        (out_width / 2, rp.roll.contact_length * rp.zouhar_contact_c2 - rp.roll.contact_length / 2),
        (out_width / 2, -rp.roll.contact_length / 2),
        (-out_width / 2, -rp.roll.contact_length / 2)
    )

    return Polygon(coords)
