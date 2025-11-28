"""
Week 1 Miniproject: Portfolio Correlation Analyzer
Demonstrates mastery of vector operations for systematic trading

Author: Eyal Perelmuter
Date: 2025-11-27
"""

from vector_basics import Vector

class PortfolioAnalyzer:
    """
    Analyze correlations in a portfolio of assets
    
    Demonstrates:
    - Vector operations (dot, norm, distance)
    - Statistical measures (mean, std, correlation)
    - Trading applications (diversification, risk)
    """
    
    def __init__(self, returns_dict):
        """
        Initialize analyzer with asset returns
        
        Args:
            returns_dict: Dictionary of {asset_name: Vector of returns}
        
        Example:
            returns = {
                'SPY': Vector([0.01, -0.02, 0.015, ...]),
                'QQQ': Vector([0.012, -0.025, 0.018, ...]),
            }
            analyzer = PortfolioAnalyzer(returns)
        """
        self.returns = returns_dict
        self.assets = list(returns_dict.keys())
        self.n_assets = len(self.assets)
        
    def correlation_matrix(self):
        """
        Calculate correlation matrix for all assets
        
        Returns:
            Dictionary with correlation data and matrix
        """
        n = self.n_assets
        matrix = []
        
        for i in range(n):
            row = []
            for j in range(n):
                asset_i = self.assets[i]
                asset_j = self.assets[j]
                
                if i == j:
                    corr = 1.0  # Asset always perfectly correlated with itself
                else:
                    corr = self.returns[asset_i].correlation_with(self.returns[asset_j])
                
                row.append(corr)
            matrix.append(row)
        
        return {
            'matrix': matrix,
            'assets': self.assets
        }
    
    def print_correlation_matrix(self):
        """Pretty print correlation matrix"""
        corr_data = self.correlation_matrix()
        matrix = corr_data['matrix']
        assets = corr_data['assets']
        
        print("\n" + "="*60)
        print("CORRELATION MATRIX")
        print("="*60)
        
        # Header
        print("        ", "  ".join(f"{asset:>6}" for asset in assets))
        print("-" * 60)
        
        # Rows
        for i, asset in enumerate(assets):
            row_values = "  ".join(f"{matrix[i][j]:>6.3f}" for j in range(len(assets)))
            print(f"{asset:>6}: {row_values}")
        
        print("="*60)
    
    def find_best_diversification_pairs(self, threshold=0.5):
        """
        Find asset pairs with correlation below threshold
        Good for diversification
        
        Args:
            threshold: Maximum correlation for "diversified" (default 0.5)
        
        Returns:
            List of (asset1, asset2, correlation) tuples
        """
        corr_data = self.correlation_matrix()
        matrix = corr_data['matrix']
        assets = corr_data['assets']
        
        diversified_pairs = []
        
        for i in range(len(assets)):
            for j in range(i + 1, len(assets)):  # Avoid duplicates
                corr = matrix[i][j]
                if abs(corr) < threshold:
                    diversified_pairs.append((assets[i], assets[j], corr))
        
        # Sort by correlation (lowest first = best diversification)
        diversified_pairs.sort(key=lambda x: abs(x[2]))
        
        return diversified_pairs
    
    def find_pairs_trading_candidates(self, threshold=0.85):
        """
        Find highly correlated pairs for pairs trading
        
        Args:
            threshold: Minimum correlation for pairs trading (default 0.85)
        
        Returns:
            List of (asset1, asset2, correlation) tuples
        """
        corr_data = self.correlation_matrix()
        matrix = corr_data['matrix']
        assets = corr_data['assets']
        
        pairs = []
        
        for i in range(len(assets)):
            for j in range(i + 1, len(assets)):
                corr = matrix[i][j]
                if corr >= threshold:
                    pairs.append((assets[i], assets[j], corr))
        
        # Sort by correlation (highest first)
        pairs.sort(key=lambda x: x[2], reverse=True)
        
        return pairs
    
    def portfolio_statistics(self):
        """Calculate statistics for each asset"""
        stats = {}
        
        for asset, returns in self.returns.items():
            stats[asset] = {
                'mean_return': returns.mean(),
                'volatility': returns.std(),
                'sharpe_approx': returns.mean() / returns.std() if returns.std() > 0 else 0,
                'max_return': max(returns.components),
                'min_return': min(returns.components)
            }
        
        return stats
    
    def print_statistics(self):
        """Pretty print portfolio statistics"""
        stats = self.portfolio_statistics()
        
        print("\n" + "="*60)
        print("PORTFOLIO STATISTICS")
        print("="*60)
        print(f"{'Asset':<8} {'Mean':>8} {'Vol':>8} {'Sharpe':>8} {'Max':>8} {'Min':>8}")
        print("-" * 60)
        
        for asset, stat in stats.items():
            print(f"{asset:<8} "
                  f"{stat['mean_return']:>8.4f} "
                  f"{stat['volatility']:>8.4f} "
                  f"{stat['sharpe_approx']:>8.2f} "
                  f"{stat['max_return']:>8.4f} "
                  f"{stat['min_return']:>8.4f}")
        
        print("="*60)
    
    def generate_insights(self):
        """Generate trading insights from analysis"""
        print("\n" + "="*60)
        print("TRADING INSIGHTS")
        print("="*60)
        
        # Diversification opportunities
        print("\n📊 DIVERSIFICATION OPPORTUNITIES (Correlation < 0.5):")
        div_pairs = self.find_best_diversification_pairs(threshold=0.5)
        if div_pairs:
            for asset1, asset2, corr in div_pairs[:3]:  # Top 3
                print(f"  • {asset1} + {asset2}: correlation = {corr:.3f}")
            print("  → These pairs provide good risk reduction")
        else:
            print("  → No highly diversified pairs found")
        
        # Pairs trading
        print("\n🔄 PAIRS TRADING CANDIDATES (Correlation > 0.85):")
        pairs = self.find_pairs_trading_candidates(threshold=0.85)
        if pairs:
            for asset1, asset2, corr in pairs[:3]:  # Top 3
                print(f"  • {asset1} / {asset2}: correlation = {corr:.3f}")
            print("  → Monitor spread for mean reversion opportunities")
        else:
            print("  → No highly correlated pairs found")
        
        # Best Sharpe
        stats = self.portfolio_statistics()
        best_sharpe = max(stats.items(), key=lambda x: x[1]['sharpe_approx'])
        print(f"\n⭐ BEST RISK-ADJUSTED RETURN:")
        print(f"  • {best_sharpe[0]}: Sharpe ≈ {best_sharpe[1]['sharpe_approx']:.2f}")
        
        print("="*60)


