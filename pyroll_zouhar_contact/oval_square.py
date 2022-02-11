import sys

from pyroll import RollPass, grooves
from pyroll.utils.hookutils import applies_to_in_grooves, applies_to_out_grooves


@RollPass.hookimpl
@applies_to_in_grooves(grooves.FlattenedOvalGroove, grooves.CircularOvalGroove, grooves.Oval3RadiiGroove)
@applies_to_out_grooves(grooves.SquareGroove)
def zouhar_contact_c2(roll_pass: RollPass):
    return 0.1


RollPass.plugin_manager.register(sys.modules[__name__])
