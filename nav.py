from defines import makeApiCall, getCreds

def search(creds):
    nome = dict()
    nome['Nome'] = creds['endpoint_base'] + 'me?fields=id,name'
    return print(f"meu nome é: {nome['Nome']}")
search()