import pyspark.sql.functions as func
from pyspark.sql import Window

windowSpec = Window.partitionBy(df['Role'])
df2 = df.withColumn('mean_salary', func.mean(df['Salary']).over(windowSpec))
df2.show()