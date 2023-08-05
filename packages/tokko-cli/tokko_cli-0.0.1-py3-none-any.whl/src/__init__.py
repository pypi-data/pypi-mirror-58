import os
import logging


logger = logging.getLogger(__name__)

REPOSITORIES_FOLDER = os.environ.get('TOKKO_CLI_REPOSITORIES_FOLDER', 'src/playbooks/big-bang/src')

if not os.path.exists(REPOSITORIES_FOLDER):
    os.makedirs(REPOSITORIES_FOLDER)
