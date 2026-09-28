# genpark-seasonal-trend-decomposition-stl-skill

Agent Skill implementing **Classical Additive Time-Series Decomposition** isolating centered moving average Trend ($T_t$), Periodic Seasonality ($S_t$), and Irregular Residuals ($R_t$).

## Architectural Overview
```mermaid
flowchart TD
    Series["Time Series Y_t"] --> Trend["Centered Moving Average Trend T_t"]
    Series & Trend --> Detrend["Detrended Series: Y_t - T_t"]
    Detrend --> Seasonal["Average Seasonality S_t (Zero-Centered)"]
    Series & Trend & Seasonal --> Residual["Residual Noise: R_t = Y_t - T_t - S_t"]
```
