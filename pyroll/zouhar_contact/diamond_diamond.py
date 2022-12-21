from pyroll.core import RollPass


@RollPass.zouhar_contact_c2
def zouhar_contact_c2(self: RollPass):
    if "diamond" in self.in_profile.types and "diamond" in self.types:
        return 0.3
