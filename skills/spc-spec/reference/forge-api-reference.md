# Forge Quality Engineering — API Reference

All packages install from `pip install git+https://github.com/ewolters/<package>.git`

## forgespc — Statistical Process Control

```python
from forgespc.charts import individuals_moving_range_chart, xbar_r_chart
from forgespc.capability import calculate_capability
from forgespc.rules import check_nelson_rules
from forgespc.advanced import cusum_chart, ewma_chart, xbar_s_chart
from forgespc.gage import gage_rr_crossed, gage_rr_nested, attribute_agreement
from forgespc.bayesian import bayesian_capability, bayesian_control_chart
from forgespc.conformal import conformal_control
```

### Control Charts

```python
# I-MR (individuals & moving range)
result = individuals_moving_range_chart(data)
# result.x_chart: ControlChartResult (data_points, ucl, cl, lcl, ooc_indices)
# result.mr_chart: ControlChartResult

# X-bar/R (subgroup data)
result = xbar_r_chart(subgroups)  # list of lists

# Attribute charts
from forgespc.charts import p_chart, c_chart, u_chart, np_chart
result = p_chart(defective_counts, sample_sizes)
```

### Process Capability

```python
cap = calculate_capability(data, usl=25.05, lsl=24.95)
# cap.cp, cap.cpk, cap.pp, cap.ppk
# cap.sigma_level, cap.dpmo, cap.yield_percent
# cap.within_sigma, cap.overall_sigma
```

### Nelson & Western Electric Rules

```python
violations = check_nelson_rules(chart_result)
# List of {rule: int, indices: [int], description: str}
```

### Advanced Charts

```python
cusum = cusum_chart(data, target=50.0, h=5.0, k=0.5)
ewma = ewma_chart(data, lambda_=0.2, L=3.0)
xbar_s = xbar_s_chart(subgroups)
```

### Gage R&R

```python
# Crossed design (most common)
grr = gage_rr_crossed(measurements, parts, operators)
# grr.repeatability, grr.reproducibility, grr.part_to_part
# grr.total_grr, grr.ndc (number of distinct categories)
# grr.percent_tolerance, grr.percent_study_var

# Nested design
grr = gage_rr_nested(measurements, parts, operators)
```

### Bayesian SPC

```python
bcap = bayesian_capability(data, usl=53.0, lsl=47.0)
# bcap.cpk_mean, bcap.cpk_credible_interval
# bcap.probability_capable (P(Cpk > 1.33))

bcc = bayesian_control_chart(data)
# Posterior-based control limits
```

---

## forgestat — Statistical Analysis

```python
# Parametric tests
from forgestat.parametric.ttest import one_sample_t, two_sample_t, paired_t
from forgestat.parametric.anova import one_way_anova, two_way_anova
from forgestat.parametric.correlation import pearson_correlation
from forgestat.parametric.chi_square import chi_square_test

# Nonparametric
from forgestat.nonparametric.rank_tests import mann_whitney_u, kruskal_wallis, wilcoxon_signed_rank

# Post-hoc
from forgestat.posthoc.comparisons import tukey_hsd, dunnett, games_howell

# Regression
from forgestat.regression.linear import ols_regression
from forgestat.regression.logistic import logistic_regression

# Bayesian
from forgestat.bayesian.tests import bayesian_t_test, bayesian_anova
from forgestat.bayesian.proportion import bayesian_proportion

# Power analysis
from forgestat.power.sample_size import (
    sample_size_t_test, sample_size_anova,
    sample_size_proportion, sample_size_doe
)

# Exploratory
from forgestat.exploratory.descriptive import descriptive_stats
from forgestat.exploratory.pca import principal_component_analysis

# Reliability
from forgestat.reliability.survival import kaplan_meier, cox_ph
from forgestat.reliability.weibull import weibull_analysis

# Time series
from forgestat.timeseries.tests import adf_test, kpss_test
from forgestat.timeseries.decomposition import seasonal_decompose
from forgestat.timeseries.changepoint import changepoint_detection

# MSA (Measurement System Analysis)
from forgestat.msa.gage import gage_rr, icc
from forgestat.msa.agreement import bland_altman, linearity_bias
```

### Result Pattern

All tests return result objects with:
```python
result.statistic      # Test statistic
result.p_value        # p-value
result.effect_size    # Cohen's d, eta-squared, etc.
result.ci             # Confidence interval
result.summary        # Human-readable summary
```

---

## forgeviz — Visualization (ChartSpec)

```python
from forgeviz import render
from forgeviz.charts.control import control_chart
from forgeviz.charts.capability import capability_histogram, sixpack
from forgeviz.charts.generic import bar, line, scatter, histogram, box_plot
from forgeviz.charts.distribution import histogram_normal_overlay
from forgeviz.charts.effects import main_effects, interaction_plot, pareto_of_effects
from forgeviz.charts.diagnostic import residual_plots, qq_plot, four_in_one
from forgeviz.charts.gage import gage_rr_components, gage_by_part_operator
from forgeviz.charts.scatter import scatter_regression, pareto_chart
from forgeviz.charts.reliability import survival_plot, weibull_plot
from forgeviz.charts.bayesian import bayesian_control, bayesian_capability_plot
from forgeviz.charts.statistical import heatmap, scatter_matrix, bubble
```

