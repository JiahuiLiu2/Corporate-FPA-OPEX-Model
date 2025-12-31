"""
Script to:
1) Load OPEX data
2) Run variance calculations
3) Export processed data for Power BI
"""

import pandas as pd
from pathlib import Path
from models.opex_model import OPEXModel

DATA_PATH = Path("data") / "opex_cost_center_data.csv"
OUTPUT_PATH = Path("data") / "opex_processed_for_powerbi.csv"
SUMMARY_PATH = Path("data") / "opex_costcenter_summary.csv"


def main():
    # 1. Load data
    df = pd.read_csv(DATA_PATH)

    # 2. Build model and calculate variances
    model = OPEXModel(df)
    processed_df = model.get_processed_frame()
    summary_df = model.summarize_by_cost_center()

    # 3. Save for Power BI or further analysis
    processed_df.to_csv(OUTPUT_PATH, index=False)
    summary_df.to_csv(SUMMARY_PATH, index=False)

    print(f"Processed OPEX data saved to: {OUTPUT_PATH}")
    print(f"Cost center summary saved to: {SUMMARY_PATH}")


if __name__ == "__main__":
    main()
