
from enum import Enum, unique
import subprocess
import platform
import sys
import restic.parser
from restic.core import version
from restic.config import restic_bin

from restic.snapshot import Snapshot
from restic.key import Key

@unique
class RepoKind(Enum):
    Local = 0
    SFTP = 1
    REST = 2
    S3 = 3
    Swift = 4
    B2 = 5
    Azure = 6
    GoogleStorage = 7
    Rclone = 8

class Repo(object):
    kind = None
    path = None
    password = None
    is_open = False
    fallback_output = False

    # global flags
    '''
    cacert = None
    cache_dir = None
    no_lock = False
    limit_download = None
    limit_upload = None
    options = {}
    quiet = False
    verbose = False
    '''

    snapshots_list = []
    def __init__(self, path, password, kind = RepoKind.Local):
        self.path = path
        self.kind = kind
        self.password = password
        self.is_open = False

        try:
            version()
        except Exception:
            print('restic is not in env or it has not been installed')

    def _run_command(self, cmd):
        out = ''
        err = ''
        try:
            with subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                encoding='utf-8',
                text=True) as proc:
                out, err = proc.communicate(self.password)
                if err is not None:
                    raise RuntimeError('Command runtime failure')
                proc.wait()
                if proc.returncode != 0:
                    raise RuntimeError(f'Return code {proc.returncode} is not zero')
        except FileNotFoundError:
            raise RuntimeError('Cannot find restic installed')
        
        if out.startswith('read password from stdin\n'):
            out = out[25:]

        return out

    def _build_command_internal(self):
        cmd = [restic_bin, '-r', self.path]
        return cmd

    def _build_command(self, cacert=None, cache_dir=None, no_lock=False, limit_download=None, limit_upload=None, quiet=False, verbose=False, json=False):
        cmd = [restic_bin, '-r', self.path]

        if cacert is not None:
            if type(self.cacert) == str:
                cmd.extend(['--cacert', self.cacert])
            else:
                raise ValueError('cacert shall be type of str or None')

        if cache_dir is not None:
            if type(self.cache_dir) == str:
                cmd.extend(['--cache-dir', self.cache_dir])
            else:
                raise ValueError('cache_dir shall be type of str or None')

        if no_lock:
            cmd.append('--no-lock')

        if limit_download is not None:
            if type(self.limit_download) == int:
                cmd.extend(['--limit-download', str(self.limit_download)])
            else:
                raise ValueError('limit_download shall be type of str or None')

        if limit_upload is not None:
            if type(self.limit_upload) == int:
                cmd.extend(['--limit-upload', str(self.limit_upload)])
            else:
                raise ValueError('limit_upload shall be type of str or None')

        if quiet:
            cmd.append('--quiet')

        if verbose:
            cmd.append('--verbose')

        if json:
            cmd.append('--json')
        return cmd


    @staticmethod
    def init(url, password, repo_kind = RepoKind.Local):
        if repo_kind not in [RepoKind.Local, RepoKind.SFTP, RepoKind.REST, RepoKind.S3]:
            raise NotImplementedError('This kind of repo is not implemented now.')
        
        # check url valid(TODO)
        repo = Repo(url, password, repo_kind)

        # create repo
        repo_url = None
        if repo_kind == RepoKind.Local:
            repo_url = url
        elif repo_kind == RepoKind.SFTP:
            repo_url = 'sftp:' + url
        elif repo_kind == RepoKind.REST:
            repo_url = 'rest:' + url
        elif repo_kind == RepoKind.S3:
            repo_url = 's3:' + url
        else:
            raise NotImplementedError('This kind of repo is not implemented now.')
        repo._run_command([restic_bin, 'init', '--repo', url])

        return repo

    def remove_all_snapshots_list(self):
        for each_snapshots in self.snapshots_list:
            each_snapshots.repo = None

        self.snapshots_list = None

    def update_snapshots_list(self):
        snapshots_list = self._run_snapshots_command()
        for each_snapshot in self.snapshots_list:
            if each_snapshot.snapshot_id not in [each.snapshot_id for each in snapshots_list]:
                each_snapshot.repo = None
                self.snapshots_list.remove(each_snapshot)

        for each_snapshot in snapshots_list:
            if each_snapshot.snapshot_id not in [each.snapshot_id for each in self.snapshots_list]:
                self.snapshots_list.append(each_snapshot)

    '''
    Internal command implement
    '''
    def _run_snapshots_command(self):
        if self.fallback_output:
            cmd = self._build_command()
            cmd.append('snapshots')

            ret = self._run_command(cmd)

            if ret is None:
                return

            return restic.parser.parse_snapshots_fallback(self, ret)
        else:
            cmd = self._build_command(json=True)
            cmd.append('snapshots')

            ret = self._run_command(cmd)

            if ret is None:
                return

            return restic.parser.parse_snapshots(self, ret)

    def _run_stats_command(self):
        if self.fallback_output:
            cmd = self._build_command()
            cmd.append('stats')

            ret = self._run_command(cmd)

            if ret is None:
                return

            return restic.parser.parse_stats_fallback(self, ret)
        else:
            cmd = self._build_command(json=True)
            cmd.append('stats')

            ret = self._run_command(cmd)

            if ret is None:
                return

            return restic.parser.parse_stats(self, ret)

    def _run_key_list_commond(self):
        if self.fallback_output:
            cmd = self._build_command()
            cmd.extend(['key', 'list'])

            ret = self._run_command(cmd)

            if ret is None:
                return

            return restic.parser.parse_key_fallback(self, ret)
        else:
            cmd = self._build_command(json=True)
            cmd.extend(['key', 'list'])

            ret = self._run_command(cmd)

            if ret is None:
                return

            return restic.parser.parse_key(self, ret)

    '''
    Public repository API
    '''
    def backup(self, file_path, exclude=None, tags=None):
        # check url valid(TODO)

        # run cmd
        cmd = self._build_command()
        cmd.extend(['backup', file_path])

        if exclude is not None and type(exclude) == list:
            exclude_cmd = '--exclude="'
            for i, each_file in enumerate(exclude):
                if i != 0:
                    exclude_cmd += ','
                exclude_cmd += each_file
            exclude_cmd += '"'
            cmd.append(exclude_cmd)

        if tags is not None:
            if type(tags) == str:
                cmd.extend(['--tag', tags])
            elif type(tags) == list:
                for each_tag in tags:
                    cmd.extend(['--tag', each_tag])
            else:
                raise ValueError('tags shall be type of str or list')

        self._run_command(cmd)

    def check(self, read_data=False):
        cmd = self._build_command()
        cmd.append('check')

        if read_data:
            cmd.append('--read-data')

        ret_text = self._run_command(cmd)

        if ret_text is None:
            return

        lines = ret_text.splitlines()
        has_errors = lines[-1].strip() != 'no errors were found'

        if has_errors:
            for each_line in lines:
                if each_line.startswith('error') or each_line.startswith('Fatal'):
                    print(each_line)

        return has_errors

    def mount(self, target, snapshot='latest'):
        if 'Linux' not in platform.system():
            raise RuntimeError('Mounting repositories via FUSE is not possible on OpenBSD, Solaris/illumos and Windows.')
        if type(snapshot) == Snapshot:
            snapshot = snapshot.snapshot_id
        elif type(snapshot) not in [str, Snapshot]:
            raise ValueError('snapshot shall be type of str or Snapshot')

        cmd = self._build_command()
        cmd.extend([snapshot, 'mount', target])

        self._run_command(cmd)

    def restore(self, target, snapshot='latest'):

        if type(snapshot) == Snapshot:
            snapshot = snapshot.snapshot_id
        elif type(snapshot) not in [str, Snapshot]:
            raise ValueError('snapshot shall be type of str or Snapshot')

        cmd = self._build_command()
        cmd.extend(['restore', snapshot, '--target', target])

        self._run_command(cmd)

    def snapshots(self):
        self.update_snapshots_list()
        return self.snapshots_list

    def stats(self):
        return self._run_stats_command()

    def tag(self, add_tags=None, remove_tags=None, set_tags=None, snapshot='latest'):
        if type(snapshot) == Snapshot:
            snapshot = snapshot.snapshot_id
        elif type(snapshot) not in [str, Snapshot]:
            raise ValueError('snapshot shall be type of str or Snapshot')

        cmd = self._build_command()
        cmd.append('tag')

        if add_tags is not None:
            if type(add_tags) == str:
                cmd.extend(['--add', add_tags])
            elif type(add_tags) == list:
                for each_tag in add_tags:
                    if ',' not in each_tag:
                        cmd.extend(['--add', each_tag])
                    else:
                        raise ValueError('the `,` charactor in tag may make PyRestic wrong')
            else:
                raise ValueError('add_tags shall be type of str or list')

        if remove_tags is not None:
            if type(remove_tags) == str:
                cmd.extend(['--remove', remove_tags])
            elif type(remove_tags) == list:
                for each_tag in remove_tags:
                    if ',' not in each_tag:
                        cmd.extend(['--remove', each_tag])
                    else:
                        raise ValueError('the `,` charactor in tag may make PyRestic wrong')
            else:
                raise ValueError('remove_tags shall be type of str or list')

        if set_tags is not None:
            if type(set_tags) == str:
                cmd.extend(['--set', set_tags])
            elif type(set_tags) == list:
                for each_tag in set_tags:
                    if ',' not in each_tag:
                        cmd.extend(['--set', each_tag])
                    else:
                        raise ValueError('the `,` charactor in tag may make PyRestic wrong')
            else:
                raise ValueError('set_tags shall be type of str or list')
        cmd.append(snapshot)
        self._run_command(cmd)



            


