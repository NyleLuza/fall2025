import kagglehub
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
# load dataset
path = kagglehub.dataset_download("iammustafatz/diabetes-prediction-dataset")

# load dataset into  pandas dataframe
data = pd.read_csv(f"{path}\diabetes_prediction_dataset.csv")

split = StratifiedShuffleSplit(data, test_size=0.2)
print(train_data)