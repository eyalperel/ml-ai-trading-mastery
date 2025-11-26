# Day 4 - Correlation

**Date:** 26/11/2025

---

## What I learned today
- Correlation measures how two vectors move together (range: -1 to +1)
- Correlation = cos(angle between **de-meaned** vectors) - this geometric view is powerful!
- Must de-mean vectors first, otherwise you're measuring absolute values not co-movement
- Edge case: if std=0 (constant vector), correlation is undefined, return 0

## Biggest "aha" moment
When I realized correlation is just the cosine of an angle! If two stock returns have correlation 0.9, their de-meaned return vectors form a ~25° angle. If correlation is 0, they're perpendicular (90°). This makes diversification visual - you want wide angles between your assets.

## How I'll use this in trading
- Pairs trading: find stocks with correlation > 0.85, trade when spread diverges
- Portfolio diversification: keep pairwise correlations < 0.7 to reduce risk
- EUR/USD vs GBP/USD in FX: check correlation before trading both simultaneously
- Calculate beta: beta = correlation × (stock_volatility / market_volatility)

## What was difficult
The zero correlation test failed initially. I gave it vectors that I thought were orthogonal, but when de-meaned they weren't! Had to manually calculate the dot product to debug. Lesson: always verify test data by hand first.

## Tomorrow I want to
- Build a miniproject using all Week 1 concepts
- Apply correlation to real market data (maybe download SPY/QQQ/GLD prices)
- Review Days 1-4 before starting Week 2 matrices