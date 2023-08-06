"""
Defines useful types in this library.
"""
from base64 import b64encode
from enum import Enum
from time import time
from typing import Any, Dict, Optional, cast

import requests
from jinja2 import Environment

from ..errors import UnreachableError


class AuthorizationType(Enum):
    """
    Enum class defines the supported authorization methods
    in this library.

    Bearer: requires 'access_token' presented in user params
    OAuth2: requires 'client_id' and 'client_secret' in user params
            for 'ClientCredentials' grant type
    """

    Bearer = "Bearer"
    OAuth2 = "OAuth2"


class Authorization:
    """
    Class carries the authorization type and
    the corresponding parameter.
    """

    auth_type: AuthorizationType
    params: Dict[str, str]
    storage: Dict[str, Any]

    def __init__(self, auth_type: AuthorizationType, params: Dict[str, str]) -> None:
        self.auth_type = auth_type
        self.params = params
        self.storage = {}

    def build(self, req_data: Dict[str, Any], params: Dict[str, Any]) -> None:
        """
        Populate some required fields to the request data.
        Complex logic may also happens in this function (e.g. start a server to do OAuth).
        """
        if self.auth_type == AuthorizationType.Bearer:  # pylint: disable=no-member
            req_data["headers"]["Authorization"] = f"Bearer {params['access_token']}"
        elif (
            self.auth_type == AuthorizationType.OAuth2
            and self.params["grantType"] == "ClientCredentials"
        ):
            # TODO: Move OAuth to a separate authenticator
            if (
                "access_token" not in self.storage
                or self.storage.get("expires_at", 0) < time()
            ):
                # Not yet authorized
                ckey = params["client_id"]
                csecret = params["client_secret"]
                b64cred = b64encode(f"{ckey}:{csecret}".encode("ascii")).decode()
                resp = requests.post(
                    self.params["tokenServerUrl"],
                    headers={"Authorization": f"Basic {b64cred}"},
                    data={"grant_type": "client_credentials"},
                ).json()

                assert resp["token_type"].lower() == "bearer"
                access_token = resp["access_token"]
                self.storage["access_token"] = access_token
                if "expires_in" in resp:
                    self.storage["expires_at"] = (
                        time() + resp["expires_in"] - 60
                    )  # 60 seconds grace period to avoid clock lag

            req_data["headers"][
                "Authorization"
            ] = f"Bearer {self.storage['access_token']}"

            # TODO: handle auto refresh
        elif (
            self.auth_type == AuthorizationType.OAuth2
            and self.params["grantType"] == "AuthorizationCode"
        ):
            raise NotImplementedError


class Fields:
    """
    A data structure that stores the fields information (e.g. headers, cookies, ...).
    This class is useful to populate concrete fields data with required variables provided.
    """

    fields: Dict[str, Any]

    def __init__(self, fields_config: Dict[str, Any]) -> None:
        self.fields = fields_config

    def populate(self, jenv: Environment, params: Dict[str, Any]) -> Dict[str, str]:
        """
        Populate a dict based on the fields definition and provided vars.
        """
        ret = {}

        for key, def_ in self.fields.items():
            if isinstance(def_, bool):
                required = def_
                value = params.get(key)
                if value is None and required:
                    raise KeyError(key)
                remove_if_empty = False
            elif isinstance(def_, str):
                # is a template
                template: Optional[str] = def_
                expr = jenv.compile_expression(cast(str, template))
                value = expr(**params)
                remove_if_empty = False
            elif isinstance(def_, dict):
                template = def_.get("template")
                remove_if_empty = def_["removeIfEmpty"]

                if template is None:
                    required = def_["required"]
                    true_key = def_.get("valueFrom") or key
                    value = params.get(true_key)
                    if value is None and required:
                        raise KeyError(key)
                else:
                    expr = jenv.compile_expression(template)
                    value = expr(**params)
            else:
                raise UnreachableError()

            if value is not None:
                str_value = str(value)

                if not (remove_if_empty and not str_value):
                    ret[key] = str_value
                    continue

        return ret


class Orient(Enum):
    """
    Different types of table orientations
    ref: (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html).
    Currently, DataConnector supports two different types of orientaions:
        1. Split, which is column store.
        2. Records, which is row store.
    Details can be found in the pandas page.
    """

    Split = "split"
    Records = "records"
