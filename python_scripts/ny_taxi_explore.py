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

#green taxi
pq_file = pq.ParquetFile("/home/docker/data_engineering/data_raw/green_tripdata_2023-01.parquet")

chunks = 100000
for i in pq_file.iter_batches(batch_size=chunks):
    df = i.to_pandas()
    df.to_sql(name="green_taxi",con=engine, if_exists="replace")

#%%
# yellow taxi
pq_file = pq.ParquetFile("/home/docker/data_engineering/data_raw/yellow_tripdata_2023-01.parquet")

chunks = 100000
for i in pq_file.iter_batches(batch_size=chunks):
    df = i.to_pandas()
    df.to_sql(name="yellow_taxi",con=engine, if_exists="replace")
    

# %%s
