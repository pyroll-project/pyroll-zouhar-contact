import sys

from pyroll import RollPass, grooves


def suits(roll_pass: RollPass):
    return (
            (
                    isinstance(roll_pass.in_profile.groove, grooves.DiamondGroove)
                    and
                    isinstance(roll_pass.groove, grooves.DiamondGroove)
            )
    )


@RollPass.hookimpl
def zouhar_contact_c2(roll_pass: RollPass):
    if suits(roll_pass):
        return 0.3


RollPass.plugin_manager.register(sys.modules[__name__])
