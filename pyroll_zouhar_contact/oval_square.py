import sys

from pyroll import RollPass, grooves
from pyroll.utils.hookutils import applies_to_in_grooves, applies_to_out_grooves


@RollPass.hookimpl
@applies_to_in_grooves(grooves.OvalGrooveBase)
@applies_to_out_grooves(grooves.SquareGroove)
def zouhar_contact_c2(roll_pass: RollPass):
    return 0.1


@RollPass.hookimpl
@applies_to_in_grooves(grooves.OvalGrooveBase)
@applies_to_out_grooves(grooves.SquareGroove)
def zouhar_contact_in_width(roll_pass: RollPass):
    return roll_pass.in_profile.gap


RollPass.plugin_manager.register(sys.modules[__name__])
