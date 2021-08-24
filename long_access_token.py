from debug_acess_token import debugAcessToken
from defines import getCreds, makeApiCall

def getAccessLongToken( params ):
    
    endpointParams = dict()
    endpointParams['grant_type'] = 'fb_exchange_token'
    endpointParams['client_id'] = params['client_id']
    endpointParams['client_secret'] = params['client_secret']
    endpointParams['fb_exchange_token'] = params['access_token']
    
    url = params['endpoint_base'] + 'oauth/access_token'
    
    return makeApiCall( url, endpointParams, params['debug'])
params = getCreds()
params['debug'] = 'yes'
response = getAccessLongToken( params ) 

print('\n ------Informaçoes de acesso do token----- ')
print(f"\nToken de acesso: {response['json_data']['access_token']}")