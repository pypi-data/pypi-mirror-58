#   Copyright 2018 Red Hat, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

import mock
import sys

from osc_lib.tests import utils
from tripleoclient.v1 import tripleo_validator

VALIDATIONS_LIST = [{
    'description': 'My Validation One Description',
    'groups': ['prep', 'pre-deployment'],
    'id': 'my_val1',
    'name': 'My Validition One Name',
    'parameters': {}
}, {
    'description': 'My Validation Two Description',
    'groups': ['prep', 'pre-introspection'],
    'id': 'my_val2',
    'name': 'My Validition Two Name',
    'parameters': {}
}]


class TestValidatorList(utils.TestCommand):

    def setUp(self):
        super(TestValidatorList, self).setUp()

        # Get the command object to test
        self.cmd = tripleo_validator.TripleOValidatorList(self.app, None)

    @mock.patch('tripleoclient.utils.parse_all_validations_on_disk',
                return_value=VALIDATIONS_LIST)
    def test_validation_list_noargs(self, mock_validations):
        arglist = []
        verifylist = []

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        self.cmd.take_action(parsed_args)


class TestValidatorRun(utils.TestCommand):

    def setUp(self):
        super(TestValidatorRun, self).setUp()

        # Get the command object to test
        self.cmd = tripleo_validator.TripleOValidatorRun(self.app, None)

    @mock.patch('sys.exit')
    @mock.patch('logging.getLogger')
    @mock.patch('pwd.getpwuid')
    @mock.patch('os.getuid')
    @mock.patch('tripleoclient.utils.get_tripleo_ansible_inventory',
                return_value='/home/stack/inventory.yaml')
    @mock.patch('tripleoclient.utils.run_ansible_playbook',
                autospec=True)
    def test_validation_run_with_ansible(self, plan_mock, mock_inventory,
                                         mock_getuid, mock_getpwuid,
                                         mock_logger, mock_sysexit):
        mock_pwuid = mock.Mock()
        mock_pwuid.pw_dir = '/home/stack'
        mock_getpwuid.return_value = mock_pwuid

        mock_log = mock.Mock()
        mock_logger.return_value = mock_log

        playbooks_dir = '/usr/share/openstack-tripleo-validations/playbooks'
        arglist = [
            '--validation-name',
            'check-ftype'
        ]
        verifylist = []

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)
        self.cmd.take_action(parsed_args)

        plan_mock.assert_called_once_with(
            logger=mock_log,
            plan='overcloud',
            inventory='/home/stack/inventory.yaml',
            workdir=playbooks_dir,
            log_path_dir='/home/stack',
            playbook='check-ftype.yaml',
            retries=False,
            output_callback='validation_output',
            extra_vars={},
            python_interpreter='/usr/bin/python{}'.format(sys.version_info[0]),
            gathering_policy='explicit'
        )

        assert mock_sysexit.called
