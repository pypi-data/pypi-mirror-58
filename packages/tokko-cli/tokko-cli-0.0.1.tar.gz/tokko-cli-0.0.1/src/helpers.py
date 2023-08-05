import json
import shutil
import logging
from subprocess import CalledProcessError

from .executors import Executor, cmd_command

logger = logging.getLogger(__name__)


def create_service_from_template(template, **settings) -> bool:
    print(f'''New service:
+ Template "{template}"
+ Settings:
  {json.dumps(settings, indent=4)}
    ''')
    return True


def django_service(**pre_settings) -> bool:
    pre_settings.update({
        'repo': ''
    })
    return create_service_from_template('django', **pre_settings)


def flask_service(**pre_settings) -> bool:
    pre_settings.update({
        'repo': ''
    })
    return create_service_from_template('flask', **pre_settings)


def start_super_jopi_infra():
    logger.info('Cleaning previous executions data ...')
    shutil.rmtree('src/playbooks/big-bang/src/')
    playbook = 'src/playbooks/big-bang/sj-infra.yml'
    play_infra_on_local_host = f'ansible-playbook -c=local --inventory 127.0.0.1, ' \
                               f'--limit 127.0.0.1 {playbook} ' \
                               f'-i ansible_hosts'
    run_ansible_playbook = Executor(**{
        'callback': cmd_command,
        'args': [play_infra_on_local_host],
        'known_exceptions': [CalledProcessError]
    })
    run_ansible_playbook.run()
