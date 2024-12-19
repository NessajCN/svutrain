import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv(
        "assets/salary.csv",
        names=["name", "salary"],
    )
    assert df is not None, "file could not be read, check with os.path.exists()"
    df["salary"] = df["salary"].apply(lambda s: s * 2)
    df.to_excel("output/salary.xlsx", sheet_name="double_salary")
