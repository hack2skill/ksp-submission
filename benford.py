import numpy as np
from benfordslaw import benfordslaw

import pandas as pd

df = pd.read_csv('stmt.csv')


#print(df)
#print(df.head(df.iloc[:,6]))


# Create uniform random data which does definitely not follow Benfords distribution.
#X = np.random.randint(0, high=100, size=1000)

# Initialize with alpha and method.
bl = benfordslaw(alpha=0.05, method='chi2')

#print(X)
# array([13, 12,  2,  4, 99, 33, 71, 69, 65, 55,  6, 30, 30, 99, 43, 36, 12,....]

# Fit
results = bl.fit(df.iloc[:,7])

# As expected, a significant P-value is detected for the inupt data X
#[benfordslaw] >Analyzing digit position: [1]
#[benfordslaw] >[chi2] Anomaly detected! P=3.46161e-73, Tstat=361.323

# Plot
bl.plot(title='First digit test')


#second digit test

bl1 = benfordslaw(alpha=0.05, method='chi2',pos=2)

results = bl1.fit(df.iloc[:,7])

bl1.plot(title='Second digit test')

#third digit test

bl2 = benfordslaw(alpha=0.05, method='chi2',pos=3)

results = bl2.fit(df.iloc[:,7])

bl2.plot(title='third digit test')
