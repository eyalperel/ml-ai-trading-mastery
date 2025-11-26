"""
Day 4: Correlation and angle in trading contexts
"""
from vector_basics import Vector
import math

def correlation_matrix(vectors, labels=None):
    """
    Create correlation matrix for a list of vectors.
    
    Args:
        vectors: List of Vector objects
        labels: Optional list of labels for printing
    
    Returns:
        List of lists (correlation matrix)
    
    Example:
        >>> spy = Vector([...])
        >>> qqq = Vector([...])
        >>> gld = Vector([...])
        >>> corr_matrix = correlation_matrix([spy, qqq, gld], ['SPY', 'QQQ', 'GLD'])
    """
    n = len(vectors)
    matrix = []
    
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1.0)  # Correlation with self = 1
            else:
                corr = vectors[i].correlation_with(vectors[j])
                row.append(corr)
        matrix.append(row)
    
    # Pretty print if labels provided
    if labels:
        print("\nCorrelation Matrix:")
        print("        ", "  ".join(f"{label:>6}" for label in labels))
        for i, row in enumerate(matrix):
            print(f"{labels[i]:>6}: ", "  ".join(f"{val:>6.3f}" for val in row))
    
    return matrix



# Example 1: Stock correlation (diversification)
print("=== Stock Return Correlation ===")
# Daily returns for 10 days
spy_returns = Vector([0.01, -0.02, 0.015, -0.01, 0.02, -0.015, 0.005, 0.01, -0.01, 0.02])
qqq_returns = Vector([0.012, -0.025, 0.018, -0.008, 0.025, -0.012, 0.008, 0.015, -0.008, 0.025])
gld_returns = Vector([-0.005, 0.01, -0.002, 0.015, -0.01, 0.008, -0.003, -0.005, 0.012, -0.008])

corr_spy_qqq = spy_returns.correlation_with(qqq_returns)
corr_spy_gld = spy_returns.correlation_with(gld_returns)

print(f"SPY vs QQQ correlation: {corr_spy_qqq:.3f}")
print(f"SPY vs GLD correlation: {corr_spy_gld:.3f}")
print("→ SPY/QQQ highly correlated (tech stocks)")
print("→ SPY/GLD low correlation (diversification benefit!)\n")

# Example 2: Pairs trading candidates
print("=== Pairs Trading: Finding Correlated Pairs ===")
stock_a = Vector([100, 102, 101, 103, 105, 104, 106, 108, 107, 109])
stock_b = Vector([50, 51, 50.5, 51.5, 52.5, 52, 53, 54, 53.5, 54.5])
stock_c = Vector([200, 195, 205, 200, 210, 205, 215, 210, 220, 215])

# Calculate returns (percent changes)
def to_returns(prices):
    """Convert prices to returns"""
    returns = []
    for i in range(1, len(prices.components)):
        ret = (prices.components[i] - prices.components[i-1]) / prices.components[i-1]
        returns.append(ret)
    return Vector(returns)

returns_a = to_returns(stock_a)
returns_b = to_returns(stock_b)
returns_c = to_returns(stock_c)

corr_ab = returns_a.correlation_with(returns_b)
corr_ac = returns_a.correlation_with(returns_c)

print(f"Stock A vs B correlation: {corr_ab:.3f}")
print(f"Stock A vs C correlation: {corr_ac:.3f}")
print(f"→ A & B are good pairs trading candidates (corr={corr_ab:.3f})")
print(f"→ A & C less suitable (corr={corr_ac:.3f})\n")

# Example 3: Factor model - correlation with market
print("=== Factor Model: Beta Calculation ===")
market_returns = Vector([0.01, -0.02, 0.03, -0.01, 0.02, -0.015, 0.01, 0.025, -0.02, 0.015])
stock_returns = Vector([0.015, -0.03, 0.045, -0.015, 0.03, -0.025, 0.015, 0.04, -0.03, 0.02])

correlation = stock_returns.correlation_with(market_returns)
beta = correlation * (stock_returns.std() / market_returns.std())

print(f"Stock-Market correlation: {correlation:.3f}")
print(f"Stock volatility: {stock_returns.std():.4f}")
print(f"Market volatility: {market_returns.std():.4f}")
print(f"Beta: {beta:.3f}")
print(f"→ Beta > 1: Stock is more volatile than market")
print(f"→ High correlation: Stock moves with market\n")

# Example 4: Uncorrelated vs orthogonal
print("=== Uncorrelated vs Orthogonal ===")
# Two random-looking return series
series_1 = Vector([0.01, -0.01, 0.02, -0.02, 0.01])
series_2 = Vector([0.02, 0.01, -0.01, 0.01, -0.02])

# De-mean them
demean_1 = series_1.de_mean()
demean_2 = series_2.de_mean()

correlation = series_1.correlation_with(series_2)
are_orthogonal = demean_1.is_orthogonal(demean_2)

print(f"Correlation: {correlation:.3f}")
print(f"De-meaned vectors orthogonal? {are_orthogonal}")
print(f"→ If correlation ≈ 0, de-meaned vectors are nearly orthogonal")
print(f"→ Zero correlation = orthogonal de-meaned vectors\n")