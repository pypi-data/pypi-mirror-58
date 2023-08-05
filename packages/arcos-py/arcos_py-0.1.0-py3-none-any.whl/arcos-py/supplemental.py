# "Supplemental" Functions

def get_supp_county_population(state, county = '',verification = True, key = 'WaPo'):
    '''(str(two letter abbreviation), bool, str, str) -> pd.df
        Returns historical county population data

        >>>get_supp_county_population('OH', 'Summit')
            EXAMPLE OUTPUT
    '''

    base_url = 'https://arcos-api.ext.nile.works/v1/'
    function_url = 'county_population?'
    add_state = 'state=' + state
    add_county = '&county=' + county
    add_key = '&key=' + key
    full_url = base_url + function_url + add_state + add_county + add_key

    if verification == True:
        print(full_url)
        county_population_df = json_normalize(requests.get(full_url).json())
        return county_population_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)
        
def get_supp_not_pharmacies(key = 'WaPo', verification = True):
    '''(str(two letter abbreviation), bool, str, str) -> pd.df
        Returns list of 330+ BUYER_DEA_NOs that we've identified as mail order or hospitals and not retail or chain pharmacies)

        >>>get_supp_not_pharmacies('OH', 'Summit')
            EXAMPLE OUTPUT
    '''

    base_url = 'https://arcos-api.ext.nile.works/v1/'
    function_url = 'not_pharmacies?'
    add_key = '&key=' + key
    full_url = base_url + function_url + add_key

    if verification == True:
        print(full_url)
        not_pharmacies_df = json_normalize(requests.get(full_url).json())
        return not_pharmacies_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)
        
def get_supp_state_population(state, verification = True, key = 'WaPo'):
    '''(str(two letter abbreviation) bool, str) -> pd.df
        Returns historical state population data

        >>>get_supp_state_population('OH', 'Summit')
            EXAMPLE OUTPUT
    '''

    base_url = 'https://arcos-api.ext.nile.works/v1/'
    function_url = 'state_population?'
    add_state = 'state=' + state
    #add_county = '&county=' + county
    add_key = '&key=' + key
    full_url = base_url + function_url + add_state + add_key

    if verification == True:
        print(full_url)
        state_population_df = json_normalize(requests.get(full_url).json())
        return state_population_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL and state are correct: ', full_url)
        
def get_supp_pharmacy_latlon(state, county = '',verification = True, key = 'WaPo'):
    '''(str(two letter abbreviation), bool, str, str) -> pd.df
        Returns pharmacy latitude and longitude data by Buyer_DEA_Number

        >>>get_supp_pharmacy_latlon('OH', 'Summit')
            EXAMPLE OUTPUT
    '''

    base_url = 'https://arcos-api.ext.nile.works/v1/'
    function_url = 'pharmacy_latlon?'
    add_state = 'state=' + state
    add_county = '&county=' + county
    add_key = '&key=' + key
    full_url = base_url + function_url + add_state + add_county + add_key

    if verification == True:
        print(full_url)
        pharmacy_latlon_df = json_normalize(requests.get(full_url).json())
        return pharmacy_latlon_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)
        
def get_supp_pharmacy_counties(state, county = '',verification = True, key = 'WaPo'):
    '''(str(two letter abbreviation), bool, str, str) -> pd.df
        Returns each pharmacy's county FIPS id number by Buyer DEA Number

        >>>get_supp_pharmacy_counties('OH', 'Summit')
            EXAMPLE OUTPUT
    '''

    base_url = 'https://arcos-api.ext.nile.works/v1/'
    function_url = 'pharmacy_counties?'
    add_state = 'state=' + state
    add_county = '&county=' + county
    add_key = '&key=' + key
    full_url = base_url + function_url + add_state + add_county + add_key

    if verification == True:
        print(full_url)
        pharmacy_counties_df = json_normalize(requests.get(full_url).json())
        return pharmacy_counties_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)
        
def get_supp_pharmacy_tracts(state, county = '',verification = True, key = 'WaPo'):
    '''(str(two letter abbreviation), bool, str, str) -> pd.df
        Returns each pharmacy's census tract FIPS code

        >>>get_supp_pharmacy_tracts('OH', 'Summit')
            EXAMPLE OUTPUT
    '''

    base_url = 'https://arcos-api.ext.nile.works/v1/'
    function_url = 'pharmacy_tracts?'
    add_state = 'state=' + state
    add_county = '&county=' + county
    add_key = '&key=' + key
    full_url = base_url + function_url + add_state + add_county + add_key

    if verification == True:
        print(full_url)
        pharmacy_tracts_df = json_normalize(requests.get(full_url).json())
        return pharmacy_tracts_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)
        
def get_supp_pharmacy_cbsa(state, county = '',verification = True, key = 'WaPo'):
    '''(str(two letter abbreviation), bool, str, str) -> pd.df
        Returns pharmacy core-based statistical area FIPS code

        >>>get_supp_pharmacy_cbsa('OH', 'Summit')
            EXAMPLE OUTPUT
    '''

    base_url = 'https://arcos-api.ext.nile.works/v1/'
    function_url = 'pharmacy_cbsa?'
    add_state = 'state=' + state
    add_county = '&county=' + county
    add_key = '&key=' + key
    full_url = base_url + function_url + add_state + add_county + add_key

    if verification == True:
        print(full_url)
        pharmacy_cbsa_df = json_normalize(requests.get(full_url).json())
        return pharmacy_cbsa_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)        