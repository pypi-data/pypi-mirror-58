# Summary Functions

def get_summ_combined_county_annual(state, county = '',verification = True, key = 'WaPo'):
    '''(str(two letter abbreviation), str, bool, str) -> pd.df
        Returns seller details such as addresses

        >>>get_summ_combined_county_annual('OH', 'Summit')
            EXAMPLE OUTPUT
    '''

    base_url = 'https://arcos-api.ext.nile.works/v1/'
    function_url = 'combined_county_annual?'
    add_state = 'state=' + state
    add_county = '&county=' + county
    add_key = '&key=' + key
    full_url = base_url + function_url + add_state + add_county + add_key

    if verification == True:
        print(full_url)
        combined_county_annual_df = json_normalize(requests.get(full_url).json())
        return combined_county_annual_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)
        
        
def get_summ_combined_county_monthly(state, county = '',verification = True, key = 'WaPo'):
    '''(str(two letter abbreviation), str, bool, str) -> pd.df
        Returns seller details such as addresses

        >>>get_summ_combined_county_monthly('OH', 'Summit')
            EXAMPLE OUTPUT
    '''

    base_url = 'https://arcos-api.ext.nile.works/v1/'
    function_url = 'combined_county_monthly?'
    add_state = 'state=' + state
    add_county = '&county=' + county
    add_key = '&key=' + key
    full_url = base_url + function_url + add_state + add_county + add_key

    if verification == True:
        print(full_url)
        combined_county_monthly_df = json_normalize(requests.get(full_url).json())
        return combined_county_monthly_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)
        
def get_summ_total_pharmacies_county(state, county = '',verification = True, key = 'WaPo'):
    '''(str(two letter abbreviation), str, bool, str) -> pd.df
        Returns all pharmacy totals by county (Will be large and could take extra time to load)

        >>>get_summ_total_pharmacies_county('OH', 'Summit')
            EXAMPLE OUTPUT
    '''

    base_url = 'https://arcos-api.ext.nile.works/v1/'
    function_url = 'total_pharmacies_county?'
    add_state = 'state=' + state
    add_county = '&county=' + county
    add_key = '&key=' + key
    full_url = base_url + function_url + add_state + add_county + add_key

    if verification == True:
        print(full_url)
        total_pharmacies_county_df = json_normalize(requests.get(full_url).json())
        return total_pharmacies_county_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)
        
def get_summ_total_manufacturers_county(state, county = '',verification = True, key = 'WaPo'):
    '''(str(two letter abbreviation), str, bool, str) -> pd.df
        Returns all Manufacturer totals by county (Will be large and could take extra time to load)

        >>>get_summ_total_manufacturers_county('OH', 'Summit')
            EXAMPLE OUTPUT
    '''

    base_url = 'https://arcos-api.ext.nile.works/v1/'
    function_url = 'total_manufacturers_county?'
    add_state = 'state=' + state
    add_county = '&county=' + county
    add_key = '&key=' + key
    full_url = base_url + function_url + add_state + add_county + add_key

    if verification == True:
        print(full_url)
        total_manufacturers_county_df = json_normalize(requests.get(full_url).json())
        return total_manufacturers_county_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)
        
def get_summ_total_distributors_county(state, county = '',verification = True, key = 'WaPo'):
    '''(str(two letter abbreviation), str, bool, str) -> pd.df
        Returns all Distributor totals by county (Will be large and could take extra time to load)

        >>>get_summ_total_distributors_county('OH', 'Summit')
            EXAMPLE OUTPUT
    '''

    base_url = 'https://arcos-api.ext.nile.works/v1/'
    function_url = 'total_distributors_county?'
    add_state = 'state=' + state
    add_county = '&county=' + county
    add_key = '&key=' + key
    full_url = base_url + function_url + add_state + add_county + add_key

    if verification == True:
        print(full_url)
        total_distributors_county_df = json_normalize(requests.get(full_url).json())
        return total_distributors_county_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)
        
