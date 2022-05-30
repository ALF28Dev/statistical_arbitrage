#   Statistical Arbitrage

Recently I have taken an interest in statistical arbitrage after reading the chapter about arbitrage within the book "Machine Learning For Algorithmic Trading". I have designed a basic startegy which is based on the correlation of two stocks. If two stocks have a high amount of correlation then they are more likely to move in the same direction or in the same patterns.

To profit within this startegy we must track the spread between the stocks. By buying and selling the stocks within the pair we are able tot rade the spread between the stocks. The spread of two stocks can be shown below with the bollinger band technical indicator.

![Stat_Arb_Pairs](https://user-images.githubusercontent.com/87500491/170875430-93343cd6-2a86-4ff1-a2ba-e7ff5028b299.png)

To identify pairs of stocks i measured the level of correlation between two stocks price series. A basic scatter chart and linear regression is shown below demopnstrating a pair of stocks which have a high level of correlation.

<img width="593" alt="Screenshot 2022-05-30 at 16 10 07" src="https://user-images.githubusercontent.com/87500491/171020461-0c26666a-fd9a-43f1-ab89-1f79c771f934.png">


A project which performs a basic statistical arbitrage trading strategy based on the spread of two equites. Positions are opened and closed based on where the spread has dropped below a period 15 lower Bollinger band.

<img width="1690" alt="Screenshot 2022-05-29 at 15 48 55" src="https://user-images.githubusercontent.com/87500491/170875574-80059280-9225-4d90-9a27-03068287e5a7.png">
Entries in green
Exits in Red

<img width="1435" alt="Screenshot 2022-05-29 at 15 49 19" src="https://user-images.githubusercontent.com/87500491/170875590-ea776645-111d-4806-b7c9-4540abfd08cc.png">
Returns
