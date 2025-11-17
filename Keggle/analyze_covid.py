import pandas as pd
from pathlib import Path
pd.set_option('display.max_rows', 5)
print("setup complete")
fruits_sales = pd.DataFrame({'Apples': [30,],
                            "Bananas": [21]},
                            index=["3", "4"])

print(fruits_sales)

csv_path = Path(__file__).parent / 'data' / 'covid19.csv'
wine_path = Path(__file__).parent / 'data' / 'winemag.csv'
ingridients_path = Path(__file__).parent / 'data' / 'ingridients.csv'

covid_19 = pd.read_csv(csv_path)
wine = pd.read_csv(wine_path)


ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], 
                        index=['Flour', 'Milk', 'Eggs', 'Spam'], 
                        name='Dinner')

ingredients.to_csv(ingridients_path, encoding='utf_8')
