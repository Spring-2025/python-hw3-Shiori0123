import pandas as pd
import numpy as np

import WhoAmI_File
def test_WhoAmI():
    assert WhoAmI_File.WhoAmI() != ''


import YFinance_File
def test_YahooData2returns():
    d = { 'Open': [100, 102, 101, 103],

    'High': [105, 104, 103, 105],

    'Low': [98, 100, 99, 101],

    'Close': [101, 103, 102, 104],

    'Adj Close': [101, 103, 102, 104],

    'Volume': [1000, 1200, 900, 1100]}



    index = pd.to_datetime(['2023-10-26', '2023-10-27', '2023-10-28', '2023-10-29'])

    tempdata = pd.DataFrame(d, index=index)

    returns = YahooData2returns(tempdata)

    np.isclose(returns[0], 0.01980198, atol=0.01)

    np.isclose(returns[1], -0.00970874, atol=0.01)

    np.isclose(returns[2], 0.01960784, atol=0.01)

    
import VaR_File
def test_VaR():
    r = np.random.normal(0.05, 0.03, 1000000)

    probability2SD = 0.977249868

    percent_var = VaR(r, probability2SD)

    np.round(percent_var, 2) == 0.01

import ES_File
def test_ES():
    u = np.random.uniform(0, 100, 100000)

    es_alpha = ES(losses=u, alpha=0.8)

    np.round(es_alpha, 0) == 90

    es_var = ES(losses=u, VaR=80)

    np.round(es_var, 0) == 90