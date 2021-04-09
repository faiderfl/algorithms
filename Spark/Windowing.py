from pyspark.sql.window import *
from pyspark.sql.functions import dense_rank, col

spec = Window.partitionBy('tag_name').orderBy(col('created_at').desc())

q4.withColumn('rnk', dense_rank().over(spec)).filter('rnk<3').show()