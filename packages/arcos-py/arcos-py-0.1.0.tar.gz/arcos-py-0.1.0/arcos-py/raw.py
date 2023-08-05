# Raw Functions"

def get_raw_county_data(state, county = '',verification = True, key = 'WaPo'):
    '''(str(two letter abbreviation), bool, str, str) -> pd.df
        Returns all data by county (Will be large and could take extra time to load)

        >>>get_raw_county_data('OH', 'Summit')
            EXAMPLE OUTPUT
    '''

    base_url = 'https://arcos-api.ext.nile.works/v1/'
    function_url = 'county_data?'
    add_state = 'state=' + state
    add_county = '&county=' + county
    add_key = '&key=' + key
    full_url = base_url + function_url + add_state + add_county + add_key

    if verification == True:
        print(full_url)
        county_data_df = json_normalize(requests.get(full_url).json())
        return county_data_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)


def get_raw_buyer_details(state, county = '',verification = True, key = 'WaPo'):
    '''(str(two letter abbreviation), bool, str, str) -> pd.df
        Returns buyer details (mail order, pharmacy, retail, practitioner, etc)

        >>>get_raw_buyer_details('OH', 'Summit')
            EXAMPLE OUTPUT
    '''

    base_url = 'https://arcos-api.ext.nile.works/v1/'
    function_url = 'buyer_details?'
    add_state = 'state=' + state
    add_county = '&county=' + county
    add_key = '&key=' + key
    full_url = base_url + function_url + add_state + add_county + add_key

    if verification == True:
        print(full_url)
        buyer_details_df = json_normalize(requests.get(full_url).json())
        return buyer_details_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)        

def get_raw_reporter_details(state, county = '',verification = True, key = 'WaPo'):
    '''(str(two letter abbreviation), bool, str, str) -> pd.df
        Returns Reporter (Manufacturers and Distributors) details such as addresses

        >>>get_raw_reporter_details('OH', 'Summit')
            EXAMPLE OUTPUT
    '''

    base_url = 'https://arcos-api.ext.nile.works/v1/'
    function_url = 'reporter_details?'
    add_state = 'state=' + state
    add_county = '&county=' + county
    add_key = '&key=' + key
    full_url = base_url + function_url + add_state + add_county + add_key

    if verification == True:
        print(full_url)
        reporter_details_df = json_normalize(requests.get(full_url).json())
        return reporter_details_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)


