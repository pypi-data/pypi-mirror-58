# coding: utf-8

from.grant import Grant


class GrantPassword(Grant):
    def __init__(self, *args, **kwargs):
        super(GrantPassword, self).__init__(*args, **kwargs)
        if len(args) == 2:
            self._password = args[1]
        elif kwargs.get("password"):
            self._password = kwargs.get("password")
        if len(args) == 3:
            self._token_scope = args[2]
        elif kwargs.get("token_scope", "trapi"):
            self._token_scope = kwargs.get("token_scope", "trapi")

    def get_password(self):
        return self._password

    def password(self, value):
        self._password = value
        return self

    def get_token_scope(self):
        return self._token_scope

    def with_scope(self, token_scope):
        if token_scope:
            self._token_scope = token_scope
        return self

