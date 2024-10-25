import logging
import webbrowser
from pathlib import Path
from pyroll.core import Profile, Roll, ThreeRollPass, Transport, RoundGroove, CircularOvalGroove, PassSequence


def test_solve_min(tmp_path: Path, caplog):
    caplog.set_level(logging.DEBUG, logger="pyroll")

    import pyroll.zouhar_contact

    in_profile = Profile.round(
        diameter=20e-3,
        temperature=1200 + 273.15,
        strain=0,
        material=["C45", "steel"],
        flow_stress=100e6
    )

    sequence = PassSequence(
        [
            ThreeRollPass(
                label="Oval I",
                roll=Roll(
                    groove=CircularOvalGroove(
                        r1=1e-3,
                        r2=12e-3,
                        depth=3.3e-3,
                        pad_angle=30
                    ),
                    nominal_radius=160e-3,
                    rotational_frequency=1
                ),
                inscribed_circle_diameter=18e-3,
            ),
            Transport(
                label="I => II",
                duration=1
            ),
            ThreeRollPass(
                label="Round II",
                roll=Roll(
                    groove=RoundGroove(
                        r1=1e-3,
                        r2=8.9e-3,
                        depth=3.9e-3,
                        pad_angle=30
                    ),
                    nominal_radius=160e-3,
                    rotational_frequency=1
                ),
                inscribed_circle_diameter=17.5e-3,
            ),
        ]
    )

    try:
        sequence.solve(in_profile)
    finally:
        print("\nLog:")
        print(caplog.text)

    assert sequence[0].has_cached("zouhar_contact_c1")

    try:
        from pyroll.report import report

        report = report(sequence)
        f = tmp_path / "report.html"
        f.write_text(report, encoding="utf-8")
        webbrowser.open(f.as_uri())

    except ImportError:
        pass
