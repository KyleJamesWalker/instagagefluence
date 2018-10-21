"""Load a configuration for this project."""
import os
import pkgutil

import yamlsettings

from yamlsettings.extensions.base import YamlSettingsExtension


class ConfigExtension(YamlSettingsExtension):
    """Load a yaml resource from this python package.

    Args:
      resource: The resource to load from the package (default: settings.yaml)
      env: When set the yamldict will update with env variables (default: true)
      prefix: Prefix for environment loading (default: None)
      persist: When set the yamldict will only be loaded once. (default: true)
    examples:
      * igf://ex.yaml (opens the settings.yaml package resource then ex.yaml)
    """
    protocols = ['igf']
    default_query = {
        'resource': 'settings.yaml',
        'env': True,
        'prefix': 'IGF',
        'persist': True,
    }
    _persistence = {}

    @classmethod
    def load_target(cls, scheme, path, fragment, username,
                    password, hostname, port, query,
                    load_method, **kwargs):
        persist = query['persist']

        if persist and cls._persistence:
            return cls._persistence

        overrides = (hostname or '') + path
        package_path = 'instagagefluence'
        query.update(kwargs)

        resource = query['resource']
        env = query['env']
        prefix = query['prefix']

        pkg_data = pkgutil.get_data(package_path, resource)

        yaml_contents = load_method(pkg_data)

        override_contents = None
        if overrides and os.path.isfile(overrides):
            override_contents = load_method(open(overrides))

        if override_contents:
            yaml_contents.update(override_contents)
        else:
            print("Warning: No configuration Found - ".format(overrides))

        if env:
            yamlsettings.update_from_env(yaml_contents, prefix)

        if persist:
            cls._persistence = yaml_contents

        return yaml_contents
