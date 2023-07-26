# Computes the following in python
#
# SELECT "UserID", "SearchPhrase", COUNT(*)
# FROM hits
# GROUP BY "UserID", "SearchPhrase"
# ORDER BY COUNT(*)
# DESC LIMIT 10;

import pandas as pd
import time
from collections import defaultdict
from operator import itemgetter


start = time.time()
+#hits = pd.read_parquet('hits_multi/hits_0.parquet', engine='pyarrow')
hits = pd.read_parquet('hits.parquet', engine='pyarrow')
print("{}s: Loaded {} rows from parquet".format(time.time() - start, len(hits)))

# build groups
counts = defaultdict(int)

for index, row in hits.iterrows():
    group = (row['UserID'], row['SearchPhrase']);
    # update the dict entry for the corresponding key
    counts[group] += 1

print("{}s: Counted groups".format(time.time() - start))


# Print the top 10 values
print (dict(sorted(counts.items(), key=itemgetter(1), reverse=True)[:10]))
print("{}s: Done".format(time.time() - start))
