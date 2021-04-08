import pandas as pd

topicbyUser= [('User1','Topic1'),('User1','Topic2'),('User2','Topic1'),('User2','Topic3')]

df_topic= pd.DataFrame(topicbyUser, columns =['User', 'Topic'])
print(df_topic.groupby('Topic').count().sort_values('User', ascending=False).head(2))