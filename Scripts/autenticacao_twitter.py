import tweepy

# Substitua pelas suas chaves e tokens
consumer_key = "0jRj5furF7cQWhQbP45NauFvi"
consumer_secret = "YSsPrx23sNIMWGRvuPXtpCODrZTq2YK7WLBb1SF3rr1GJFJJWD"
access_token = "1905703903670468608-ObrIUx4csEDKGcdW1vzpMwdlDPZFCF"
access_token_secret = "DjSURJ6oeC9wRzuYp7pBEdDAmdnLsO8iGjJXog1CT9j0P"

try:
    # Autenticação usando OAuth 1.0a
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Criar um objeto API
    api = tweepy.API(auth)

    # Verificar a autenticação (pegar informações do seu perfil)
    user = api.verify_credentials()
    print(f"Autenticação bem-sucedida como @{user.screen_name}")

except tweepy.TweepyException as e:
    print(f"Erro de autenticação com o Twitter: {e}")
    print("Por favor, verifique suas chaves e tokens.")