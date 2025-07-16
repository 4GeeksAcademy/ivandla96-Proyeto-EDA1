from utils import db_connect
engine = db_connect()

# your code here
import pandas as pd

airbhb_csv = pd.read_csv("https://raw.githubusercontent.com/4GeeksAcademy/data-preprocessing-project-tutorial/main/AB_NYC_2019.csv")


airbhb_csv.head()