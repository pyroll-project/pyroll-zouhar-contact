import sys

from pyroll import RollPass, grooves
from pyroll.utils.hookutils import applies_to_in_grooves, applies_to_out_grooves


@RollPass.hookimpl
@applies_to_in_grooves(grooves.RoundGroove)
@applies_to_out_grooves(grooves.OvalGrooveBase)
def zouhar_contact_c1(roll_pass: RollPass):
    return 0.45


@RollPass.hookimpl
@applies_to_in_grooves(grooves.RoundGroove)
@applies_to_out_grooves(grooves.OvalGrooveBase)
def zouhar_contact_c2(roll_pass: RollPass):
    return 0.18


RollPass.plugin_manager.register(sys.modules[__name__])
