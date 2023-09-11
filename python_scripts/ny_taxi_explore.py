#%%
import pandas as pd
import numpy as np

#%%
df = pd.read_parquet("/home/docker/data_engineering/data_raw/green_tripdata_2023-01.parquet", nrows=100)


# %%
import sqlalchemy as sqla

# %%
engine = sqlalchemy.create_engine('postgresql://root:root@localhost:5432/ny_taxi')
# %%
print(pd.io.sql.get_schema(df, name='green_taxi_data'))