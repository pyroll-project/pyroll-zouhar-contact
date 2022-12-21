from pyroll.core import RollPass


@RollPass.zouhar_contact_c1
def zouhar_contact_c1(self: RollPass):
    if "square" in self.in_profile.types and "oval" in self.types:
        return 0.82


@RollPass.zouhar_contact_c2
def zouhar_contact_c2(self: RollPass):
    if "square" in self.in_profile.types and "oval" in self.types:
        return 0.2


@RollPass.zouhar_contact_c3
def zouhar_contact_c3(self: RollPass):
    if "square" in self.in_profile.types and "oval" in self.types:
        return 1.02
