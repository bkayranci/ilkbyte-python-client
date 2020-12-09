import logging
import os
from typing import Dict
from ilkbyte.exception import ConfigurationError
from ilkbyte.session import IlkbyteAPISession
from ilkbyte.utils import PowerAction, DNSRecordType

logger = logging.getLogger(__name__)


class Ilkbyte(object):

    def __init__(self, host: str = None, secret_key: str = None, access_key: str = None):
        """
        Ilkbyte API client.
        Args:
            host (str): Hostname of the ilkbyte api.
            secret_key (str): Secret key.
            access_key (str): Access key.
        """

        if not host:
            host = os.getenv('ILKBYTE_HOST')
            if not host:
                logger.error("hostname variable or ILKBYTE_HOST environment variable is required!")
                raise ConfigurationError()

        if not secret_key:
            secret_key = os.getenv('ILKBYTE_SECRET_KEY')
            if not secret_key:
                logger.error("secret_key variable or ILKBYTE_SECRET_KEY environment variable is required!")
                raise ConfigurationError()

        if not access_key:
            access_key = os.getenv('ILKBYTE_ACCESS_KEY')
            if not access_key:
                logger.error("access_key variable or ILKBYTE_ACCESS_KEY environment variable is required!")
                raise ConfigurationError()

        self._session = IlkbyteAPISession(host, secret_key, access_key)

    def get_account(self) -> Dict:
        return self._session.get_resource('account').json()

    def get_users(self) -> Dict:
        return self._session.get_resource('account/users')

    def get_all_servers(self, page_number: int = 1):
        return self._session.get_resource('server/list/all', params={
            'p': page_number
        })

    def get_active_servers(self, page_number: int = 1):
        return self._session.get_resource('server/list', params={
            'p': page_number
        })

    def get_plans(self, page_number: int = 1):
        return self._session.get_resource('server/create')

    def create_server(self, username, name, os_id, app_id, package_id, sshkey, password=None):
        params = {
            'username': username,
            'name': name,
            'os_id': os_id,
            'app_id': app_id,
            'package_id': package_id,
            'sshkey': sshkey,
        }
        if not password:
            params['password'] = password

        return self._session.get_resource('server/create/config', params=params)

    def get_server(self, server_name: str):
        return self._session.get_resource(f"server/manage/{server_name}/show")

    def set_power(self, server_name: str, action: PowerAction):
        return self._session.get_resource(f"server/manage/{server_name}/power", params={
            'set': action.value
        })

    def get_ips(self, server_name: str):
        return self._session.get_resource(f"server/manage/{server_name}/ip/list")

    def get_ip_logs(self, server_name: str):
        return self._session.get_resource(f"server/manage/{server_name}/ip/logs")

    def get_ip_rdns(self, server_name: str, ip: str, rdns: str):
        return self._session.get_resource(f"server/manage/{server_name}/ip/rdns", params={
            'ip': ip,
            'rdns': rdns
        })

    def get_snapshots(self, server_name: str):
        return self._session.get_resource(f"server/manage/{server_name}/snapshot")

    def create_snapshot(self, server_name: str):
        return self._session.get_resource(f"server/manage/{server_name}/snapshot/create")

    def restore_snapshot(self, server_name: str, snapshot_name: str):
        return self._session.get_resource(f"server/manage/{server_name}/snapshot/revert", params={
            'name': snapshot_name
        })

    def update_snapshot(self, server_name: str, snapshot_name: str):
        return self._session.get_resource(f"server/manage/{server_name}/snapshot/update", params={
            'name': snapshot_name
        })

    def delete_snapshot(self, server_name: str, snapshot_name: str):
        return self._session.get_resource(f"server/manage/{server_name}/snapshot/delete", params={
            'name': snapshot_name
        })

    def set_cron(self, server_name: str, cron_name: str, day: int, hour: int, min: int):
        return self._session.get_resource(f"server/manage/{server_name}/snapshot/cron/add", params={
            'name': cron_name,
            'day': day,
            'hour': hour,
            'min': min
        })

    def delete_cron(self, server_name: str, cron_name: str):
        return self._session.get_resource(f"server/manage/{server_name}/snapshot/cron/delete", params={
            'name': cron_name
        })

    def get_backups(self, server_name: str):
        return self._session.get_resource(f"server/manage/{server_name}/backup")

    def restore_backup(self, server_name: str, backup_name: str):
        return self._session.get_resource(f"server/manage/{server_name}/backup/restore", params={
            'backup_name': backup_name
        })

    def get_domains(self, p: int = 1):
        return self._session.get_resource("domain/list", params={
            'p': p
        })

    def create_domain(self, domain: str, server: str, ipv6: bool):
        return self._session.get_resource("domain/create", params={
            'domain': domain,
            'server': server,
            'ipv6': ipv6
        })

    def get_domain(self, domain_name: str):
        return self._session.get_resource(f"domain/manage/{domain_name}/show")

    def add_dns_record(self, domain_name: str, record_name: str, record_type: DNSRecordType, record_content: str,
                       record_priority: int):
        return self._session.get_resource(f"domain/manage/{domain_name}/add", params={
            'record_name': record_name,
            'record_type': record_type.value,
            'record_content': record_content,
            'record_priority': record_priority
        })

    def update_dns_record(self, domain_name: str, record_id: int, record_content: str, record_priority: int):
        return self._session.get_resource(f"domain/manage/{domain_name}/update", params={
            'record_id': record_id,
            'record_content': record_content,
            'record_priority': record_priority
        })

    def delete_dns_record(self, domain_name: str, record_id: int):
        return self._session.get_resource(f"domain/manage/{domain_name}/delete", params={
            'record_id': record_id
        })

    def dns_push(self, domain_name: str):
        return self._session.get_resource(f"domain/manage/{domain_name}/push")
