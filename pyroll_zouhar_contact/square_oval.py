import sys

from pyroll import RollPass, grooves


def suits(roll_pass: RollPass):
    return (
            (
                    isinstance(roll_pass.in_profile.groove, grooves.SquareGroove)
                    and
                    isinstance(roll_pass.groove, grooves.CircularOvalGroove)
            )
            or
            (
                    isinstance(roll_pass.in_profile.groove, grooves.SquareGroove)
                    and
                    isinstance(roll_pass.groove, grooves.FlattenedOvalGroove)
            )
    )


@RollPass.hookimpl
def zouhar_contact_c1(roll_pass: RollPass):
    if suits(roll_pass):
        return 0.82


@RollPass.hookimpl
def zouhar_contact_c2(roll_pass: RollPass):
    if suits(roll_pass):
        return 0.2


@RollPass.hookimpl
def zouhar_contact_c3(roll_pass: RollPass):
    if suits(roll_pass):
        return 1.02


@RollPass.hookimpl
def zouhar_contact_in_width(roll_pass: RollPass):
    if suits(roll_pass):
        return roll_pass.in_profile.rotated.width


RollPass.plugin_manager.register(sys.modules[__name__])
