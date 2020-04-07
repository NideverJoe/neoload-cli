import pytest
from click.testing import CliRunner
from commands.test_settings import cli as settings
from commands.status import cli as status
from commands.logout import cli as logout
from test_utils import *


@pytest.mark.test
@pytest.mark.usefixtures("neoload_login")  # it's like @Before on the neoload_login function
class TestCreate:
    def test_minimal(self, monkeypatch):
        runner = CliRunner()
        result_status = runner.invoke(status)
        assert 'settings id:' not in result_status.output

        test_name = generate_test_settings_name()
        mock_api_post(monkeypatch, 'v2/tests',
                      '{"id":"70ed01da-f291-4e29-b75c-1f7977edf252", "name":"%s", "description":""}' % test_name)
        result = runner.invoke(settings, ['create', test_name])
        assert_success(result)
        json_result = json.loads(result.output)
        assert json_result['name'] == test_name
        assert json_result['description'] == ''

        result_status = runner.invoke(status)
        assert 'settings id: %s' % json_result['id'] in result_status.output

    def test_all_options(self, monkeypatch):
        runner = CliRunner()
        test_name = generate_test_settings_name()
        mock_api_post(monkeypatch, 'v2/tests',
                      '{"id":"70ed01da-f291-4e29-b75c-1f7977edf252", "name":"%s", "description":"test description ",'
                      '"scenarioName":"scenario name", "controllerZoneId":"defaultzone", '
                      '"lgZoneIds":{"defaultzone":5,"UdFyn":1}, "testResultNamingPattern":"test_${runId}"}' % test_name)
        result = runner.invoke(settings,
                               ['create', test_name, '--description', 'test description ',
                                '--scenario', 'scenario name', '--zone', 'defaultzone',
                                '--lgs', 'defaultzone:5,UdFyn:1', '--naming-pattern', 'test_${runId}'])
        assert_success(result)
        json_result = json.loads(result.output)
        assert json_result['name'] == test_name
        assert json_result['description'] == 'test description '
        assert json_result['scenarioName'] == 'scenario name'
        assert json_result['controllerZoneId'] == 'defaultzone'
        assert json_result['lgZoneIds']['defaultzone'] == 5
        assert json_result['lgZoneIds']['UdFyn'] == 1
        assert json_result['testResultNamingPattern'] == 'test_${runId}'

    def test_input_map(self, monkeypatch):
        runner = CliRunner()
        test_name = generate_test_settings_name()
        mock_api_post(monkeypatch, 'v2/tests',
                      '{"id":"70ed01da-f291-4e29-b75c-1f7977edf252", "name":"%s", "description":"test description ",'
                      '"scenarioName":"scenario name", "controllerZoneId":"defaultzone", '
                      '"lgZoneIds":{"defaultzone":5,"UdFyn":1}, "testResultNamingPattern":"test_${runId}"}' % test_name)
        result = runner.invoke(settings, ['create'],
                               input='{"name":"%s", "description":"test description ",'
                                     '"scenarioName":"scenario name", "controllerZoneId":"defaultzone", '
                                     '"lgZoneIds":{"defaultzone":5,"UdFyn":1}, "testResultNamingPattern":"test_${runId}"}' % test_name)
        assert_success(result)
        json_result = json.loads(result.output)
        assert json_result['name'] == test_name
        assert json_result['description'] == 'test description '
        assert json_result['scenarioName'] == 'scenario name'
        assert json_result['controllerZoneId'] == 'defaultzone'
        assert json_result['lgZoneIds']['defaultzone'] == 5
        assert json_result['lgZoneIds']['UdFyn'] == 1
        assert json_result['testResultNamingPattern'] == 'test_${runId}'

    def test_error_required(self):
        runner = CliRunner()
        result = runner.invoke(settings, ['create'])
        assert result.exit_code == 1
        assert 'Error: Expecting value: line 1 column 1' in result.output
        assert 'This command requires a valid Json input' in result.output

    def test_error_invalid_json(self):
        runner = CliRunner()
        result = runner.invoke(settings, ['create'], input='{"key": not valid,,,}')
        assert result.exit_code == 1
        assert 'Error: Expecting value: line 1 column 9 (char 8)' in result.output
        assert 'This command requires a valid Json input' in result.output

    def test_error_not_logged_in(self):
        runner = CliRunner()
        result_logout = runner.invoke(logout)
        assert_success(result_logout)

        result = runner.invoke(settings, ['create', 'any'])
        assert result.exit_code == 1
        assert 'You are\'nt logged' in str(result.exception)