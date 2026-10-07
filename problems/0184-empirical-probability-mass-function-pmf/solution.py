from collections import Counter

def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    if len(samples) == 0:
        return []
    proba = []
    return [(k, v/len(samples)) for k, v in sorted(Counter(samples).items(), key=lambda p:p[0])]