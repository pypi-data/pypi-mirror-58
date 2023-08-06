# coding:utf8

from fastweb.compat import urlencode
from fastweb.accesspoint import HTTPRequest, HTTPError, UsernameToken


DEFAULT_TIMEOUT = 5
DEFAULT_RETRY_TIME = 3

__all__ = ['UsernameToken', 'Request', 'SoapRequest', 'HTTPError']


class Request(HTTPRequest):
    """Http请求对象"""

    def __init__(self, url, method="GET", headers=None, body=None,
                 auth_username=None, auth_password=None, auth_mode=None,
                 connect_timeout=DEFAULT_TIMEOUT, request_timeout=DEFAULT_TIMEOUT,
                 if_modified_since=None, follow_redirects=None,
                 max_redirects=None, user_agent=None, use_gzip=None,
                 network_interface=None, streaming_callback=None,
                 header_callback=None, prepare_curl_callback=None,
                 proxy_host=None, proxy_port=None, proxy_username=None,
                 proxy_password=None, allow_nonstandard_methods=None,
                 validate_cert=None, ca_certs=None,
                 allow_ipv6=None,
                 client_key=None, client_cert=None, body_producer=None,
                 expect_100_continue=False, decompress_response=None,
                 ssl_options=None, params=None, retry=DEFAULT_RETRY_TIME, json=None):
        if params:
            url = '{url}?{params}'.format(url=url, params=urlencode(params))
        if body:
            body = urlencode(body)
        self.json = json
        self.retry = retry
        super(Request, self).__init__(url, method=method, headers=headers, body=body,
                                      auth_username=auth_username, auth_password=auth_password, auth_mode=auth_mode,
                                      connect_timeout=connect_timeout, request_timeout=request_timeout,
                                      if_modified_since=if_modified_since, follow_redirects=follow_redirects,
                                      max_redirects=max_redirects, user_agent=user_agent, use_gzip=use_gzip,
                                      network_interface=network_interface, streaming_callback=streaming_callback,
                                      header_callback=header_callback, prepare_curl_callback=prepare_curl_callback,
                                      proxy_host=proxy_host, proxy_port=proxy_port, proxy_username=proxy_username,
                                      proxy_password=proxy_password, allow_nonstandard_methods=allow_nonstandard_methods,
                                      validate_cert=validate_cert, ca_certs=ca_certs,
                                      allow_ipv6=allow_ipv6,
                                      client_key=client_key, client_cert=client_cert, body_producer=body_producer,
                                      expect_100_continue=expect_100_continue, decompress_response=decompress_response,
                                      ssl_options=ssl_options)

    def __str__(self):
        return '<Request {method} {url}>'.format(method=self.method, url=self.url)


class SoapRequest(object):
    """Soap 请求对象"""

    def __init__(self, wsdl, function, wsse=None, retry=DEFAULT_RETRY_TIME, timeout=DEFAULT_TIMEOUT, **kwargs):
        self.wsdl = wsdl
        self.function = function
        self.wsse = wsse
        self.kwargs = kwargs
        self.retry = retry
        self.timeout = timeout

    def __str__(self):
        return '<SoapRequest {wsdl} {function} {kwargs}>'.format(wsdl=self.wsdl, function=self.function,
                                                                 kwargs=self.kwargs)
