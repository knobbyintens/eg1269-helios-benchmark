# Helios benchmark results

Reported on the held-out 2025 split (mean over three seeds).

| model       | MAE (W/m2) | RMSE (W/m2) | forecast skill |
|-------------|-----------:|------------:|---------------:|
| persistence |      71.4  |       98.2  |          0.00  |
| climatology |      58.1  |       84.7  |          0.26  |
| MLP (ours)  |      41.9  |       63.5  |          0.58  |

The MLP baseline uses a 24 hour input window and a 6 hour horizon.  All
configurations are in `experiments/helios_mlp.yaml`.
