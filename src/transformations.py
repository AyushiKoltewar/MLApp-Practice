"""PySpark transformations for MLApp."""
from pyspark.sql import DataFrame


def clean_data(df: DataFrame) -> DataFrame:
    """Clean transaction data."""
    df = df.filter(df['amount'] > 0)
    return df


def calculate_totals(df: DataFrame) -> DataFrame:
    """Calculate total spend per customer."""
    from pyspark.sql import functions as F
    return df.groupBy("customer_id").agg(
        F.sum("amount").alias("total_spend")
    )