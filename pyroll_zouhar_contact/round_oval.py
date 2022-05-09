from pyroll import RollPass
from pyroll import for_in_profile_types, for_out_profile_types


@RollPass.hookimpl
@for_in_profile_types("round")
@for_out_profile_types("oval")
def zouhar_contact_c1(roll_pass: RollPass):
    return 0.45


@RollPass.hookimpl
@for_in_profile_types("round")
@for_out_profile_types("oval")
def zouhar_contact_c2(roll_pass: RollPass):
    return 0.18
