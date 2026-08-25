def segment_customers(df):
    """RFM-based customer segmentation for MLAPP-1234."""
    return df.withColumn(
        "segment",
        F.when(F.col("total_spend").isNull(), "Unknown")
         .when(F.col("total_spend") > 10000, "Premium")
         .when(F.col("total_spend") > 5000, "Gold")
         .when(F.col("total_spend") > 1000, "Silver")
         .otherwise("Bronze")
    )