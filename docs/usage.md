# Usage of the Plugin

Load the plugin with the module name `pyroll_zouhar_contact`.

## Coefficient Hooks

The plugin specifies hooks for the three coefficients as `zouhar_contact_c1`, `zouhar_contact_c2`
and `zouhar_contact_c3`. on `RollPass`. Default implementations of them result in $`C_1 = 1`$, $`C_2 = 0`$ and
$`C_3 = 1`$, which is essentially the trapezoidal rule.

For the pass types listed in the [model page](model.md), implementation are provided, which check for the type of the in
and out profiles.

## Initial Contact Width Hook

The plugin specifies a `zouhar_contact_in_width` hook on `RollPass`, to deliver the width of the initial contact $`b`$.
For the pass types listed in the [model page](model.md), implementation are provided, which check for the type of the in
and out profiles.

## Contact Area hook

The plugin provides an implementation of the `RollPass.contact_area` hook, which calculates the contact area according
to the [model](model.md) function. It asks the roll pass for coefficients and initial width. If one of these is not
available, the function returns `None`.