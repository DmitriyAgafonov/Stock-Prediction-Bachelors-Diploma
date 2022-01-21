# Stock-Prediction-Bachelors-Diploma
Using several machine learning algorithms and AI to predict stock market movements

___The task is to collect data, perform data analysis, construct features, test data, reduce dimensions, 
train algorithm and predict movements of Goldman Sachs stock prices.___

## Several important basic assumptions
1) Markets are not 100% random 
2) History repeats
3) Markets follow people's rational behavior
4) The **Efficient Market Hypothesis (EMH)** that states that asset prices reflect all available information **is correct**

## Data
To understand what affects whether GS's stock price will move up or down 
we need to incorporate as much information (depicting the stock from different aspects and angles) as possible.
We collect data from 01.01.2010 to 01.04.2021.

The features we will use are:
- **Correlated assets** - these are other assets (other stocks, commodities, FX, indices, fixed income securities). 
A big company such as GS depends on and interacts with many external factors, including its competitors, clients, the global economy, 
the geo-political situation, fiscal and monetary policies, access to capital, etc. 
- **Technical indicators** - use the most popular indicators as independent features. For example - 
7 and 21 days moving average, exponential moving average, momentum, Bollinger bands, MACD etc.
- **News** - news an indicate upcoming events that can potentially move the stock in certain direction. 
We will read all daily news for Goldman Sachs and extract whether the total sentiment about Goldman Sachs on that day is positive, neutral, or negative. 
- **Fast Fourier transform** - 
