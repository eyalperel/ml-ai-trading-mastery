"""
Day 3: Distance and normalization in trading contexts
"""
from vector_basics import Vector

# Example 1: Market regime similarity
print("=== Market Regime Similarity ===")
# Feature vector: [volatility, trend_strength, volume_ratio]
regime_bull_2020 = Vector([0.15, 0.8, 1.2])
regime_bull_2023 = Vector([0.18, 0.75, 1.15])
regime_crash_2020 = Vector([0.65, -0.9, 0.4])

print(f"Bull 2020 vs Bull 2023 distance: {regime_bull_2020.distance(regime_bull_2023):.3f}")
print(f"Bull 2020 vs Crash 2020 distance: {regime_bull_2020.distance(regime_crash_2020):.3f}")
print("→ Similar regimes have small distance\n")

# Example 2: Returns volatility
print("=== Returns Volatility (Standard Deviation) ===")
daily_returns = Vector([0.01, -0.02, 0.015, -0.01, 0.02, -0.015, 0.005])
print(f"Mean return: {daily_returns.mean():.4f}")
print(f"Volatility (std): {daily_returns.std():.4f}")
print(f"Annualized vol (approx): {daily_returns.std() * (252**0.5):.2%}\n")

# Example 3: Feature standardization for ML
print("=== Feature Standardization ===")
volumes = Vector([1.2e6, 1.5e6, 0.9e6, 1.8e6, 1.1e6])  # Raw volumes
print(f"Original volumes: mean={volumes.mean():.2e}, std={volumes.std():.2e}")

volumes_z = volumes.standardize()
print(f"Standardized: mean={volumes_z.mean():.6f}, std={volumes_z.std():.6f}")
print("→ Now ready for ML model input\n")