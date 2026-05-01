---
name: capability
description: >-
  Run process capability analysis. Calculates Cp, Cpk, Pp, Ppk, sigma level,
  DPMO, and yield. Supports Bayesian capability with credible intervals.
  Use when assessing whether a process meets specifications.
argument-hint: "describe your data and specs"
allowed-tools:
  - Bash(pip install *)
  - Bash(python3 *)
  - Write
  - Read
---

# Process Capability Analysis

Assess process capability against specification limits.

## Step 1: Ensure Dependencies

```bash
pip install git+https://github.com/ewolters/forgespc.git git+https://github.com/ewolters/forgeviz.git 2>/dev/null || true
```

## Step 2: Get Inputs

Ask for:
1. **Data**: measurements (list, CSV, or file path)
2. **USL**: upper specification limit
3. **LSL**: lower specification limit
4. **Target** (optional): nominal target value

## Step 3: Run Capability Analysis

```python
from forgespc.capability import calculate_capability
from forgeviz.charts.capability import capability_histogram, sixpack
from forgeviz import render

data = [...]  # user's data
cap = calculate_capability(data, usl=USL, lsl=LSL)

# Capability histogram
spec = capability_histogram(
    data=data, usl=USL, lsl=LSL,
    cp=cap.cp, cpk=cap.cpk,
    title=f"Process Capability: Cpk={cap.cpk:.2f}"
)
print(render(spec, format="json"))
```

### Optional: Bayesian Capability

```python
from forgespc.bayesian import bayesian_capability

bcap = bayesian_capability(data, usl=USL, lsl=LSL)
# bcap.cpk_mean — posterior mean Cpk
# bcap.cpk_credible_interval — 95% credible interval
# bcap.probability_capable — P(Cpk > 1.33)
```

## Step 4: Interpret Results

| Metric | Value | Meaning |
|--------|-------|---------|
| Cp | {cap.cp} | Potential capability (spread vs spec width) |
| Cpk | {cap.cpk} | Actual capability (accounts for centering) |
| Pp | {cap.pp} | Long-term potential capability |
| Ppk | {cap.ppk} | Long-term actual capability |
| Sigma level | {cap.sigma_level} | Process sigma (6σ = 3.4 DPMO) |
| DPMO | {cap.dpmo} | Defects per million opportunities |
| Yield | {cap.yield_percent}% | Expected percent conforming |

### Capability Guidelines

| Cpk | Assessment |
|-----|-----------|
| < 1.00 | Not capable — process produces defects |
| 1.00-1.33 | Marginally capable — needs improvement |
| 1.33-1.67 | Capable — meets typical requirements |
| > 1.67 | Highly capable — exceeds requirements |

Report the assessment and recommend actions if Cpk < 1.33.