### Control Chart

```python
spec = control_chart(
    data_points=[23.1, 22.8, 23.4, 22.9, 24.1, 22.5],
    ucl=24.0, cl=23.0, lcl=22.0,
    ooc_indices=[4],
    title="I-MR Chart — Line 2"
)
```

### Capability Histogram

```python
spec = capability_histogram(
    data=[...],
    usl=25.05, lsl=24.95,
    cp=1.67, cpk=1.45,
    title="Process Capability"
)
```

### Rendering

```python
chart_dict = render(spec, format="dict")   # Raw ChartSpec dict
chart_json = render(spec, format="json")   # JSON for forgeviz.js
svg_string = render(spec, format="svg")    # SVG for export
```

### Dashboard

```python
from forgeviz import DashboardBuilder

dash = (DashboardBuilder("Production Overview", columns=3)
    .add(control_chart(...), title="Line 1 I-MR")
    .add(capability_histogram(...), title="Capability")
    .add(bar(...), title="Defects by Shift")
    .build())
```

---

## forgedoe — Design of Experiments

```python
from forgedoe.designs.factorial import full_factorial, fractional_factorial, plackett_burman
from forgedoe.designs.response_surface import central_composite, box_behnken
from forgedoe.designs.screening import definitive_screening
from forgedoe.designs.space_filling import latin_hypercube
from forgedoe.analysis.regression import fit_model, anova_table, effects
from forgedoe.analysis.optimization import desirability, multi_response_optimize
from forgedoe.power.power_analysis import power_analysis, required_replicates
from forgedoe.adaptive.bayesian_doe import bayesian_adaptive
```

### Design Creation

```python
from forgedoe.core.types import Factor

factors = [
    Factor("Temperature", low=150, high=200, unit="°C"),
    Factor("Pressure", low=50, high=100, unit="psi"),
    Factor("Time", low=10, high=30, unit="min"),
]

design = full_factorial(factors)           # 2^3 = 8 runs
design = central_composite(factors)        # CCD with center/axial points
design = definitive_screening(factors)     # DSD for screening
```

---

## forgepbs — Process Belief System

Advanced SPC combining multiple monitoring streams: BOCPD (Bayesian Online
Changepoint Detection), E-detectors, predictive monitoring, and Bayesian
capability tracking.

```python
from forgepbs import ProcessBeliefSystem

pbs = ProcessBeliefSystem(usl=65, lsl=35)
for obs in data:
    pbs.update(obs)

pbs.shift_probability       # P(process has shifted)
pbs.health                  # Overall process health (0-1)
pbs.capability_trajectory   # Cpk over time
pbs.evidence_accumulation   # Cumulative evidence for change
```

---

## forgesia — Causal Inference

```python
from forgesia.graph.model import CausalGraph, Node, Edge
from forgesia.inference.belief import beta_binomial_update
from forgesia.propagation.cpt import belief_propagation
from forgesia.risk.scoring import risk_score
```

---

## Common Patterns

### SPC Workflow

```python
from forgespc.charts import individuals_moving_range_chart
from forgespc.capability import calculate_capability
from forgespc.rules import check_nelson_rules
from forgeviz.charts.control import control_chart
from forgeviz.charts.capability import capability_histogram
from forgeviz import render

# 1. Compute
data = [25.01, 24.99, 25.03, 25.00, 24.98, 25.02, 25.05]
chart_result = individuals_moving_range_chart(data)
cap = calculate_capability(data, usl=25.10, lsl=24.90)
violations = check_nelson_rules(chart_result)

# 2. Visualize
chart_spec = control_chart(
    data_points=chart_result.x_chart.data_points,
    ucl=chart_result.x_chart.ucl,
    cl=chart_result.x_chart.cl,
    lcl=chart_result.x_chart.lcl,
    ooc_indices=chart_result.x_chart.ooc_indices,
    title="I-MR Chart"
)
cap_spec = capability_histogram(
    data=data, usl=25.10, lsl=24.90,
    cp=cap.cp, cpk=cap.cpk,
    title=f"Capability: Cpk={cap.cpk:.2f}"
)

# 3. Render
print(render(chart_spec, format="json"))
print(render(cap_spec, format="json"))
```

### Hypothesis Testing Workflow

```python
from forgestat.parametric.ttest import two_sample_t
from forgeviz.charts.generic import box_plot
from forgeviz import render

result = two_sample_t(group_a, group_b)
print(f"p={result.p_value:.4f}, d={result.effect_size:.2f}")

spec = box_plot(
    groups={"Group A": group_a, "Group B": group_b},
    title=f"Comparison (p={result.p_value:.4f})"
)
print(render(spec, format="json"))
```
