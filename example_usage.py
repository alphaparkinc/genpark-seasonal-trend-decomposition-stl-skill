from client import SeasonalDecomposition

series = [10, 12, 15, 9, 11, 13, 16, 10, 12, 14, 17, 11]
res = SeasonalDecomposition.decompose(series, period=4)

print("Decomposition Complete:")
print("Seasonal Component (Sample):", [round(s, 2) for s in res['seasonal'][:4]])
print("Valid Trend Points Count:", sum(1 for t in res['trend'] if t is not None))
