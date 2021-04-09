import pyspark.sql.functions as func
from pyspark.sql import Window

windowSpec = Window.partitionBy(df['Role'])
df2 = df.withColumn('mean_salary', func.mean(df['Salary']).over(windowSpec))
df2.show()

SELECT approx_percentile(10.0, array(0.5, 0.4, 0.1), 100);
SELECT approx_percentile(val, 0.5, 100);