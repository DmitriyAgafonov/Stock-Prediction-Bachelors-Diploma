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
- **Fast Fourier transform** - to extract global and local trends in the GS stocs and to denoise it.
- **Autoregressive Integrated Moving Average (ARIMA)** - add it as a predictive feature.

## Sentiment Analysis
For the purpose of creating accurate sentiment prediction - **classifying news as positive or negative (or neutral)** - we will use Neural Language Processing (NLP). Bidirectional Embedding Representations from Transformers (BERT) is Google's NLP approach for transfer learning. For sentiment classification of financial news we use pre-trained BERT-based model **finBERT**.

## Fourier Transform
Fourier transforms take a function and create a series of sine waves (with different amplitudes and frames). When combined, these sine waves approximate the original function.
We will create Fourier transforms in order to generalize several long- and short-term trends. These transforms will eliminate noise (random walks) in data and create approximations of the real stock movement. Having trend approximations can help the LSTM network pick its prediction trends more accurately.

## ARIMA
 ARIMA is a technique for predicting time series data.
 We use it as a technique to denoise the stock a little and to extract some new patters or features.

## Statistical check
- Multicollinearity (error terms (also called residuals) depend on each other)
- Serial correlation (one feature completely depemnds on another feature)
- Heteroskedasticity (the error terms (the difference between a predicted value by a regression and the real value) are dependent on the data)

## Reduce dimensions
We use **Principal Component Analysis (PCA)** in order to reduce the dimensionality of the created features and to create the new components to explain maximum of the variance.

## LSTM Modelling
### Train/test set formation
Performing stationarization and time series stationarity (math expectation, variance and lack of autocorellation are constant) test - **Dickey-Fuller Test**
Since we use **sequence-to-sequence LSTM model** we shound transform data by: 1) shift back objective function with respect to independent variables; 2) iteratively move window in direction of timeline - create batches for each iteration. We will predict price change in next 30 days based on previous 60 days.

---
### LSTM architecture
Hyperparameter tuning gave **LSTM architecture:**
- 2 hidden layers
- each 120 nodes
- Adam optimizer
- learning rate 0.0001
- 100 epochs
- batch size 32

---
### Prediction results
Predicted data transformed back into time series and vizualized:

![img1.png](https://github.com/DmitriyAgafonov/Stock-Prediction-Bachelors-Diploma/blob/master/imgs/img1.png)

Metric evaluation:

![img2.png](https://github.com/DmitriyAgafonov/Stock-Prediction-Bachelors-Diploma/blob/master/imgs/img2.png)

## Dash application
**Dash** is a Python framework based on Flask and Plotly that used for web application development. Dash is open source and runs in a web browser. Graphs are interactive, the user can interact with time periods and scale them.

![img3.png](https://github.com/DmitriyAgafonov/Stock-Prediction-Bachelors-Diploma/blob/master/imgs/img3.png)

![img4.png](https://github.com/DmitriyAgafonov/Stock-Prediction-Bachelors-Diploma/blob/master/imgs/img4.png)
