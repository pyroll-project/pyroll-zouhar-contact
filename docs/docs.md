---
title: The PyRoll Zouhar Contact Model Plugin  
author: [Max Weiner, Christoph Renzing]  
date: 2023-02-07
---

## The Zouhar approach to contact areas

The simplest method to estimate contact areas in elongation groove rolling is to use a trapezoid. However, this method
is quite inaccurate. Zouhar extended this method by applying several empirical correction coefficients dependent on the
pass type. His function for the contact area is:

$$ A_{\mathrm{d}} = \left[ b_1 C_2 + \frac{1}{2} \left( b_1 + b C_1 \right) \left( 1 - C_2 \right) \right] C_3 L_
{\mathrm{d}} $$

This function includes three empirical coefficients $L_i$, the contact length $L_{\mathrm{d}}$, the out profile width
$b_1$ and the initial contact width $b$. For $C_1 = 1$, $C_2 = 0$ and $C_3 = 1$ the model collapses to the trapezoidal
rule. The initial contact width $b$ for some pass types approximated with the roll gap of the last roll $s_0$, since the
profile first contacts mainly with its tip. For other types it is just the width of the rotated profile $b_0$.

Zouhar gave the following coefficients:

| In      | Out     | $b$   | $C_1$ | $C_2$ | $C_3$ |
|---------|---------|-------|-------|-------|-------|
| diamond | diamond | $s_0$ | 1     | 0.3   | 1     |
| diamond | square  | $s_0$ | 1     | 0.28  | 1     |
| square  | diamond | $s_0$ | 1     | 0.28  | 1     |
| oval    | square  | $s_0$ | 1     | 0.1   | 1     |
| square  | oval    | $b_0$ | 0.82  | 0.2   | 1.02  |
| round   | oval    | $b_0$ | 0.45  | 0.18  | 1     |
| oval    | round   | $s_0$ | 1     | 0     | 1     |

## Usage of the Plugin

Load the plugin with the module name `pyroll.zouhar_contact`.

### Coefficient Hooks

The plugin specifies hooks for the three coefficients as `zouhar_contact_c1`, `zouhar_contact_c2`
and `zouhar_contact_c3`. on `RollPass`. Default implementations of them result in $C_1 = 1$, $C_2 = 0$ and $C_3 = 1$,
which is essentially the trapezoidal rule.

For the pass types listed above, implementation are provided, which check for the type of the in and out profiles.

### Initial Contact Width Hook

The plugin specifies a `zouhar_contact_in_width` hook on `RollPass`, to deliver the width of the initial contact $b$.
For the pass types listed above, implementation are provided, which check for the type of the in and out profiles.

### Contact Area Hook

The plugin provides an implementation of the `RollPass.Roll.contact_area` hook, which calculates the contact area
according to the model function. It asks the roll pass for coefficients and initial width. If one of these is not
available, the function returns `None`.

## References

- Zouhar, G.: Umformungskräfte beim Walzen in Streckkalibern, 1960, Phd Thesis, TU Bergakademie Freiberg
- Hensel, Poluchin: Technologie der Metallformung, Deutscher Verlag für Grundstoffindustrie, Leipzig, 1990, ISBN:
  3-342-00311-1