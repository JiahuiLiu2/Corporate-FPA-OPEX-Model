import pandas as pd


class OPEXModel:
    """
    Core OPEX model for cost centers.
    - Calculates total OPEX
    - Calculates variances
    - Summarizes by cost center
    """

    def __init__(self, df: pd.DataFrame):
        # Work on a copy to avoid mutating original
        self.df = df.copy()

    @classmethod
    def from_csv(cls, path: str) -> "OPEXModel":
        """Create an OPEXModel from a CSV file."""
        df = pd.read_csv(path)
        return cls(df)

    def calculate_total_opex(self) -> pd.DataFrame:
        """Add a Total_OPEX column based on key cost categories."""
        self.df["Total_OPEX"] = (
            self.df["Travel"]
            + self.df["Software"]
            + self.df["VendorSpend"]
            + self.df["OfficeExpense"]
        )
        return self.df

    def calculate_variances(self) -> pd.DataFrame:
        """Add variance columns: Budget vs Actual, etc."""
        self.df["Budget_vs_Actual"] = self.df["Actuals"] - self.df["Budget"]
        self.df["Forecast_vs_Actual"] = self.df["Actuals"] - self.df["Forecast"]
        self.df["Budget_vs_Forecast"] = self.df["Forecast"] - self.df["Budget"]
        return self.df

    def summarize_by_cost_center(self) -> pd.DataFrame:
        """
        Aggregate P&L-style view per cost center.
        Useful as a table for Power BI dashboards.
        """
        summary = (
            self.df.groupby("CostCenter")[
                ["Budget", "Forecast", "Actuals",
                 "Budget_vs_Actual", "Forecast_vs_Actual", "Budget_vs_Forecast"]
            ]
            .sum()
            .reset_index()
        )
        return summary

    def get_processed_frame(self) -> pd.DataFrame:
        """
        Run full pipeline: total opex + variances.
        """
        self.calculate_total_opex()
        self.calculate_variances()
        return self.df
