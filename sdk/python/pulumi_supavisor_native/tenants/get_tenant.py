# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload, Awaitable
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities
from . import outputs

__all__ = [
    'Tenant',
    'AwaitableTenant',
    'get_tenant',
    'get_tenant_output',
]

@pulumi.output_type
class Tenant:
    def __init__(__self__, auth_query=None, db_database=None, db_host=None, db_port=None, enforce_ssl=None, external_id=None, id=None, inserted_at=None, ip_version=None, require_user=None, sni_hostname=None, updated_at=None, upstream_ssl=None, upstream_verify=None, users=None):
        if auth_query and not isinstance(auth_query, str):
            raise TypeError("Expected argument 'auth_query' to be a str")
        pulumi.set(__self__, "auth_query", auth_query)
        if db_database and not isinstance(db_database, str):
            raise TypeError("Expected argument 'db_database' to be a str")
        pulumi.set(__self__, "db_database", db_database)
        if db_host and not isinstance(db_host, str):
            raise TypeError("Expected argument 'db_host' to be a str")
        pulumi.set(__self__, "db_host", db_host)
        if db_port and not isinstance(db_port, int):
            raise TypeError("Expected argument 'db_port' to be a int")
        pulumi.set(__self__, "db_port", db_port)
        if enforce_ssl and not isinstance(enforce_ssl, bool):
            raise TypeError("Expected argument 'enforce_ssl' to be a bool")
        pulumi.set(__self__, "enforce_ssl", enforce_ssl)
        if external_id and not isinstance(external_id, str):
            raise TypeError("Expected argument 'external_id' to be a str")
        pulumi.set(__self__, "external_id", external_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if inserted_at and not isinstance(inserted_at, str):
            raise TypeError("Expected argument 'inserted_at' to be a str")
        pulumi.set(__self__, "inserted_at", inserted_at)
        if ip_version and not isinstance(ip_version, str):
            raise TypeError("Expected argument 'ip_version' to be a str")
        pulumi.set(__self__, "ip_version", ip_version)
        if require_user and not isinstance(require_user, bool):
            raise TypeError("Expected argument 'require_user' to be a bool")
        pulumi.set(__self__, "require_user", require_user)
        if sni_hostname and not isinstance(sni_hostname, str):
            raise TypeError("Expected argument 'sni_hostname' to be a str")
        pulumi.set(__self__, "sni_hostname", sni_hostname)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)
        if upstream_ssl and not isinstance(upstream_ssl, bool):
            raise TypeError("Expected argument 'upstream_ssl' to be a bool")
        pulumi.set(__self__, "upstream_ssl", upstream_ssl)
        if upstream_verify and not isinstance(upstream_verify, str):
            raise TypeError("Expected argument 'upstream_verify' to be a str")
        pulumi.set(__self__, "upstream_verify", upstream_verify)
        if users and not isinstance(users, list):
            raise TypeError("Expected argument 'users' to be a list")
        pulumi.set(__self__, "users", users)

    @property
    @pulumi.getter(name="authQuery")
    def auth_query(self) -> Optional[str]:
        """
        SELECT rolname, rolpassword FROM pg_authid WHERE rolname=$1
        """
        return pulumi.get(self, "auth_query")

    @property
    @pulumi.getter(name="dbDatabase")
    def db_database(self) -> str:
        """
        Database name
        """
        return pulumi.get(self, "db_database")

    @property
    @pulumi.getter(name="dbHost")
    def db_host(self) -> str:
        """
        Database host
        """
        return pulumi.get(self, "db_host")

    @property
    @pulumi.getter(name="dbPort")
    def db_port(self) -> int:
        """
        Database port
        """
        return pulumi.get(self, "db_port")

    @property
    @pulumi.getter(name="enforceSsl")
    def enforce_ssl(self) -> Optional[bool]:
        return pulumi.get(self, "enforce_ssl")

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[str]:
        """
        External ID
        """
        return pulumi.get(self, "external_id")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="insertedAt")
    def inserted_at(self) -> Optional[str]:
        return pulumi.get(self, "inserted_at")

    @property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> Optional[str]:
        """
        auto
        """
        return pulumi.get(self, "ip_version")

    @property
    @pulumi.getter(name="requireUser")
    def require_user(self) -> Optional[bool]:
        return pulumi.get(self, "require_user")

    @property
    @pulumi.getter(name="sniHostname")
    def sni_hostname(self) -> Optional[str]:
        """
        your.domain.com
        """
        return pulumi.get(self, "sni_hostname")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[str]:
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="upstreamSsl")
    def upstream_ssl(self) -> Optional[bool]:
        return pulumi.get(self, "upstream_ssl")

    @property
    @pulumi.getter(name="upstreamVerify")
    def upstream_verify(self) -> Optional[str]:
        """
        none
        """
        return pulumi.get(self, "upstream_verify")

    @property
    @pulumi.getter
    def users(self) -> Sequence['outputs.User']:
        return pulumi.get(self, "users")


