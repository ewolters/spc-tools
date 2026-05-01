---
name: control-chart
description: >-
  Create SPC control charts from data. Supports I-MR, X-bar/R, X-bar/S,
  p, c, u, np, CUSUM, and EWMA charts with Nelson rule checks and
  ForgeViz rendering. Use when analyzing process stability or monitoring
  for out-of-control conditions.
argument-hint: "<chart_type> or describe your data"
allowed-tools:
  - Bash(pip install *)
  - Bash(python3 *)
  - Write
  - Read
---

# Control Chart Analysis

Create an SPC control chart using the Forge engine.

## Step 1: Ensure Dependencies

```bash
pip install git+https://github.com/ewolters/forgespc.git git+https://github.com/ewolters/forgeviz.git 2>/dev/null || true
```

## Step 2: Determine Chart Type

From `$ARGUMENTS` or by asking:

| Chart | Data Type | Use When |
|-------|-----------|----------|
| `imr` | Individual measurements | Single measurements per time period |
| `xbar_r` | Subgroups (n=2-10) | Multiple measurements per sample |
| `xbar_s` | Subgroups (n>10) | Larger subgroups |
| `p` | Proportion defective | Variable sample size, attribute data |
| `np` | Count defective | Fixed sample size, attribute data |
| `c` | Count defects | Fixed inspection unit |
| `u` | Defects per unit | Variable inspection units |
| `cusum` | Detect small shifts | Need to detect shifts < 1.5σ |
| `ewma` | Detect small shifts | Weighted moving average approach |

## Step 3: Get Data

Ask the user for data or read from a file. Data can be:
- A Python list of numbers
- A CSV/Excel file path
- A pandas DataFrame

## Step 4: Run Analysis

```python
from forgespc.charts import individuals_moving_range_chart, xbar_r_chart
from forgespc.rules import check_nelson_rules
from forgeviz.charts.control import control_chart
from forgeviz import render

# Compute
data = [...]  # user's data
result = individuals_moving_range_chart(data)
violations = check_nelson_rules(result)

# Visualize
spec = control_chart(
    data_points=result.x_chart.data_points,
    ucl=result.x_chart.ucl,
    cl=result.x_chart.cl,
    lcl=result.x_chart.lcl,
    ooc_indices=result.x_chart.ooc_indices,
    title="I-MR Chart"
)

# Output as JSON for rendering
print(render(spec, format="json"))
```

## Step 5: Interpret Results

Report:
- Center line, UCL, LCL values
- Number of out-of-control points and their indices
- Nelson rule violations (which rules, which points)
- Process stability assessment
- If unstable: suggest investigation of assignable causes

Write the chart JSON to a file so it can be rendered with forgeviz.js.
