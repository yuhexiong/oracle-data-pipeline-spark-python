from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace, when, lit

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

pattern = r"(\r\n|\n|\r|\t|\r)"
processed_df = df \
    .select(
        regexp_replace(col("BOOKID"), pattern, "").alias("book_id"),
        regexp_replace(col("TITLE"), pattern, "").alias("title"),
        regexp_replace(col("AUTHOR"), pattern, "").alias("author"),
        regexp_replace(col("PUBLICATIONYEAR"), pattern,"").alias("publication_year"),
        regexp_replace(col("GENRE"), pattern, "").alias("genre"),
        regexp_replace(col("RATING"), pattern, "").alias("rating"),
        when(regexp_replace(col("RATING"), pattern, "").isNull(), lit(0))
            .otherwise(regexp_replace(col("RATING"), pattern, ""))
            .alias("wo_create_date"),
        regexp_replace(col("STATUS"), pattern, "").alias("status")
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
