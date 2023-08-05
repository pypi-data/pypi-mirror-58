# National (Aggregate) Functions

def get_national_pharmacy_data(us_abbr_list: list, verification: bool = False, key: str = 'WaPo'):
    '''(string) -> pd.df
        Returns all pharmacy totals from all states (Will be large and could take extra time to load) 

        >>>get_national_pharmacy_data(verification = True)
            EXAMPLE OUTPUT
    '''
    national_pharm_data = pd.DataFrame()

    if verification == True:
        for state_abbr in us_abbr_list:
            print(state_abbr)
            state_df = get_summ_total_pharmacies_state(state_abbr, verification, key)
            national_pharm_data = national_pharm_data.append(state_df)
        return national_pharm_data
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ')
        
def get_national_pharmacy_latlon(us_abbr_list: list, county = "", verification: bool = False, key: str = 'WaPo'):
    '''(string) -> pd.df
        Returns all pharmacy latlon from all states (Will be large and could take extra time to load) 

        >>>get_national_pharmacy_latlon(verification = True)
            EXAMPLE OUTPUT
    '''
    national_pharm_latlon_data = pd.DataFrame()

    if verification == True:
        for state_abbr in us_abbr_list:
            print(state_abbr)
            state_pharm_latlon_df = get_supp_pharmacy_latlon(state_abbr,"",verification, key)
            national_pharm_latlon_data = national_pharm_latlon_data.append(state_pharm_latlon_df)
        return national_pharm_latlon_data
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ')
        
def get_national_pharmacy_tracts(us_abbr_list: list, verification: bool = False, key: str = 'WaPo'):
    '''(string) -> pd.df
        Returns all pharmacy census tracts from all states (Will be large and could take extra time to load) 

        >>>get_national_pharmacy_latlon(verification = True)
            EXAMPLE OUTPUT
    '''
    national_pharm_tracts_df = pd.DataFrame()

    if verification == True:
        for state_abbr in us_abbr_list:
            print(state_abbr)
            state_pharm_tracts_df = get_supp_pharmacy_tracts(state_abbr,'', verification, key)
            national_pharm_tracts_df = national_pharm_tracts_df.append(state_pharm_tracts_df)
        return national_pharm_tracts_df
    else:
        print('Problem encountered, not returning data:')
        print('Either verification == False')
        print('Or problem with API encountered, please verify URL, state and county are correct: ')
        
        
def national_data_with_geo(us_abbr_list, verification = False, key: str = 'WaPo'):
    '''(string) -> geopandas.gdf
        Returns all pharmacy data and latlon geometry (Will be large and could take extra time to load) 

        >>>get_national_pharmacy_latlon(verification = True)
            EXAMPLE OUTPUT
    '''
    if verification == True:
        national_data = get_national_pharmacy_data(us_abbr_list, verification, key)

        national_pharm_latlon = get_national_pharmacy_latlon(us_abbr_list, "", verification, key)
        national_pharm_latlon = national_pharm_latlon.rename(str.lower, axis='columns') #match case of other df

        national_pharm_tracts = get_national_pharmacy_tracts(us_abbr_list, verification, key)
        national_pharm_tracts = national_pharm_tracts.rename(str.lower, axis='columns') #match case of other df

        national_pharm_locations = gpd.GeoDataFrame(national_pharm_latlon, geometry = gpd.points_from_xy(
            national_pharm_latlon.lon, national_pharm_latlon.lat))

        national_pharmacies = pd.merge(national_pharm_locations, national_data, how='left', on='buyer_dea_no')
        national_pharmacies = pd.merge(national_pharmacies, national_pharm_tracts, how='left', on='buyer_dea_no')
        
        total_national_dosage = national_pharmacies.total_dosage_unit.to_list()
        total_dosage = [float(i) for i in total_national_dosage]
        national_pharmacies['total_dosage'] = np.array(total_dosage)

        return national_pharmacies
    elif verification == False:
        print("Please verify this operation as it might take a long time to complete")