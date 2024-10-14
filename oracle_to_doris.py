from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("MySparkApp") \
    .config("spark.some.config.option", "config-value") \
    .getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# read oracle
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:oracle:thin:@host:port:service") \
    .option("dbtable", "schema.table") \
    .option("user", "user") \
    .option("password", "password") \
    .load()

df.show(10)

processed_df = df \
    .select(
        col("BOOKID").alias("book_id"),
        col("TITLE").alias("title"),
        col("AUTHOR").alias("author"),
        col("PUBLICATIONYEAR").alias("publication_year"),
        col("GENRE").alias("genre"),
        col("RATING").alias("rating"),
        col("STATUS").alias("status")
    )

# save doris
ds = processed_df \
    .write \
    .mode("append") \
    .format("doris") \
    .option("checkpointLocation", "./checkpoint") \
    .option("doris.table.identifier", "database.table") \
    .option("doris.fenodes", "host:port") \
    .option("user", "user") \
    .option("password", "password") \
    .save()
