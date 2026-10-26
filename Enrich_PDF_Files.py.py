# Databricks notebook source
from pyspark.sql import functions as F
from pyspark.sql.types import StringType

print("✓ Libraries imported successfully")

# COMMAND ----------

products_df = spark.table("agentic_catalog.agentic_schema.products")

print("Products Table Schema:")
products_df.printSchema()
print(f"\nTotal products: {products_df.count()}")

# Display sample data
print("\nSample products:")
display(products_df.limit(5))

# COMMAND ----------

product_docs_df = spark.table("agentic_catalog.agentic_schema.product_docs")

print("Product Docs Table Schema:")
product_docs_df.printSchema()
print(f"\nTotal documents: {product_docs_df.count()}")

# Display sample data (truncate long text)
print("\nSample documents:")
display(product_docs_df.limit(5))

# COMMAND ----------

joined_df = products_df.join(
    product_docs_df,
    on="product_name",
    how="inner"
)

print("Joined Table Schema:")
joined_df.printSchema()
print(f"\nTotal joined records: {joined_df.count()}")

# Display sample joined data
print("\nSample joined data:")
display(joined_df.limit(3))

# COMMAND ----------

indexed_df = joined_df.withColumn(
    "indexed_doc",
    F.concat(
        F.lit("<product_category>"),
        F.col("product_category"),
        F.lit("</product_category>\n"),
        F.lit("<product_sub_category>"),
        F.col("product_sub_category"),
        F.lit("</product_sub_category>\n"),
        F.lit("<product_name>"),
        F.col("product_name"),
        F.lit("</product_name>\n"),
        F.lit("<product_doc>\n"),
        F.col("product_doc"),
        F.lit("\n</product_doc>")
    )
)

print("✓ Indexed document column created")

# COMMAND ----------

print("\nSample indexed document (first 500 characters):")
sample_indexed = indexed_df.select("product_name", "indexed_doc").first()
print(f"\nProduct: {sample_indexed['product_name']}")
print(f"\nIndexed Doc:\n{sample_indexed['indexed_doc'][:500]}...")

# COMMAND ----------

final_df = indexed_df.select(
    "product_id",
    "product_name",
    "product_doc",
    "product_category",
    "product_sub_category",
    "indexed_doc"
)

print("Final Table Schema:")
final_df.printSchema()
print(f"\nTotal records: {final_df.count()}")

# Display final sample
print("\nSample final data:")
display(final_df.limit(5))

# COMMAND ----------

target_table = "agentic_catalog.agentic_schema.product_docs_combined"

# COMMAND ----------

final_df.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable(target_table)

print(f"✓ Table saved successfully: {target_table}")
print(f"\nTotal records written: {spark.table(target_table).count()}")

# COMMAND ----------

verify_df = spark.table("agentic_catalog.agentic_schema.product_docs_combined")

print("Verification Results:")
print(f"Total records: {verify_df.count()}")
print("\nTable Schema:")
verify_df.printSchema()

# Display sample records
print("\nSample Records:")
display(verify_df.limit(5))

# COMMAND ----------

spark.sql("""
ALTER TABLE agentic_catalog.agentic_schema.product_docs_combined
SET TBLPROPERTIES (delta.enableChangeDataFeed = true)
""")