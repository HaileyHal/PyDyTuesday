import pandas as pd
import matplotlib.pyplot as plt

flint_mdeq = pd.read_csv('flint_mdeq.csv')
mdeq_desc = flint_mdeq.describe()
print(f'MDEQ: {mdeq_desc}')

flint_vt = pd.read_csv('flint_vt.csv')
vt_desc = flint_vt.describe()
print(f'VT: {vt_desc}')

# visualize data
plt.hist(flint_mdeq['lead'], histtype='bar', bins=30)
plt.xlabel('Lead (ppb)')
plt.ylabel('Number of Samples')
plt.title('MDEQ Lead Before Data Cuts')
plt.grid()

plt.show()

plt.hist(flint_vt['lead'], histtype='bar', bins=30)
plt.xlabel('Lead (ppb)')
plt.ylabel('Number of Samples')
plt.title('VT Lead')
plt.show()

'''
How does the distribution of lead levels differ between MDEQ and Virginia Tech datasets?

In both the filtered and unfiltered MDEQ datasets, the distribution of lead levels is much less
of a wide spread than the VT sample.
'''