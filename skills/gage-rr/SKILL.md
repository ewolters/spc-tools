---
name: gage-rr
description: >-
  Run Gage R&R measurement system analysis. Supports crossed and nested
  designs with repeatability, reproducibility, part-to-part variation,
  and number of distinct categories (ndc). Use when validating a
  measurement system before process capability studies.
argument-hint: "describe your measurement study"
allowed-tools:
  - Bash(pip install *)
  - Bash(python3 *)
  - Write
  - Read
---

# Gage R&R — Measurement System Analysis

Evaluate measurement system adequacy using Gage R&R.

## Step 1: Ensure Dependencies

```bash
pip install git+https://github.com/ewolters/forgespc.git git+https://github.com/ewolters/forgeviz.git 2>/dev/null || true
```

## Step 2: Determine Study Design

| Design | When to Use |
|--------|------------|
| **Crossed** | Every operator measures every part (most common) |
| **Nested** | Each operator measures different parts (destructive testing) |

## Step 3: Get Data

Ask for:
1. **Measurements**: all measurement values
2. **Parts**: which part each measurement belongs to (10+ parts recommended)
3. **Operators**: which operator took each measurement (2-3 operators typical)
4. **Replicates**: how many times each operator measured each part (2-3 typical)

Data can be provided as lists, CSV, or a structured table.

## Step 4: Run Analysis

```python
from forgespc.gage import gage_rr_crossed  # or gage_rr_nested
from forgeviz.charts.gage import gage_rr_components, gage_by_part_operator
from forgeviz import render

grr = gage_rr_crossed(measurements, parts, operators)

# Visualization
comp_spec = gage_rr_components(grr, title="Gage R&R Components")
po_spec = gage_by_part_operator(grr, title="By Part × Operator")

print(render(comp_spec, format="json"))
print(render(po_spec, format="json"))
```

## Step 5: Interpret Results

| Component | %Study Var | %Tolerance |
|-----------|-----------|------------|
| Total Gage R&R | {grr.total_grr} | {grr.percent_tolerance} |
| Repeatability | {grr.repeatability} | — |
| Reproducibility | {grr.reproducibility} | — |
| Part-to-Part | {grr.part_to_part} | — |

**Number of Distinct Categories (ndc):** {grr.ndc}

### Acceptance Criteria (AIAG)

| %Study Var | ndc | Assessment |
|-----------|-----|-----------|
| < 10% | ≥ 5 | Acceptable measurement system |
| 10-30% | 3-4 | Marginal — may be acceptable for some applications |
| > 30% | < 3 | Not acceptable — measurement system needs improvement |

### If Not Acceptable

- **High repeatability**: equipment variation — calibrate, maintain, or replace gage
- **High reproducibility**: operator variation — training, clearer procedures, fixtures
- **Low ndc**: measurement system cannot distinguish between parts — finer resolution needed

Report the assessment. If the measurement system is not acceptable, capability
studies on the process are meaningless — fix the measurement system first.
