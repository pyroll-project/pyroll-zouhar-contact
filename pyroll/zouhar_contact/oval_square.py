from pyroll.core import RollPass


@RollPass.zouhar_contact_c2
def zouhar_contact_c2(self: RollPass):
    if "oval" in self.in_profile.types and "square" in self.types:
        return 0.1


@RollPass.zouhar_contact_in_width
def zouhar_contact_in_width(self: RollPass):
    if "oval" in self.in_profile.types and "square" in self.types:
        return self.in_profile.local_width(self.in_profile.height / 2)
