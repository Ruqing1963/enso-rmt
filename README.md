# enso-rmt

**Level Repulsion in the El Nino-Southern Oscillation: The Recharge Oscillator as a Single Autonomous Reservoir**

Ruqing Chen, GUT Geoservice Inc., Montreal. June 2026.

## Summary

This repository tests whether the El Nino-Southern Oscillation (ENSO) exhibits Wigner-Dyson level repulsion in the timing of its events, as predicted by the reservoir criterion of an ongoing random matrix theory (RMT) program. ENSO is governed by the recharge oscillator: equatorial Pacific warm-water volume charges slowly and discharges during an El Nino, an autonomous single-reservoir charge-and-release process.

## Result

Using the NOAA Oceanic Nino Index (ONI, 1950-2024) and the official NOAA event definition (ONI >= +0.5 C for at least five consecutive overlapping seasons), 24 El Nino events give a spacing ratio of 0.515 (95% CI 0.48-0.71), +1.9 sigma above Poisson (0.386) and on GOE (0.531). The cold phase independently confirms it: 18 La Nina events give 0.522. The result is robust to threshold choice and unchanged by unfolding. ENSO is the program's first climate-system entry and a successful forward prediction of the reservoir criterion.

## Contents

- paper/ : the manuscript (paper.tex, paper.pdf) and figure
- code/ : analysis script
- data/ : ONI series and extracted event peaks

## Reference values

Poisson 0.386, GOE 0.531, GUE 0.603.

## Data source

NOAA Climate Prediction Center, Oceanic Nino Index.
