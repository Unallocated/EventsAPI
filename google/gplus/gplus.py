import authenticate, json

user = 'me'
app = 'plusDomains'
version = 'v1'
scope = ['https://www.googleapis.com/auth/plus.me', 'https://www.googleapis.com/auth/plus.stream.write']
post = {
    'object' : {
        'originalContent' : 'Happy Monday! #caseofthemondays'
        },
    'access' : {
        'items' : [{
            'type' : 'domain'
            }],
        'domainRestricted': True
        }
    }

service = authenticate.authenticate(app, version, scope, sub='uas.events.tester@gmail.com')

def create_post():
    return service.activities().insert(userId = user, body = post).execute()
    
def create_comment():
    pass


if __name__ == '__main__':
    print(create_post())


