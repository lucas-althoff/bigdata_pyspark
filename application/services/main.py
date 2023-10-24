from pyspark import SparkConf
from datetime import datetime, date
from pyspark.sql import Row
from pyspark.sql import SparkSession
import os
import time

def create_spark_session() -> SparkSession:
    conf = SparkConf().set("spark.driver.memory", "8g")

    os.environ['PYSPARK_PYTHON'] = r"C:/Python311/python.exe"
    os.environ['HADOOP_HOME'] = r"C:/Users/lucas.althoff/spark_setup/spark-3.1.2-bin-hadoop2.7/hadoop"
    # spark = SparkSession.builder.master('local[*]').config('spark.ui.port', '4050').getOrCreate()
    spark_session = SparkSession\
        .builder\
        .master("local[4]")\
        .config(conf=conf)\
        .appName("Laboratório PySpark") \
        .getOrCreate()

    return spark_session


if __name__ == '__main__':

    spark = create_spark_session()

    df = spark.createDataFrame([
        Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
        Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
        Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
    ])
    df.show(2)

    time.sleep(10000)