import statistics as st
from math import sqrt

def get_lambda_mom(sample: list[float]) -> float:
    mean = st.mean(sample)
    return mean


def get_lambda_mle(sample: list[float]) -> float:
    mean = st.mean(sample)
    return mean

def get_confidence_interval(sample: list[float]) -> tuple[float, float]:
    mean = st.mean(sample)
    dev = 1.96 * sqrt(mean / len(sample))
    interval = (mean - dev, mean + dev)
    return interval