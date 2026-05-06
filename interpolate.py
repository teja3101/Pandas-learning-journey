import pandas as pd

data = pd.read_csv("C:\\Users\\tejud\\OneDrive\\Documents\\Desktop\\CTVed\\Coding with Harry Potter\\Python\\Pandas\\Biggg Data.csv")
# print(data)

# In pandas, interpolate() fills missing values by guessing a value between the numbers before and after it
# it will not work with string, works only with numbers
# print(data.interpolate())

# method : {'linear', 'time', 'index', 'values', 'nearest', 'zero', 'slinear', 'quadratic', 'cubic', 'barycentric', 'krogh', 'polynomial', 'spline', 'piecewise_polynomial', 'from_derivatives', 'pchip', 'akima'}
# These methods tell pandas how to guess the missing values
# print(data.interpolate(method="linear"))
# print(data.interpolate(method="linear", axis=0))

# Fills missing values using default linear method, But only fills maximum 2 consecutive NaN values, Direction: forward (default)
# print(data.interpolate(limit=2))

# Same as above, but explicitly says: Fill from top → downward, Fill only 2 missing values in a row, This is basically the default behavior
# print(data.interpolate(limit_direction="forward", limit=2))

# Fills missing values from bottom → upward, Still fills only 2 consecutive NaN values
# print(data.interpolate(limit_direction="backward", limit=2))

# Fills only the missing values that are in between valid values
# print(data.interpolate(limit_area="inside"))

# Fills only the missing values at the edges (start or end)
# print(data.interpolate(limit_area="outside"))

# It fills up to 2 missing values from both directions and updates the original data (so it prints None because of inplace=True).
# inplace=True means modify the original data directly instead of returning a new copy
print(data.interpolate(limit_direction="both", limit=2, inplace=True))