def get_summ_total_pharmacies_state(state,verification = True, key = 'WaPo'):
    '''(str(two letter abbreviation), str, bool, str) -> pd.df
        Returns all pharmacy totals by state (Will be large and could take extra time to load)

        >>>get_summ_total_pharmacies_state('OH')
            EXAMPLE OUTPUT
    '''

    base_url = 'https://arcos-api.ext.nile.works/v1/'
    function_url = 'total_pharmacies_state?'
    add_state = 'state=' + state
    add_key = '&key=' + key
    full_url = base_url + function_url + add_state + add_key

    if verification == True:
        print(full_url)
        total_pharmacies_state_df = json_normalize(requests.get(full_url).json())
        return total_pharmacies_state_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)
        
def get_summ_total_manufacturers_state(state,verification = True, key = 'WaPo'):
    '''(str(two letter abbreviation), str, bool, str) -> pd.df
        Returns all Manufacturer totals by state (Will be large and could take extra time to load) 

        >>>get_summ_total_manufacturers_state('OH', 'Summit')
            EXAMPLE OUTPUT
    '''

    base_url = 'https://arcos-api.ext.nile.works/v1/'
    function_url = 'total_manufacturers_state?'
    add_state = 'state=' + state
    add_key = '&key=' + key
    full_url = base_url + function_url + add_state + add_key

    if verification == True:
        print(full_url)
        total_manufacturers_state_df = json_normalize(requests.get(full_url).json())
        return total_manufacturers_state_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)
        
def get_summ_total_distributors_state(state,verification = True, key = 'WaPo'):
    '''(str(two letter abbreviation), str, bool, str) -> pd.df
        Returns all Distributor totals by state (Will be large and could take extra time to load) 

        >>>get_summ_total_distributors_state('OH', 'Summit')
            EXAMPLE OUTPUT
    '''

    base_url = 'https://arcos-api.ext.nile.works/v1/'
    function_url = 'total_distributors_state?'
    add_state = 'state=' + state
    add_key = '&key=' + key
    full_url = base_url + function_url + add_state + add_key

    if verification == True:
        print(full_url)
        total_distributors_state_df = json_normalize(requests.get(full_url).json())
        return total_distributors_state_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL and state are correct: ', full_url)

def get_summ_combined_buyer_annual(state, county = '',verification = True, key = 'WaPo'):
    '''(str(two letter abbreviation), str, bool, str) -> pd.df
        Returns summarized annual dosages of pharmacies and practitioners by state and county 

        >>>get_summ_combined_buyer_annual('OH', 'Summit')
            EXAMPLE OUTPUT
    '''

    base_url = 'https://arcos-api.ext.nile.works/v1/'
    function_url = 'combined_buyer_annual?'
    add_state = 'state=' + state
    add_county = '&county=' + county
    add_key = '&key=' + key
    full_url = base_url + function_url + add_state + add_county + add_key

    if verification == True:
        print(full_url)
        combined_buyer_annual_df = json_normalize(requests.get(full_url).json())
        return combined_buyer_annual_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)
        
def get_summ_combined_buyer_monthly(state, year, county = '',verification = True, key = 'WaPo'):
    '''(str(two letter abbreviation), str, bool, str) -> pd.df
        Returns dosages by pharmacy or practitioner by county, state, and yea 

        >>>get_summ_combined_buyer_monthly('OH', 'Summit')
            EXAMPLE OUTPUT
    '''

    base_url = 'https://arcos-api.ext.nile.works/v1/'
    function_url = 'combined_buyer_monthly?'
    add_state = 'state=' + state
    add_county = '&county=' + county
    add_year = '&year=' + year
    add_key = '&key=' + key
    full_url = base_url + function_url + add_state + add_county + add_year + add_key

    if verification == True:
        print(full_url)
        combined_buyer_monthly_df = json_normalize(requests.get(full_url).json())
        return combined_buyer_monthly_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)
        