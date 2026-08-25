"""PySpark transformations for MLApp."""
from pyspark.sql import DataFrame


def clean_data(df):
    df = df.na.drop(how='any')
    df = df.filter(df['amount'].isNotNull())
    return df


def calculate_totals(df: DataFrame) -> DataFrame:
    """Calculate total spend per customer."""
    from pyspark.sql import functions as F
    return df.groupBy("customer_id").agg(
        F.sum("amount").alias("total_spend")
    )