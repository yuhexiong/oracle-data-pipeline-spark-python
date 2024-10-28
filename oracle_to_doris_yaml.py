from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace, when, lit
import yaml
import argparse

spark = SparkSession.builder \
    .appName("MySparkApp") \
    .config("spark.some.config.option", "config-value") \
    .getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# args
parser = argparse.ArgumentParser(description='setting yaml file.')
parser.add_argument('-f', '--file', type=str, required=True, help='yaml configuration file name')
args = parser.parse_args()

# setting yaml
with open(args.file, "r") as file:
    config = yaml.safe_load(file)

source = config['source']
df = spark.read \
    .format("jdbc") \
    .option("url", source["url"]) \
    .option("dbtable", source["dbtable"]) \
    .option("user", source["user"]) \
    .option("password", source["password"]) \
    .load()

df.show(5)

process = config['process']
selected_columns = []
for field in process["fields"]:
    # regex
    column = regexp_replace(col(field['name']), r"(\r\n|\n|\r|\t|\r)", "").alias(field['alias'])

    # default
    if "default" in field:
        column = when(column.isNull(), lit(field["default"])).otherwise(column)

    column = column.alias(field['alias'])
    selected_columns.append(column)
processed_df = df.select(*selected_columns)

# sink doris
sink = config['sink']
ds = processed_df \
    .write \
    .mode("append") \
    .format("doris") \
    .option("checkpointLocation", "./checkpoint") \
    .option("doris.table.identifier", sink["table"]) \
    .option("doris.fenodes", sink["feNodes"]) \
    .option("user", sink["user"]) \
    .option("password", sink["password"]) \
    .save()
