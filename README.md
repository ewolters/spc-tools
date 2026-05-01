# spc-tools

Statistical Process Control and quality engineering for Claude Code. Powered by the [Forge](https://github.com/ewolters) engine. Sponsored by [Svend](https://svend.ai).

## Skills

| Skill | Description |
|-------|-------------|
| `/spc-tools:control-chart` | I-MR, X-bar/R, p, c, CUSUM, EWMA charts with Nelson rules |
| `/spc-tools:capability` | Cp, Cpk, Pp, Ppk, sigma level, DPMO, yield |
| `/spc-tools:gage-rr` | Measurement system analysis (crossed/nested) |

A background `spc-spec` skill loads the complete Forge API reference automatically when you're working on quality/manufacturing analysis.

## Packages

| Package | Purpose | GitHub |
|---------|---------|--------|
| forgespc | Control charts, capability, gage R&R, Bayesian SPC | [ewolters/forgespc](https://github.com/ewolters/forgespc) |
| forgestat | Statistical tests, regression, power analysis, reliability | [ewolters/forgestat](https://github.com/ewolters/forgestat) |
| forgeviz | Chart rendering (ChartSpec → JSON/SVG) | [ewolters/forgeviz](https://github.com/ewolters/forgeviz) |
| forgedoe | Design of experiments (factorial, CCD, DSD) | [ewolters/forgedoe](https://github.com/ewolters/forgedoe) |
| forgepbs | Process belief system (advanced SPC) | [ewolters/forgepbs](https://github.com/ewolters/forgepbs) |
| forgesia | Causal inference graphs | [ewolters/forgesia](https://github.com/ewolters/forgesia) |

Dependencies auto-install on session start.

## About Svend

[Svend](https://svend.ai) is a hypothesis-driven decision science platform for manufacturing and quality professionals. Control charts, capability analysis, DOE, FMEA, root cause analysis, and more — built on the same Forge engine that powers this plugin.
