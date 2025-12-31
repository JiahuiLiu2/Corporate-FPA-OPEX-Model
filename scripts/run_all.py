"""
High-level pipeline:
1) Run variance analysis (Budget vs Actual, etc.)
2) Run forecast pipeline (run-rate + growth)
This simulates a monthly FP&A refresh process.
"""

import subprocess


def main():
    print("Step 1: Running variance analysis...")
    subprocess.run(["python", "scripts/variance_analysis.py"], check=True)

    print("Step 2: Running forecast pipeline...")
    subprocess.run(["python", "scripts/forecast_pipeline.py"], check=True)

    print("All steps completed. Data is ready for Power BI / analysis.")


if __name__ == "__main__":
    main()
