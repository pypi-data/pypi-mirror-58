# -*- coding: utf-8 -*-

# Copyright (c) ALT-F1 SPRL, Abdelkrim Boujraf. All rights reserved.
# Licensed under the EUPL License, Version 1.2. See LICENSE in the project root for license information.
 
# get the list of countries in the field place

from country_list import countries_for_language
import pycountry
import inspect
import logging

def get_list_of_countries_in_text(df, place="place", languages_to_check=["en", "fr", "nl"]):
    """
    get the list of countries stored in the field
    'place' in transactions stored in twikey.

    The places written using a language matching the Languages_to_check list will be found (e.g. en, fr or nl).

    Return
    ----------

    list of countries (ISO-3) matching the names of countries found in the field 'place'

    Parameters
    ----------
    df : pandas.DataFrame
    contains a dataframe containing the field containing country names

    place: text
    field containing the country name

    languages_to_check : list
    list of languages used inside the field 'place' that needs to be checked (ISO 3166-1 alpha-2 codes)

    Exmample
    --------
    
    countries_utils.get_list_of_countries_in_text(
        pd.DataFrame(np.array(['Belgium', 'Frankrijk', 'Royaume-Uni']), columns=['place']),
        place="place",
        languages_to_check=["en", "fr", "nl"]
        )
        
    returns

    (['Belgium', 'France', 'United Kingdom'], {'France', 'Belgium', 'United Kingdom'})
    """

    logging.info(f"{'='*25} {inspect.currentframe().f_code.co_name}")
    logging.info(f"len(df containing list of places) : {len(df)}")

    country_iso_set = set()
    country_iso_list = []

    for index, value in df[place].iteritems():   
        found=False
        for language_to_check in languages_to_check:
            # keep the list of countries is the selected language
            countries = dict(countries_for_language(language_to_check)) 
            for country in countries:
                if countries[country] in value:
                    # alpha_3 = pycountry.countries.get(alpha_2=country).alpha_3
                    country_name = pycountry.countries.get(alpha_2=country).name
                    country_iso_set.add(country_name)
                    country_iso_list.append(country_name)
                    found=True
                    break
            if found == True:
                break
        if found == False:
            logging.error(f"Country is NOT FOUND {value} in this list {languages_to_check}")
            country_iso_list.append(None)
    logging.debug(f"len(country_iso_list) : {len(country_iso_list)}")
    logging.debug(f"len(country_iso_set) : {len(country_iso_set)}")
    return country_iso_list, country_iso_set
