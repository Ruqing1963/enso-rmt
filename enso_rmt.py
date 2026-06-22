#!/usr/bin/env python3
"""ENSO RMT analysis: level repulsion in El Nino event spacing."""
import numpy as np

def spacing_ratio(s):
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    return float(np.mean(r))

def cv(s):
    return float(np.std(s) / np.mean(s))

def extract_events(anom, t, thr=0.5, minlen=5, sign=1):
    """NOAA objective definition: |ONI| >= thr for >= minlen consecutive
    overlapping seasons; event time = ONI peak. No hand-selection."""
    ev = []; i = 0; n = len(anom)
    while i < n:
        if sign * anom[i] >= thr:
            j = i
            while j < n and sign * anom[j] >= thr:
                j += 1
            if j - i >= minlen:
                ev.append(float(t[i + int(np.argmax(sign * anom[i:j]))]))
            i = j
        else:
            i += 1
    return np.array(ev)

if __name__ == "__main__":
    anom = np.load("data/oni_a.npy")
    t = np.load("data/oni_t.npy")
    el = extract_events(anom, t, 0.5, 5, +1)
    la = extract_events(anom, t, 0.5, 5, -1)
    for name, ev in [("El Nino", el), ("La Nina", la)]:
        iv = np.diff(ev); s = iv / np.mean(iv)
        print(f"{name}: n={len(ev)} r={spacing_ratio(s):.3f} CV={cv(s):.2f}")
    print("Reference: Poisson 0.386, GOE 0.531, GUE 0.603")
