import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.predict import predict_yield


def test_predict_returns_float():
    result = predict_yield(22.0, 88.0, 920)

    assert isinstance(result, float)
    assert 0 < result < 50


def test_prediction_changes():
    low = predict_yield(22.0, 75.0, 920)
    high = predict_yield(22.0, 92.0, 920)

    assert low != high