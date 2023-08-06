'''Meta command which draws a graph of chapters with Graphviz'''

import yaml

from pathlib import Path


from foliant.meta_commands.base import BaseMetaCommand
from foliant.meta_commands.generate.generate import load_meta
from foliant.preprocessors.testrail import Preprocessor as TestRail


class MetaCommand(BaseMetaCommand):
    config_section = 'testcoverage'
    defaults = {'filename': 'test_data.yml'}
    meta_fields = ['functionality', 'test_case_ids']

    def _get_testrail(self):
        options = {}
        for p in self.config.get('preprocessors', []):
            if isinstance(p, dict):
                if 'testrail' in p:
                    options = p['testrail']
        if not options:
            raise RuntimeError('Error: to use this command add testrail to'
                               'preprocessors list in foliant.yml and set up'
                               'host, login and password.')
        return TestRail(self.context,
                        self.logger,
                        False,
                        False,
                        options)

    def collect_data(self) -> list:
        result = []
        testrail = self._get_testrail()
        for section in self.meta.iter_sections():
            if section.data.get('functionality', False):
                data = {'title': section.title}
                test_cases = []
                for case_id in section.data.get('test_case_ids', []):
                    test_cases.append(testrail._get_case_data(case_id))
                data['test_cases'] = test_cases
                result.append(data)
        return result

    def run(self, config_file_name='foliant.yml', project_path=Path('.')):
        self.logger.debug('Meta command collect_test_data started')

        self.meta = load_meta(self.config['chapters'],
                              self.project_path / self.config['src_dir'])
        test_data = self.collect_data()
        with open(self.options['filename'], 'w') as f:
            yaml.dump({'data': test_data},
                      f,
                      default_flow_style=False,
                      allow_unicode=True,
                      sort_keys=False)
        self.logger.debug('Meta command collect_test_data finished')
