import numpy as np
import pandas as pd
import pytest

from src.data.cleaning import handle_missing, remove_duplicates
from src.data.feature_engineering import compute_density


def test_remove_duplicates():
    df = pd.DataFrame({"a": [1, 1, 2], "b": [3, 3, 4]})
    assert len(remove_duplicates(df)) == 2


def test_handle_missing_mean_and_mode():
    numeric = pd.DataFrame({"a": [1.0, None, 3.0]})
    assert handle_missing(numeric, "mean")["a"].isna().sum() == 0

    categorical = pd.DataFrame({"x": ["a", None, "a", "b"]})
    assert handle_missing(categorical, "mode").loc[1, "x"] == "a"


def test_handle_missing_rejects_unknown_strategy():
    with pytest.raises(ValueError):
        handle_missing(pd.DataFrame({"a": [1, None]}), "magic")


def test_compute_density_invalid_area_becomes_nan():
    df = pd.DataFrame({"units": [10, 5], "area": [100.0, 0.0]})
    density = compute_density(df, "units", "area")
    assert density.iloc[0] == pytest.approx(0.1)
    assert np.isnan(density.iloc[1])
