"""
Script to:
1) Load already processed OPEX data
2) Generate simple run-rate & growth forecasts
3) Export result for visualization or further analysis
"""

import pandas as pd
from pathlib import Path
from models.forecast_model import ForecastModel

INPUT_PATH = Path("data") / "opex_processed_for_powerbi.csv"
OUTPUT_PATH = Path("data") / "opex_with_forecast.csv"


def main():
    df = pd.read_csv(INPUT_PATH)

    forecast_model = ForecastModel(df)
    df = forecast_model.add_run_rate_forecast(metric="Actuals")
    df = forecast_model.add_simple_growth_forecast(growth_rate=0.03)

    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Forecasted OPEX data saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
