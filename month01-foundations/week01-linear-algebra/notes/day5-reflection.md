# Day 5 - Week 1 Complete

**Date:** 27-11-2025    

---

## What I learned today
- How to structure a professional portfolio analyzer using classes
- Correlation matrix: nested loops calculate all pairwise correlations
- Real portfolio insights: SPY/QQQ highly correlated (0.99), GLD negatively correlated (-0.91)
- Sharpe ratio = mean/std measures risk-adjusted returns
- All my Vector methods (mean, std, correlation) work in a real application!

## Biggest "aha" moment
Seeing how the correlation matrix reveals portfolio structure! SPY and QQQ are basically the same (0.993), so holding both gives almost no diversification. But GLD has -0.91 correlation with stocks - that's TRUE diversification. This is why portfolio theory works - math reveals what you can't see by just looking at price charts.

## How I'll use this in trading
- Before adding an asset to my portfolio, check correlation with existing holdings
- Target correlation < 0.7 for new positions (better diversification)
- In FX trading: check EUR/USD vs GBP/USD correlation before trading both
- Use Sharpe ratio to compare strategies on risk-adjusted basis, not just returns
- Negative correlation assets (like gold vs stocks) are portfolio insurance

## What was difficult
Understanding the nested loop logic for the correlation matrix at first. The `j = i+1` trick to avoid duplicates is clever but took me a minute to grasp. Also understanding why TLT has the best Sharpe even though it doesn't have the highest return - it's the low volatility that makes it win on risk-adjusted basis.

## Next week I want to
- Start matrices (Week 2)
- Keep the daily reflection habit going
- Maybe extend this miniproject with real market data using yfinance
- Understand how correlation matrices connect to covariance matrices