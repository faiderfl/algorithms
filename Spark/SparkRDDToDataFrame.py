
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark import sql
import re
import pyspark.sql.functions as F
from pyspark.sql.types import StructField, StructType, IntegerType, StringType,DoubleType,DecimalType
from decimal import Decimal


spark = SparkSession.builder.appName('Word Count').master('local[*]').getOrCreate()
sc= spark.sparkContext


topicbyUser= [('User1','Topic1'),('User1','Topic2'),('User2','Topic1'),('User2','Topic3')]

topicbyUserRDD= sc.parallelize(topicbyUser)

schema= StructType([(StructField('Users',StringType(),True)), (StructField('Topic',StringType(),True))])

df_UserByTopic = spark.createDataFrame(topicbyUserRDD, schema)
df_UserByTopic.show()




dict_Numbers=[(1,),(2,)]

df_Numbers= sc.parallelize(dict_Numbers)

schema1 = StructType([  StructField("Value1", IntegerType(), True)])

df = spark.createDataFrame(df_Numbers, schema= schema1)
#df.printSchema()
df.show()


l=[(83.33,)]           #note the comma (,)
schema = StructType([StructField("value", DoubleType(), True)])
df= spark.createDataFrame(l,schema)
df.show()

# List
data = [('Category A', Decimal(100), "This is category A"),
        ('Category B', Decimal(120), "This is category B"),
        ('Category C', Decimal(150), "This is category C")]

# Create a schema for the dataframe
schema = StructType([
    StructField('Category', StringType(), True),
    StructField('Count', DecimalType(), True),
    StructField('Description', StringType(), True)
])

# Convert list to RDD
rdd = spark.sparkContext.parallelize(data)

# Create data frame
df = spark.createDataFrame(rdd,schema)
print(df.schema)
df.show()

#listNumbers = df_Numbers.take(3) #foreach(print)
#print(listNumbers)
#df_Numbers.show(3)
