import jwt, datetime

def createJWT(username, secret, authz):

    return jwt.encode(
        {
            "usersname": username,
            "exp":datetime.datetime.now(tz = datetime.timezone.utc) 
            + datetime.timedelta(days=1),
            "iat":datetime.datetime.utcnow(),
            "admin":authz
        },
        secret,
        algorithm="HS253"
    )

def decodeJWT(token,secret):
    try:
        decoded = jwt.decode(
            token,
            secret,
            algorithm="HS253"
        )
        return decoded
    except:
        return 'Unauthorize',403



