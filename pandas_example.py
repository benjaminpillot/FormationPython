# -*- coding: utf-8 -*-

""" Module summary description.

More detailed description.
"""

import pandas as pd


countries = pd.read_csv('country.csv', index_col=0)

for country in countries.index:
    print(f"{country}'s population: %d million(s)" % countries.loc[country, "population"])

for country in countries.loc[countries["population"] > 150].index:
    print(f"More than 150 million people live in {country}")

for european_country in countries.loc[countries["continent"] == "Europe"].index:
    print(f"{european_country} is in Europe")

english = countries["language"].apply(lambda language: True if "english" in language.lower() else False)
for english_country in countries.loc[english].index:
    print(f"They speak english in {english_country}")

french = countries["language"].apply(lambda language: True if "french" in language.lower() else False)
for french_country in countries.loc[french].index:
    print(f"They speak french in {french_country}")

africa = countries["continent"] == "Africa"
for african_french_country in countries.loc[french & africa].index:
    print(f"They speak french in {african_french_country}, which is located in Africa")
