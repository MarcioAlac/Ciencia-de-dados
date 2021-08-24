import requests
import json 

def getCreds():
    creds = dict()
    creds['access_token'] ='EAALxQPbRkCoBABxrTN1hZBHqms3nGawnEmUFvv8eJN8QBpKsKfcW6TIXqfI4DEJPxSFZB4fNnnlmcZAxT2HFRwBxQTYpNq5UoNFmY4Evp7krlAG9bTzpPpxwfU7VI1WHQKZBrMUiUcXepxskQXL7rk8mrtQPC1sQQZAGkCZBfNAOv6mO6be4r9rF411gjTbkkZD'
    creds['client_id'] = '828211274551338'
    creds['client_secret'] = '5d1f8782732476667c42d5e811c62a92'
    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v11.0'
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'
    creds['debug'] = 'no'
    return creds 

def makeApiCall( url, endpointParams, debug = 'no' ):
    data = requests.get( url, endpointParams)
    response = dict()
    response['url'] = url
    response['endpoint_params'] = endpointParams
    response['endpoint_params_pretty'] = json.dumps( endpointParams, indent = 2 )
    response['json_data'] = json.loads( data.content )
    response['json_data_pretty'] = json.dumps( response['json_data'], indent= 2 )
    
    if( 'yes' == debug ):
        displayApiCallData( response )
    return response

def displayApiCallData( response ):
    print( f"\nURL: {response['url']}" )
    print( f"\nEndpoint Params: {response['endpoint_params_pretty']}")
    print(f"\nResponse: {response['json_data_pretty']}")
    
    
    