from pyroll.core import RollPass, Hook
from logging import getLogger

_log = getLogger(__name__)

RollPass.zouhar_contact_c1 = Hook[float]()
"""Get the value of the Zouhar C1 constant for the given roll pass."""

RollPass.zouhar_contact_c2 = Hook[float]()
"""Get the value of the Zouhar C2 constant for the given roll pass."""

RollPass.zouhar_contact_c3 = Hook[float]()
"""Get the value of the Zouhar C3 constant for the given roll pass."""

RollPass.zouhar_contact_in_width = Hook[float]()
"""Get the value of the incoming profile width for the given roll pass."""


@RollPass.zouhar_contact_c1
def default_zouhar_contact_c1(self: RollPass):
    return 1


@RollPass.zouhar_contact_c2
def default_zouhar_contact_c2(self: RollPass):
    return 0


@RollPass.zouhar_contact_c3
def default_zouhar_contact_c3(self: RollPass):
    return 1


@RollPass.zouhar_contact_in_width
def default_zouhar_contact_in_width(self: RollPass):
    return self.in_profile.width


@RollPass.Roll.contact_area
def contact_area(self: RollPass.Roll):
    roll_pass = self.roll_pass()
    if (
            roll_pass.zouhar_contact_c1 is not None
            and
            roll_pass.zouhar_contact_c2 is not None
            and
            roll_pass.zouhar_contact_c3 is not None
            and
            roll_pass.zouhar_contact_in_width is not None
    ):
        _log.debug(f"Used Zouhar contact model for roll pass {roll_pass.label}.")
        return (
                roll_pass.out_profile.width * roll_pass.zouhar_contact_c2
                + 0.5 * (
                        roll_pass.out_profile.width
                        + roll_pass.zouhar_contact_in_width * roll_pass.zouhar_contact_c1
                )
                * (1 - roll_pass.zouhar_contact_c2)
        ) * roll_pass.zouhar_contact_c3 * roll_pass.roll.contact_length


from . import (
    diamond_diamond,
    diamond_square,
    oval_square,
    round_oval,
    square_oval
)
