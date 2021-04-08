
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

topicbyUserRDD= sc.parallelize(topicbyUser,1)

schema= StructType([(StructField('Users',StringType(),True)), (StructField('Topic',StringType(),True))])

df_UserByTopic = spark.createDataFrame(topicbyUserRDD, schema)
#df_UserByTopic.show()

df_UserByTopic.createOrReplaceTempView('UT')
#spark.sql("Select Topic, COUNT(*) As Quantity FROM UT GROUP BY Topic ORDER BY COUNT(*) DESC LIMIT 2").show()

df_count= df_UserByTopic.groupBy("Topic").count()
#df_count.orderBy("count", ascending=False).show(2)


counts = topicbyUserRDD.map(lambda x: (x[1],1)).reduceByKey(lambda accum,n:(accum+n))

results = counts.take(2) #{topic: topic for topic,count in counts.collect()}
print(results)