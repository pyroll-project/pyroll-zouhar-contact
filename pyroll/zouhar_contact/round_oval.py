from pyroll.core import RollPass


@RollPass.zouhar_contact_c1
def zouhar_contact_c1(self: RollPass):
    if "round" in self.in_profile.types and "oval" in self.types:
        return 0.45


@RollPass.zouhar_contact_c2
def zouhar_contact_c2(self: RollPass):
    if "round" in self.in_profile.types and "oval" in self.types:
        return 0.18
