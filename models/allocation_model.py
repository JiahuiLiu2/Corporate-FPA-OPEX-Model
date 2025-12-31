import pandas as pd


class AllocationModel:
    """
    Simple cost allocation model.
    Example: allocate IT or HR shared service cost
    to other cost centers using headcount or another driver.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def allocate_costs(self, total_cost: float, basis_column: str) -> pd.DataFrame:
        """
        Allocate a given total_cost across cost centers based on a driver column.
        e.g., basis_column = "Headcount"
        """
        if basis_column not in self.df.columns:
            raise ValueError(f"Basis column '{basis_column}' not found in dataframe.")

        total_basis = self.df[basis_column].sum()
        if total_basis == 0:
            raise ValueError("Total basis is zero; cannot allocate cost.")

        self.df["AllocatedCost"] = total_cost * (self.df[basis_column] / total_basis)
        return self.df
