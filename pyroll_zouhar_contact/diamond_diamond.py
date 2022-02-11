import sys

from pyroll import RollPass, grooves
from pyroll.utils.hookutils import applies_to_in_grooves, applies_to_out_grooves


@RollPass.hookimpl
@applies_to_in_grooves(grooves.DiamondGroove)
@applies_to_out_grooves(grooves.DiamondGroove)
def zouhar_contact_c2(roll_pass: RollPass):
    return 0.3


RollPass.plugin_manager.register(sys.modules[__name__])
