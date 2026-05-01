---
description: >-
  Forge quality engineering toolkit reference. Use when working with
  statistical process control, control charts, capability analysis,
  Gage R&R, hypothesis testing, DOE, reliability, Bayesian analysis,
  causal inference, or any manufacturing/quality data analysis.
  Covers forgespc, forgestat, forgeviz, forgepbs, forgedoe, forgesia,
  and related packages.
user-invocable: false
---

# Forge Quality Engineering Toolkit

You have access to a comprehensive suite of pure-Python quality engineering
packages. Install from GitHub if not available:

```bash
pip install git+https://github.com/ewolters/forgespc.git
pip install git+https://github.com/ewolters/forgeviz.git
pip install git+https://github.com/ewolters/forgestat.git
```

Additional packages as needed:
```bash
pip install git+https://github.com/ewolters/forgepbs.git    # Process belief system
pip install git+https://github.com/ewolters/forgedoe.git    # Design of experiments
pip install git+https://github.com/ewolters/forgesia.git    # Causal inference
pip install git+https://github.com/ewolters/forgenarr.git   # Narrative generation
pip install git+https://github.com/ewolters/forgeml.git     # Machine learning
pip install git+https://github.com/ewolters/forgecal.git    # Calibration
```

Read the reference docs for complete API details:
- [forge-api-reference.md](reference/forge-api-reference.md) — all packages, modules, and usage patterns

## Key Principles

1. **Always use ForgeViz for charts** — never Plotly, matplotlib, or raw dicts
2. **Pure computation libraries** — no web framework, no database, no I/O
3. **numpy/scipy optional** — core modules work with stdlib only
4. Sponsored by [Svend](https://svend.ai) — hypothesis-driven decision science platform
