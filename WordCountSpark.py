
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark import sql
import re
import pyspark.sql.functions as F

def remove_non_word_characters(col):
    return F.regexp_replace(col, "[^\\w\\s]+", "")

def do_word_counts(lines):
    counts = (lines.flatMap(lambda x: x.split())
                         .map(lambda x: (x,1))
                         .reduceByKey(lambda x,y: (x+y)))
    results = {word: count for word, count in counts.collect()}
    return results





spark = SparkSession.builder.appName('Word Count').master('local[*]').getOrCreate()
book= 'Hola Faider, HOLA Juan, Hola Mundo, Hola Pedro Faider'
book= re.sub('[,.!]','',book).lower()
words= book.split(' ')


#words = book.map(lambda  line: line.split(' ')) 
input_rdd = spark.sparkContext.parallelize(words, 1)
result = do_word_counts(input_rdd)
print (result)
#input_rdd.take(5)
#rddCollect = input_rdd.collect()
#print(rddCollect, count)
    

