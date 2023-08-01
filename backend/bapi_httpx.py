from httpx import Client, Response
import json
from custom_cookies import MyCookies

# Read config
config = json.load(open('config.json', 'r'))

class BAPIRequest:
    def __init__(self, cookies:list[dict]=[]):
        self.client = Client(headers=config['base_headers'], http2=True)
        self.client._cookies = MyCookies()
        self.client.cookies.read_dict_list(cookies)
    
    def refresh_cookies(self) -> Response:
        """ Refresh cookies by accessing the index page """
        return self.client.get(config['apis']['index_url'])

    def get_cookies(self) -> list[dict]:
        return self.client.cookies.to_dict_list()
    
    def set_cookies(self, cookies:list[dict]=[]):
        self.client.cookies.clear()
        self.client.cookies.read_dict_list(cookies)

    def get_popular(self, pn:int=1, ps:int=20) -> Response:
        params = {
            'ps': ps,
            'pn': pn
        }
        return self.client.get(config['apis']['popular_api'], params=params)
    
    def get_reply_to_me(self, cursor:dict={}) -> Response:
        '''
        cursor = {
            id: int
            reply_time: int
        }
        '''
        params = {
            'platform': 'web',
            'build': 0,
            'mobi_app': 'web'
        }
        if 'id' in cursor:
            params.update(cursor)
        return self.client.get(config['apis']['reply_to_me_api'], params=params)

    def get_my_info(self) -> Response:
        return self.client.get(config['apis']['my_info_api'])
    
    def get_approval_to_me(self, cursor:dict={}) -> Response:
        '''
        cursor = {
            id: int
            like_time: int
        }
        '''
        params = {
            'platform': 'web',
            'build': 0,
            'mobi_app': 'web'
        }
        if 'id' in cursor:
            params.update(cursor)
        return self.client.get(config['apis']['approval_to_me_api'], params=params)
    
    def get_dynamic(self, cursor:dict={}, type='all', host_mid=None) -> Response:
        '''
        cursor = {
            page: int
            offset: int
        }
        '''
        params = {
            'timezone_offset': -480,
            'type': type,
            'features': 'itemOpusStyle'
        }
        if 'page' in cursor:
            params.update(cursor)
        if host_mid is not None:
            params['host_mid'] = host_mid
        #print(params)
        return self.client.get(config['apis']['dynamic_api'], params=params)

    def get_portal(self) -> Response:
        return self.client.get(config['apis']['portal_api'])


if __name__ == '__main__':
    pass