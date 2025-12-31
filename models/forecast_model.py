import pandas as pd


class ForecastModel:
    """
    Simple forecasting helpers for FP&A:
    - Run-rate forecast
    - Simple growth forecast
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def add_run_rate_forecast(self, metric: str = "Actuals") -> pd.DataFrame:
        """
        Very simple run-rate forecast:
        - Take the latest month actual for each cost center
        - Annualize it for the remaining months.
        """
        df = self.df.copy()
        df["Month_Num"] = df["Month"].astype(str).str.slice(5, 7).astype(int)

        latest_per_cc = (
            df.sort_values("Month_Num")
            .groupby("CostCenter")
            .tail(1)[["CostCenter", metric, "Month_Num"]]
            .rename(columns={metric: "Latest_Value"})
        )

        # Merge back
        df = df.merge(
            latest_per_cc[["CostCenter", "Latest_Value", "Month_Num"]],
            on=["CostCenter", "Month_Num"],
            how="left",
            suffixes=("", "_latest"),
        )

        # If Latest_Value is NaN after merge, fill with current Actuals
        df["Latest_Value"] = df["Latest_Value"].fillna(df[metric])

        # Remaining months in year
        df["Remaining_Months"] = 12 - df["Month_Num"]
        df["RunRateForecast_Annualized"] = df["Latest_Value"] * df["Remaining_Months"]

        self.df = df
        return self.df

    def add_simple_growth_forecast(self, growth_rate: float = 0.02) -> pd.DataFrame:
        """
        Apply a simple uniform growth rate to Actuals
        to create a next-period forecast.
        """
        self.df["GrowthForecast"] = self.df["Actuals"] * (1 + growth_rate)
        return self.df
