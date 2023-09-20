#%%
import pandas as pd
import numpy as np

#%%
df = pd.read_parquet("/home/docker/data_engineering/data_raw/green_tripdata_2023-01.parquet")


# %%
import sqlalchemy

# %%
engine = sqlalchemy.create_engine('postgresql://root:root@localhost:5432/ny_taxi')
engine.connect()
# %%
print(pd.io.sql.get_schema(df, name='green_taxi_data', con=engine))




#%%
import pyarrow.parquet as pq
import psycopg2

pq_file = pq.ParquetFile("/home/docker/data_engineering/data_raw/green_tripdata_2023-01.parquet")
conn = psycopg2.connect(database="ny_taxi", 
                        user="root",
                        password="root")

chunks = 100000
for i in pq_file.iter_batches(batch_size=chunks):
    df = i.to_pandas()    
    





#%%

chunksize = 100000

for i in range(pq_file.num_row_groups):
    row_data = pq_file.read_row_group(i)



# %%
