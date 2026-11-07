# Helios Benchmark

A reproducible benchmark suite for short-horizon solar irradiance nowcasting.

## Contents

- `src/helios/data.py` - loaders and quality filters for the three public networks
- `src/helios/models.py` - reference model adapters (persistence, ARIMA, MLP)
- `src/helios/metrics.py` - forecast skill scores used in the paper
- `data/` - curated hourly irradiance series used for the reported numbers
- `experiments/` - training configurations and result tables

## Reproducing the results

```
python -m helios.run --config experiments/helios_mlp.yaml
```

The suite is released under the MIT license.  Please cite the paper if you use
the benchmark in your own work.