class AwaitableTenant(Tenant):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return Tenant(
            auth_query=self.auth_query,
            db_database=self.db_database,
            db_host=self.db_host,
            db_port=self.db_port,
            enforce_ssl=self.enforce_ssl,
            external_id=self.external_id,
            id=self.id,
            inserted_at=self.inserted_at,
            ip_version=self.ip_version,
            require_user=self.require_user,
            sni_hostname=self.sni_hostname,
            updated_at=self.updated_at,
            upstream_ssl=self.upstream_ssl,
            upstream_verify=self.upstream_verify,
            users=self.users)


def get_tenant(external_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableTenant:
    """
    Use this data source to access information about an existing resource.

    :param str external_id: External ID of the tenant
    """
    __args__ = dict()
    __args__['externalId'] = external_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('supavisor-native:tenants:getTenant', __args__, opts=opts, typ=Tenant).value

    return AwaitableTenant(
        auth_query=pulumi.get(__ret__, 'auth_query'),
        db_database=pulumi.get(__ret__, 'db_database'),
        db_host=pulumi.get(__ret__, 'db_host'),
        db_port=pulumi.get(__ret__, 'db_port'),
        enforce_ssl=pulumi.get(__ret__, 'enforce_ssl'),
        external_id=pulumi.get(__ret__, 'external_id'),
        id=pulumi.get(__ret__, 'id'),
        inserted_at=pulumi.get(__ret__, 'inserted_at'),
        ip_version=pulumi.get(__ret__, 'ip_version'),
        require_user=pulumi.get(__ret__, 'require_user'),
        sni_hostname=pulumi.get(__ret__, 'sni_hostname'),
        updated_at=pulumi.get(__ret__, 'updated_at'),
        upstream_ssl=pulumi.get(__ret__, 'upstream_ssl'),
        upstream_verify=pulumi.get(__ret__, 'upstream_verify'),
        users=pulumi.get(__ret__, 'users'))
def get_tenant_output(external_id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[Tenant]:
    """
    Use this data source to access information about an existing resource.

    :param str external_id: External ID of the tenant
    """
    __args__ = dict()
    __args__['externalId'] = external_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('supavisor-native:tenants:getTenant', __args__, opts=opts, typ=Tenant)
    return __ret__.apply(lambda __response__: Tenant(
        auth_query=pulumi.get(__response__, 'auth_query'),
        db_database=pulumi.get(__response__, 'db_database'),
        db_host=pulumi.get(__response__, 'db_host'),
        db_port=pulumi.get(__response__, 'db_port'),
        enforce_ssl=pulumi.get(__response__, 'enforce_ssl'),
        external_id=pulumi.get(__response__, 'external_id'),
        id=pulumi.get(__response__, 'id'),
        inserted_at=pulumi.get(__response__, 'inserted_at'),
        ip_version=pulumi.get(__response__, 'ip_version'),
        require_user=pulumi.get(__response__, 'require_user'),
        sni_hostname=pulumi.get(__response__, 'sni_hostname'),
        updated_at=pulumi.get(__response__, 'updated_at'),
        upstream_ssl=pulumi.get(__response__, 'upstream_ssl'),
        upstream_verify=pulumi.get(__response__, 'upstream_verify'),
        users=pulumi.get(__response__, 'users')))
