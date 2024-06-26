# In a code cell in your Jupyter notebook
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Spark SQL Example") \
    .getOrCreate()

# Create a DataFrame
data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Register the DataFrame as a SQL temporary view
df.createOrReplaceTempView("people")

# Run a Spark SQL query
result = spark.sql("SELECT * FROM people WHERE Age > 30")

# Show the result
result.show()
