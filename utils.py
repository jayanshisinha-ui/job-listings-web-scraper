import pandas as pd
import os
from datetime import datetime

def save_to_csv(data, filename):

    os.makedirs("output", exist_ok=True)

    file_path = os.path.join("output", filename)

    df = pd.DataFrame(data)

    df["Scraped Date"] = datetime.now()

    df.to_csv(file_path, index=False)

    print("Data saved successfully at:", file_path)