# -*- coding: utf-8 -*-

"""Python sina weibo sdk.

Notice:

   The base client is copied from http://lxyu.github.io/weibo/,
   I just pack some methods in order to make my use more convenient

.........

    Rely on `requests` to do the dirty work, so it's much simpler and cleaner
    than the official SDK.

    For more info, refer to:
    http://lxyu.github.io/weibo/

.........

  Haibo Wang   2019.12

"""

from __future__ import absolute_import

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

import json
import time

import requests


class Client(object):

    GET_ALL_WEIBO_LIST = "home_timeline"
    GET_MY_WEIBO_LIST = "user_timeline"
    GET_ONE_WEIBO = "show"


    GET_COMMENT_LIST = "show"
    GET_COMMENTS_BY_ME = "by_me"
    GET_COMMENTS_TO_ME = "to_me"
    GET_ALL_COMMENTS_LIST = "timeline"
    GET_ALL_METIONME_COMMENTS = "mentions"
    GET_COMMENTS_CONENTS = "show_batch"


    POST_PUB_WEIBO = "share"
    POST_PUB_COMMENT = "create"
    POST_DEL_COMMENT = "destroy"
    POST_REPLY_COMMENT = "reply"



    def __init__(self, api_key, api_secret, redirect_uri, token=None,
                 username=None, password=None):
        # const define
        self.site = 'https://api.weibo.com/'
        self.authorization_url = self.site + 'oauth2/authorize'
        self.token_url = self.site + 'oauth2/access_token'
        self.api_url = self.site + '2/'

        # init basic info
        self.client_id = api_key
        self.client_secret = api_secret
        self.redirect_uri = redirect_uri

        self.session = requests.session()
        if username and password:
            self.session.auth = username, password

        # activate client directly if given token
        if token:
            self.set_token(token)

    @property
    def authorize_url(self):
        params = {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri
        }
        return "{0}?{1}".format(self.authorization_url, urlencode(params))

    @property
    def alive(self):
        if self.expires_at:
            return self.expires_at > time.time()
        else:
            return False

    def set_code(self, authorization_code):
        """Activate client by authorization_code.
        """
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'authorization_code',
            'code': authorization_code,
            'redirect_uri': self.redirect_uri
        }
        res = requests.post(self.token_url, data=params)
        token = json.loads(res.text)
        self._assert_error(token)

        token[u'expires_at'] = int(time.time()) + int(token.pop(u'expires_in'))
        self.set_token(token)

    def set_token(self, token):
        """Directly activate client by access_token.
        """
        self.token = token

        self.uid = token['uid']
        self.access_token = token['access_token']
        self.expires_at = token['expires_at']

        self.session.params = {'access_token': self.access_token}

    def _assert_error(self, d):
        """Assert if json response is error.
        """
        if 'error_code' in d and 'error' in d:
            raise RuntimeError("{0} {1}".format(
                d.get("error_code", ""), d.get("error", "")))

    def get(self, uri, **kwargs):
        """Request resource by get method.
        """
        url = "{0}{1}.json".format(self.api_url, uri)

        # for username/password client auth
        if self.session.auth:
            kwargs['source'] = self.client_id

        res = json.loads(self.session.get(url, params=kwargs).text)
        self._assert_error(res)
        return res

    def post(self, uri, **kwargs):
        """Request resource by post method.
        """
        url = "{0}{1}.json".format(self.api_url, uri)

        # for username/password client auth
        if self.session.auth:
            kwargs['source'] = self.client_id

        if "pic" not in kwargs:
            res = json.loads(self.session.post(url, data=kwargs).text)
        else:
            files = {"pic": kwargs.pop("pic")}
            res = json.loads(self.session.post(url,
                                               data=kwargs,
                                               files=files).text)
        self._assert_error(res)
        return res


    def baseRequest(self,category, method, **kwargs):
        uri = category + "/" + method
        if method.startswith("GET"):
            return self.get(uri, **kwargs)
        return self.post(uri, **kwargs)

    """
      weibo comment,such as get comment by weibo id,publish one comment,reply comment and so on.
      
    """
    def comment(self, method, **kwargs):
        return self.baseRequest("comment", method, **kwargs)

    """
      weibo methods,such as get weibo list,create weibo,get some weibo by id 
    
    """
    def statuses(self, method, **kwargs):
        return self.baseRequest("statuses", method, **kwargs)


