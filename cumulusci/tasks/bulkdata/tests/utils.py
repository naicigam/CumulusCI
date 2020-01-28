from cumulusci.core.config import BaseGlobalConfig
from cumulusci.core.config import BaseProjectConfig
from cumulusci.core.config import TaskConfig
from cumulusci.core.keychain import BaseProjectKeychain
from cumulusci.tests.util import DummyOrgConfig


def _make_task(task_class, task_config):
    task_config = TaskConfig(task_config)
    global_config = BaseGlobalConfig()
    project_config = BaseProjectConfig(global_config, config={"noyaml": True})
    keychain = BaseProjectKeychain(project_config, "")
    project_config.set_keychain(keychain)
    org_config = DummyOrgConfig(
        {"instance_url": "https://example.com", "access_token": "abc123"}, "test"
    )
    return task_class(project_config, task_config, org_config)
