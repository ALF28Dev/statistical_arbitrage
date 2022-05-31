#   Statistical Arbitrage

I recently became interested in statistical arbitrage after reading the chapter about arbitrage in the book "Machine Learning For Algorithmic Trading". I have designed a basic strategy based on the correlation of two stocks. If two stocks have a high correlation, they are more likely to move in the same direction or the same patterns.

To profit from this strategy, we must track the spread between the stocks. We can trade the spread by buying and selling the stocks within the pair. An example spread is shown below with a bollinger band indicator.

![Stat_Arb_Pairs](https://user-images.githubusercontent.com/87500491/170875430-93343cd6-2a86-4ff1-a2ba-e7ff5028b299.png)

To identify pairs of stocks, I measured the level of correlation between two stock price time series. A basic scatter chart and linear regression are shown below, demonstrating a pair of stocks with a high correlation level.

<img width="593" alt="Screenshot 2022-05-30 at 16 10 07" src="https://user-images.githubusercontent.com/87500491/171020461-0c26666a-fd9a-43f1-ab89-1f79c771f934.png">

A key component of the statistical arbitrage strategy is knowing when to open and close positions. For my strategy, I chose to utilise a period 15 bollinger band. Whenever the spread drops below the lower band, I will open a position. The position will then be sold when the spread rises above the upper band. This strategy will only place long positions that profit when the spread widens (long bias).

#   Strategy Backtesting

<img width="1690" alt="Screenshot 2022-05-29 at 15 48 55" src="https://user-images.githubusercontent.com/87500491/170875574-80059280-9225-4d90-9a27-03068287e5a7.png">

To test this strategy, I designed and developed my own backtest engine, which can take in data from the yfinance API and open/close trades as well as track/monitor positions and cumulative returns. The image above shows one of the output charts produced by my backtest engine. The entries and exits are clearly shown by the green (entries) and red (exits) triangles.

The cumulative returns of the strategy above are shown in the chart below. The system does not place a lot of trades; however it does seem to have a reasonably high win rate. I have also noticed that the win rate will increase dramatically based on the amount of correlation between the pairs. This becomes evident when using the strategy on Indices and DLC's.

<img width="1435" alt="Screenshot 2022-05-29 at 15 49 19" src="https://user-images.githubusercontent.com/87500491/170875590-ea776645-111d-4806-b7c9-4540abfd08cc.png">

#   Index and DLC Statistical Arbitrage

Arbitrage using DLC'S

A DLC is a Dual-Listed Company. This is a company with a stock listed on more than one exchange. As exchanges are independent and markets are not perfect, price discrepancies will arise. A typical example of a dual-listed stock is GOOG and GOOGL. Below is the performance of my strategy on the GOOG and GOOGL pair. I have shown the spread, positions and returns of the backtest.

<img width="916" alt="Screenshot 2022-05-30 at 21 33 25" src="https://user-images.githubusercontent.com/87500491/171056357-5a1fc80a-e1a0-4ca3-865a-1b189bec47b1.png">
<img width="593" alt="Screenshot 2022-05-30 at 21 33 41" src="https://user-images.githubusercontent.com/87500491/171056396-e9414fc5-9abf-4bf4-b790-b7d2a34eea65.png">
<img width="594" alt="Screenshot 2022-05-30 at 21 33 51" src="https://user-images.githubusercontent.com/87500491/171056417-bfba98c3-d08b-42f7-9078-53d4d313a07e.png">

Arbitrage using Indices

Indices are portfolios of stocks that move based on the portfolio's overall performance. Different indices can contain the same stocks. Therefore, they are likely to have the same performance over time. As indices have the same stocks, they have a high level of correlation, meaning it is potentially possible to profit when the indices diverge.

#   Furthur improvements
* Research cointegration
* Develop platform to manage statarb positions
* Research sharpe ratios to measure performance

