import sys

from pyroll import RollPass, grooves


def suits(roll_pass: RollPass):
    return (
            (
                    isinstance(roll_pass.in_profile.groove, grooves.CircularOvalGroove)
                    and
                    isinstance(roll_pass.groove, grooves.SquareGroove)
            )
            or
            (
                    isinstance(roll_pass.in_profile.groove, grooves.FlattenedOvalGroove)
                    and
                    isinstance(roll_pass.groove, grooves.SquareGroove)
            )
    )


@RollPass.hookimpl
def zouhar_contact_c2(roll_pass: RollPass):
    if suits(roll_pass):
        return 0.1


RollPass.plugin_manager.register(sys.modules[__name__])
