import pandas as pd
import random
if __name__ == "__main__":
    df = pd.read_csv(
        "assets/salary.csv",
        names=["name", "salary"],
    )
    assert df is not None, "file could not be read, check with os.path.exists()"
    df["salary"] = df["salary"].apply(lambda s: random.randint(1000, 100000))
    df.to_csv("assets/salary.csv", index=False)
