import tweepy

def connect_api():
    """
    connect_api 함수는 tweepy 로 API 를 연결한 'api' 객체를 리턴합니다.

    Hint: api 객체는 tweepy.API 로 만들 수 있습니다.
    """

    api_key = 'CGk6gHJsb4J8PGsbwZWJHbsab'
    api_key_secret = 'qcfdvfc60dFHBuQqOQIJxBqWhDo0a2sdc2dop0HkAzdoL0GsY2'
    access_token = '1557193091819646976-8HIGTFExoKHzmWelvg8jnuonN9bwuF'
    access_token_secret = '8zgW8zEuxGl9aMGJL0jGCEFggP3e80vbnJmb0LTomlF6K'

    api = None
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api


def get_tweets(api, username):
    """
    'username' 이 주어지면 해당 유저의 트윗들을 가지고 올 수 있어야 합니다.
    각 트윗은 140 자 이상이어도 모든 내용을 가지고 올 수 있어야 합니다.

    Hint: 'tweet_mode' 에 대해서 알아보세요!
    """

    tweets = None
    tweets = api.user_timeline(username, tweet_mode='extended')

    return tweets
