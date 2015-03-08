import json, urllib, requests, sys, getopt
from requests.auth import HTTPBasicAuth

jsonheader = {'content-type': 'application/json'}

devServer = 'http://localhost/'
testServer = 'https://test.domain.com'
liveServer = 'https://domain.com'

defpath = '/path/to/service'

request = {
        "key1":"value",
        "key2":"value",
        "key3":"value",
        "key4":"value",
        "key5":"value",
}

def postReq(url, key, header, body):
    r = requests.post(url, headers=header, data=body)
    print("encoding = {}".format(r.encoding))
    return json.loads(json.dumps(r.text))

def main(argv):
    server = devServer
    path = defPath

    jsonBody = json.dumps(request)

    try:
        opts, args = getopt.getopt(argv,"s:p:d:h")

    except (getopt.GetoptError):
        sys.exit(2)

    for opt, arg in opts:
        if (opt == "-s"):
            if (arg == "live"):
                server = liveServer
            elif (arg == "test"):
                server = testServer
        elif (opt == '-p'):
                path = arg
        elif (opt == '-d'):
                jsonBody = arg
        elif (opt == '-h'):
            printHelp() 
            sys.exit(0)

    url = server + path

    print("connecting to {} \nwith data {}".format(url, jsonBody))
    resp = postReq(url, key, jsonheader, jsonBody)
    print(resp);

def printHelp():
    print 'ibvApiPost.py [-s [live|test]] [-p path] [-d json_data]'

if __name__ == "__main__":
    main(sys.argv[1:])
