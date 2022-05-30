#   Statistical Arbitrage

Recently I have taken an interest in statistical arbitrage after reading the chapter about arbitrage within the book "Machine Learning For Algorithmic Trading". I have designed a basic startegy which is based on the correlation of two stocks. If two stocks have a high amount of correlation then they are more likely to move in the same direction or in the same patterns.

To profit within this startegy we must track the spread between the stocks. By buying and selling the stocks within the pair we are able to trade the spread. The spread of two stocks can be shown below with the bollinger band technical indicator.

![Stat_Arb_Pairs](https://user-images.githubusercontent.com/87500491/170875430-93343cd6-2a86-4ff1-a2ba-e7ff5028b299.png)

To identify pairs of stocks i measured the level of correlation between two stocks price series. A basic scatter chart and linear regression is shown below demopnstrating a pair of stocks which have a high level of correlation.

<img width="593" alt="Screenshot 2022-05-30 at 16 10 07" src="https://user-images.githubusercontent.com/87500491/171020461-0c26666a-fd9a-43f1-ab89-1f79c771f934.png">

A key component of the statistical arbitrage startgey is knowing when to open and close positions. For my strategy i chose to utilise a period 15 bollinger band. Whenever the spread drops below the lower-band I will open a position. i will then sell this position when the spread rises above the upper-band. This startegy will only place long positions which will profit when the spread widens. (Long Bias)

#   Strategy Backtesting

<img width="1690" alt="Screenshot 2022-05-29 at 15 48 55" src="https://user-images.githubusercontent.com/87500491/170875574-80059280-9225-4d90-9a27-03068287e5a7.png">

To test this stratgey i designed and developed my own backtest engine which can take in vast amounts of data from the yfinance api and open, close trades as well as track and monitor position and cumulative returns. The image above shows one of the output charts produced by my backtest engine. The entries and exits are clearly shown by the green (entries) and red (exits) triangles.

The cumulative returns of the strategy above arw shown in the chart below. The stratgey does not place a lot of trades however it does seem to have a fairly high winrate. I have also noticed that the winrate will increase dramatically based on the amount of correlation bewteen the pairs.

<img width="1435" alt="Screenshot 2022-05-29 at 15 49 19" src="https://user-images.githubusercontent.com/87500491/170875590-ea776645-111d-4806-b7c9-4540abfd08cc.png">

#   Index and DLC Statistical Arbitrage



#   Furthur improvements
* Research cointegration
* Develop platform to manage statarb positions
