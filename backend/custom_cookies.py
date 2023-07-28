from httpx import Cookies
from http.cookiejar import Cookie

class MyCookies(Cookies):

    def make_cookie_from_dict(self, cookie_dict:dict) -> Cookie:
        # Read infomation from dict
        name = cookie_dict['name']
        value = cookie_dict['value']
        domain = cookie_dict['domain']
        path = cookie_dict['path']
        expires = cookie_dict.get('expirationDate')
        # Make kwargs for Cookiejar.set_cookie
        kwargs = {
                "version": 0,
                "name": name,
                "value": value,
                "port": None,
                "port_specified": False,
                "domain": domain,
                "domain_specified": bool(domain),
                "domain_initial_dot": domain.startswith("."),
                "path": path,
                "path_specified": bool(path),
                "secure": False,
                "expires": expires,
                "discard": True,
                "comment": None,
                "comment_url": None,
                "rest": {"HttpOnly": None},
                "rfc2109": False,
            }
        return Cookie(**kwargs)
    
    def read_dict_list(self, cookie_dict_list:list[dict]):
        for item in cookie_dict_list:
            cookie = self.make_cookie_from_dict(item)
            self.jar.set_cookie(cookie)
    
    def make_dict_from_cookie(self, cookie:Cookie) -> dict:
        cookie_dict = {
            'name': cookie.name,
            'value': cookie.value,
            'domain': cookie.domain,
            'path': cookie.path,
            'expirationDate': cookie.expires
        }
        return cookie_dict
    
    def to_dict_list(self) -> dict:
        dict_arr = []
        for cookie in self.jar:
            dict_arr.append(self.make_dict_from_cookie(cookie))
        return dict_arr