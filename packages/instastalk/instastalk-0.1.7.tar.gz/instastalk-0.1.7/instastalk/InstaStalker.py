from instastalk.BaseStalker import BaseStalker
from instastalk.constants import (
    BASE_URL,
    LOGIN_REFERER,
    LOGIN_URL,
    LOGOUT_URL,
    STORIES_API_URL,
)
from datetime import (
    datetime,
)
import json


class InstaStalker(BaseStalker):
    def __init__(self, username: str, password: str):
        '''constructor'''
        super().__init__()
        self.username = username
        self.password = password  # might not be the best to save it

    def login(self):
        '''this login function should gain you access to private users and stories,
        certain headers or cookies should be stored here'''
        login_data = {
            'username': self.username,
            'password': self.password,
            'queryParams': {},
        }
        self.session.headers['referer'] = LOGIN_REFERER
        self.session.headers['origin'] = BASE_URL

        r = self.session.post(LOGIN_URL, data=login_data, allow_redirects=True)
        print(r.text)

    def logout(self):
        '''this logout function is pretty much useless'''
        pass

    def _download_user_stories(self, username: str, user_id: str):
        '''this should get all stories of users and download'''
        url = STORIES_API_URL.format(id=user_id)
        r2 = self.session.get(url)
        data = json.loads(r2.text)
        if len(data['data']['reels_media']) > 0:
            for i in data['data']['reels_media'][0]['items']:
                time_taken = i['taken_at_timestamp']
                time_taken = datetime.fromtimestamp(
                    time_taken).strftime('%Y-%m-%d--%H-%M-%S')

                if i['__typename'] == 'GraphStoryVideo':
                    resource_url = i['video_resources'][-1]['src']
                    filename = f'{resource_url}-stories.mp4'
                else:
                    resource_url = i['diplay_url']
                    filename = f'{resource_url}-stories.jpg'

                self._download_file(resource_url, filename)
