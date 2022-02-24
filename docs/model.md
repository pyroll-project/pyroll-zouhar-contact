# The Zouhar approach to contact areas

The simplest method to estimate contact areas in elongation groove rolling is to use a trapezoid. However, this method
is quite inaccurate. Zouhar extended this method by applying several empirical correction coefficients dependent on the
pass type. His function for the contact area is:

```math
    A_{\mathrm{d}} = \left[ b_1 C_2 + \frac{1}{2} \left( b_1 + b C_1 \right) \left( 1 - C_2 \right) \right] C_3 L_{\mathrm{d}}
```

This function includes three empirical coefficients $`C_i`$, the contact length $`L_{\mathrm{d}}`$, the out profile
width $`b_1`$ and the initial contact width $`b`$. For $`C_1 = 1`$, $`C_2 = 0`$ and $`C_3 = 1`$ the model collapses to
the trapezoidal rule. The initial contact width $`b`$ for some pass types approximated with the roll gap of the last
roll $`s_0`$, since the profile first contacts mainly with its tip. For other types it is just the width of the rotated
profile $`b_0`$.

Zouhar gave the following coefficients:

| In      | Out     | $`b`$   | $`C_1`$ | $`C_2`$ | $`C_3`$ |
|---------|---------|---------|---------|---------|---------|
| diamond | diamond | $`s_0`$ | 1       | 0.3     | 1       |
| diamond | square  | $`s_0`$ | 1       | 0.28    | 1       |
| square  | diamond | $`s_0`$ | 1       | 0.28    | 1       |
| oval    | square  | $`s_0`$ | 1       | 0.1     | 1       |
| square  | oval    | $`b_0`$ | 0.82    | 0.2     | 1.02    |
| round   | oval    | $`b_0`$ | 0.45    | 0.18    | 1       |
| oval    | round   | $`s_0`$ | 1       | 0       | 1       |

## References

- Zouhar, G.: Umformungskräfte beim Walzen in Streckkalibern, 1960, Phd Thesis, TU Bergakademie Freiberg
- Hensel, Poluchin: Technologie der Metallformung, Deutscher Verlag für Grundstoffindustrie, Leipzig, 1990, ISBN:
  3-342-00311-1
