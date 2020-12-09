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
        response = self._session.get_resource('account')
        response.raise_for_status()
        return response.json()

    def get_users(self) -> Dict:
        response = self._session.get_resource('account/users')
        response.raise_for_status()
        return response.json()

    def get_all_servers(self, page_number: int = 1):
        response = self._session.get_resource('server/list/all', params={
            'p': page_number
        })
        response.raise_for_status()
        return response.json()

    def get_active_servers(self, page_number: int = 1):
        response = self._session.get_resource('server/list', params={
            'p': page_number
        })
        response.raise_for_status()
        return response.json()

    def get_plans(self, page_number: int = 1):
        response = self._session.get_resource('server/create')
        response.raise_for_status()
        return response.json()

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

        response = self._session.get_resource('server/create/config', params=params)
        response.raise_for_status()
        return response.json()

    def get_server(self, server_name: str):
        response = self._session.get_resource(f"server/manage/{server_name}/show")
        response.raise_for_status()
        return response.json()

    def set_power(self, server_name: str, action: PowerAction):
        response = self._session.get_resource(f"server/manage/{server_name}/power", params={
            'set': action.value
        })
        response.raise_for_status()
        return response.json()

    def get_ips(self, server_name: str):
        response = self._session.get_resource(f"server/manage/{server_name}/ip/list")
        response.raise_for_status()
        return response.json()

    def get_ip_logs(self, server_name: str):
        response = self._session.get_resource(f"server/manage/{server_name}/ip/logs")
        response.raise_for_status()
        return response.json()

    def get_ip_rdns(self, server_name: str, ip: str, rdns: str):
        response = self._session.get_resource(f"server/manage/{server_name}/ip/rdns", params={
            'ip': ip,
            'rdns': rdns
        })
        response.raise_for_status()
        return response.json()

    def get_snapshots(self, server_name: str):
        response = self._session.get_resource(f"server/manage/{server_name}/snapshot")
        response.raise_for_status()
        return response.json()

    def create_snapshot(self, server_name: str):
        response = self._session.get_resource(f"server/manage/{server_name}/snapshot/create")
        response.raise_for_status()
        return response.json()

    def restore_snapshot(self, server_name: str, snapshot_name: str):
        response = self._session.get_resource(f"server/manage/{server_name}/snapshot/revert", params={
            'name': snapshot_name
        })
        response.raise_for_status()
        return response.json()

    def update_snapshot(self, server_name: str, snapshot_name: str):
        response = self._session.get_resource(f"server/manage/{server_name}/snapshot/update", params={
            'name': snapshot_name
        })
        response.raise_for_status()
        return response.json()

    def delete_snapshot(self, server_name: str, snapshot_name: str):
        response = self._session.get_resource(f"server/manage/{server_name}/snapshot/delete", params={
            'name': snapshot_name
        })
        response.raise_for_status()
        return response.json()

    def set_cron(self, server_name: str, cron_name: str, day: int, hour: int, min: int):
        response = self._session.get_resource(f"server/manage/{server_name}/snapshot/cron/add", params={
            'name': cron_name,
            'day': day,
            'hour': hour,
            'min': min
        })
        response.raise_for_status()
        return response.json()

    def delete_cron(self, server_name: str, cron_name: str):
        response = self._session.get_resource(f"server/manage/{server_name}/snapshot/cron/delete", params={
            'name': cron_name
        })
        response.raise_for_status()
        return response.json()

    def get_backups(self, server_name: str):
        response = self._session.get_resource(f"server/manage/{server_name}/backup")
        response.raise_for_status()
        return response.json()

    def restore_backup(self, server_name: str, backup_name: str):
        response = self._session.get_resource(f"server/manage/{server_name}/backup/restore", params={
            'backup_name': backup_name
        })
        response.raise_for_status()
        return response.json()

    def get_domains(self, p: int = 1):
        response = self._session.get_resource("domain/list", params={
            'p': p
        })
        response.raise_for_status()
        return response.json()

    def create_domain(self, domain: str, server: str, ipv6: bool):
        response = self._session.get_resource("domain/create", params={
            'domain': domain,
            'server': server,
            'ipv6': ipv6
        })
        response.raise_for_status()
        return response.json()

    def get_domain(self, domain_name: str):
        response = self._session.get_resource(f"domain/manage/{domain_name}/show")
        response.raise_for_status()
        return response.json()

    def add_dns_record(self, domain_name: str, record_name: str, record_type: DNSRecordType, record_content: str,
                       record_priority: int):
        response = self._session.get_resource(f"domain/manage/{domain_name}/add", params={
            'record_name': record_name,
            'record_type': record_type.value,
            'record_content': record_content,
            'record_priority': record_priority
        })
        response.raise_for_status()
        return response.json()

    def update_dns_record(self, domain_name: str, record_id: int, record_content: str, record_priority: int):
        response = self._session.get_resource(f"domain/manage/{domain_name}/update", params={
            'record_id': record_id,
            'record_content': record_content,
            'record_priority': record_priority
        })
        response.raise_for_status()
        return response.json()

    def delete_dns_record(self, domain_name: str, record_id: int):
        response = self._session.get_resource(f"domain/manage/{domain_name}/delete", params={
            'record_id': record_id
        })
        response.raise_for_status()
        return response.json()

    def dns_push(self, domain_name: str):
        response = self._session.get_resource(f"domain/manage/{domain_name}/push")
        response.raise_for_status()
        return response.json()
