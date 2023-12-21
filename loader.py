import pandas as pd

# file_path = "ar41_cleaned.csv"
# file_path = "ar41_for_ulb.csv"
# file_path = "ar41_sample_10k.csv"
# file_path = "ar41_sample_200k.csv"
# file_path = "ar41_for_ulb_mini.csv"
file_path = "h.csv"  # TODO : full file ?
# file_path = "C:/Users/sezne/Downloads/ar41_diff.csv"

hist_data = pd.read_csv(file_path, sep=';')
maps_data = hist_data
