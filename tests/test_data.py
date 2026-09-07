"""Tests unitarios para modulos de datos."""
import pandas as pd
import pytest
from src.data.cleaning import remove_duplicates, handle_missing


def test_remove_duplicates():
    df = pd.DataFrame({"a": [1, 1, 2], "b": [3, 3, 4]})
    result = remove_duplicates(df)
    assert len(result) == 2


def test_handle_missing_drop():
    df = pd.DataFrame({"a": [1, None, 3], "b": [4, 5, 6]})
    result = handle_missing(df, strategy="drop")
    assert len(result) == 2


def test_handle_missing_mean():
    df = pd.DataFrame({"a": [1.0, None, 3.0]})
    result = handle_missing(df, strategy="mean")
    assert result["a"].isna().sum() == 0