def main():
    """Main demonstration of portfolio analyzer"""
    
    print("\n" + "="*70)
    print("WEEK 1 MINIPROJECT: PORTFOLIO CORRELATION ANALYZER")
    print("Demonstrating Vector Operations for Systematic Trading")
    print("="*70)
    
    # Sample portfolio: 5 assets, 20 trading days
    # Realistic returns data (daily returns as decimals)
    portfolio_returns = {
        'SPY': Vector([0.01, -0.02, 0.015, -0.01, 0.02, -0.015, 0.005, 0.01, -0.01, 0.02,
                       0.008, -0.012, 0.018, -0.008, 0.015, -0.01, 0.012, 0.005, -0.015, 0.01]),
        
        'QQQ': Vector([0.012, -0.025, 0.018, -0.008, 0.025, -0.012, 0.008, 0.015, -0.008, 0.025,
                       0.01, -0.015, 0.022, -0.01, 0.018, -0.012, 0.015, 0.008, -0.018, 0.012]),
        
        'GLD': Vector([-0.005, 0.01, -0.002, 0.015, -0.01, 0.008, -0.003, -0.005, 0.012, -0.008,
                       0.002, 0.008, -0.005, 0.01, -0.008, 0.012, -0.002, 0.005, 0.008, -0.005]),
        
        'TLT': Vector([0.003, 0.008, -0.002, 0.012, -0.005, 0.01, -0.003, 0.005, 0.008, -0.005,
                       0.008, 0.005, -0.008, 0.01, -0.005, 0.008, -0.002, 0.008, 0.005, -0.008]),
        
        'VNQ': Vector([0.008, -0.015, 0.012, -0.008, 0.015, -0.01, 0.005, 0.008, -0.012, 0.015,
                       0.005, -0.01, 0.012, -0.005, 0.01, -0.008, 0.008, 0.002, -0.01, 0.008])
    }
    
    # Create analyzer
    analyzer = PortfolioAnalyzer(portfolio_returns)
    
    # Display results
    analyzer.print_statistics()
    analyzer.print_correlation_matrix()
    analyzer.generate_insights()
    
    print("\n" + "="*70)
    print("✅ Week 1 Complete: Vector operations mastered!")
    print("📊 Next: Week 2 - Matrices")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()