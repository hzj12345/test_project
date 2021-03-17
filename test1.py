from pyspark import SparkContext
from operator import add
sc = SparkContext("local", "first app")
#nums = sc.parallelize([1, 2, 3, 4, 5])
#adding = nums.reduce(lambda a,b:a+b)
lines=sc.textFile('D:\spark-3.1.1-bin-hadoop2.7\README.md')
#print(lines.first())
#print(lines.count())
#lines=lines.take(3)
print(lines.cartesian(lines).collect())

#print("Adding all the elements -> %i" % (adding))