A personal package.

#Initialization

dance = DanceGoogleAuth()
dance.init_app(app, 'index')
//OR
dance = DanceGoogleAuth(app, 'index')

#Set login_handler

def login_handler(email, name):
    session['user_email'] = email
    session['user_name'] = name
    return True
dance.set_login_handler(login_handler)

#Signin/out Route

dance.signin_url()
dance.signout_url()

#Decorator Requiring

@dance.login_required()
@dance.auth_required(lambda: session.get('user_email') == 'abc@gmail.com')

#Complete Protect

dance.all_login_required()
dance.all_auth_required(lambda: session.get('user_email') == 'abc@gmail.com')

#Required Env

GOOGLE_OAUTH_CLIENT_ID
GOOGLE_OAUTH_CLIENT_SECRET