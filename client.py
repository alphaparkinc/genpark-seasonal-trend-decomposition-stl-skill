"""Classical Additive Seasonal-Trend Decomposition Engine.
100% Python Standard Library.
"""

class SeasonalDecomposition:
    """Classical Additive Seasonal-Trend Decomposition."""
    @staticmethod
    def decompose(series, period=4):
        n = len(series)
        assert n >= period * 2, "Series too short for decomposition"

        trend = [None] * n
        half = period // 2
        for i in range(half, n - half):
            if period % 2 == 0:
                w1 = sum(series[i - half : i + half])
                w2 = sum(series[i - half + 1 : i + half + 1])
                trend[i] = (w1 + w2) / (2.0 * period)
            else:
                trend[i] = sum(series[i - half : i + half + 1]) / period

        detrended = [None if trend[i] is None else series[i] - trend[i] for i in range(n)]

        season_sums = [0.0] * period
        season_counts = [0] * period
        for i in range(n):
            if detrended[i] is not None:
                season_sums[i % period] += detrended[i]
                season_counts[i % period] += 1

        seasonal_pattern = [season_sums[i] / (season_counts[i] or 1) for i in range(period)]
        mean_s = sum(seasonal_pattern) / period
        seasonal_pattern = [s - mean_s for s in seasonal_pattern]

        seasonal = [seasonal_pattern[i % period] for i in range(n)]
        residual = [None if trend[i] is None else series[i] - trend[i] - seasonal[i] for i in range(n)]

        return {"trend": trend, "seasonal": seasonal, "residual": residual, "period": period}
