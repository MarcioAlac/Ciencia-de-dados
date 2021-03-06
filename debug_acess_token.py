from defines import getCreds, makeApiCall
import datetime

def debugAcessToken( params ):
    endpointParams = dict()
    endpointParams['input_token'] = params['access_token']
    endpointParams['access_token'] = params['access_token']
    
    url = params['graph_domain'] + 'debug_token'
    
    return makeApiCall( url, endpointParams, params['debug'] )

params = getCreds()
params['debug'] = 'yes'
response = debugAcessToken( params )

validade = datetime.datetime.fromtimestamp( response['json_data']['data']['expires_at'])
print(f"\nToken expira em: {validade}")