import findspark
findspark.init()
from pyspark.sql import SparkSession 
from pyspark.sql.functions import col, sum
from pyspark.sql.types import DoubleType


# Create a SparkSession
spark = SparkSession.builder \
    .appName("Simple DataFrame Example") \
    .getOrCreate()


#Create a simple DataFrame with two columns: 'id' and 'value'
# data = [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')]
# columns = ['id', 'value']
# df = spark.createDataFrame(data, columns)
# df.show()
#spark.stop()


#########################
try:
    # 1. Ingest Data
    df = spark.read.parquet("..\data\yellow_tripdata_2024-01.parquet")
    print(df.count())

    # 2. Filter Data
    filtered_df = df.filter(col("fare_amount") > 10)

    enhanced_df = filtered_df.withColumn("total_amount", col("total_amount").cast(DoubleType())) \
                            .withColumn("tip_amount", col("tip_amount").cast(DoubleType())) \
                            .withColumn("total_amount_with_tip", col("total_amount") + col("tip_amount"))

    enhanced_df.show(5)

# Save as parquet 
#########################
    enhanced_df.write.parquet('..\processed_data\parquet_taxi.parquet')   # .mode('overwrite')
    print("the data saved as parquet successfly YooPi")
    
# 3. Save as CSV
#########################
    enhanced_df.write.option('header', 'true').csv('..\processed_data\parquet_taxi.csv')    # .mode('overwrite')
    print("the data saved as csv successfly YooPi")

#########################
except Exception as e:
    print("Error occurred:", e)
##########################

finally:
    spark.stop()