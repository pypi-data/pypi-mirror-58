import json
import os
import subprocess
from jinja2 import Environment, Template, FileSystemLoader
from k9.core import last_word


def helm_install(chart_name: str, params, release_name: str = None, debug = False):
    """
    Runs the Helm installation for the specified chart.   Before the chart
    is installed, the values file which should have the same name as the release_name
    will be evaluated with Jinja, using the parameters to build the new values file.

    The values file is written to the .output/{{release-name}}-values.yaml.

    Helm installation is run with this values.yaml file.

    :param chart_name: Name of Chart.
    :param params: Parameter values used when pre-processing values.
    :param release_name: If None - release_name is defaulted to the last word in chart_name.  For example
           if chart_name is "stable/tomcat", the release_name is "tomcat".   Release name
           is also used to construct the charts values file in the following format:
           ./charts/{{release_name}}-values.yaml
    :param debug: If True, runs Helm with --debug and --dry-run, which will not actually run
                  and displays the chart values.  Default is False.
    :return: 0 for success, non-zero for failure.
    """
    f = None

    try:
        # setup release_name
        if release_name is None:
            release_name = last_word(chart_name)

        env = Environment(loader=FileSystemLoader('./charts/'))
        value_fn = f'{release_name}-values.yaml'

        if not os.path.exists(f'./charts/{value_fn}'): 
            value_fn = f'{release_name}-values.yml'

        if not os.path.exists(f'./charts/{value_fn}'): 
            print(f'values file not found: ./charts/{value_fn}')
            
        template = env.get_template(value_fn)
        template_body = template.render(params)

        if not os.path.exists('./.output'):
            os.mkdir('./.output')

        value_path = f'./.output/{value_fn}'
        f = open(value_path, 'w+')
        f.write(template_body)
        f.close()

        the_call = ['helm', 'install', '-f', value_path, release_name, chart_name]
        if debug:
            the_call.extend(['--debug', '--dry-run'])
        subprocess.check_call(the_call)

    finally:
        if f is not None:
            f.close()


def helm_ls():
    """
    Lists all current helm installations.

    :return: List of all helm installations.

    Sample Output::

        [
            {"name":"tomcat",
            "namespace":"default",
            "revision":"1",
            "updated":"2019-12-10 18:28:43.753814 -0500 EST",
            "status":"deployed",
            "chart":"tomcat-0.4.0",
            "app_version":"7.0"}
        ]

    """
    values = subprocess.check_output(['helm', 'ls', '-o', 'json'])
    result = json.loads(values)
    return result

def helm_exists(release_name: str):
    """
    Returns true if the specified release_name exist.

    :param release_name: Name of release.
    :return: True if found.
    """
    result = helm_ls()
    found = [
        release
        for release in result
        if release['name'] == 'tomcat'
    ]
    return len(found) > 0

def helm_uninstall(release_name: str):
    """
    Uninstalls the specified release.

    :param release_name: Name of the release you want to uninstall.
    :return: Returns output value from uninstall process.  Otherwise throws exception.
    """
    return subprocess.check_output(['helm', 'uninstall', release_name])


def helm_update(release_name: str, chart_name: str, params ):
    """
    Runs the Helm installation for the specified chart.   Before the chart
    is installed, the values file which should have the same name as the release_name
    will be evaluated with Jinja, using the parameters to build the new values file.

    The values file is written to the .output/{{release-name}}-values.yaml.

    Helm installation is run with this values.yaml file.

    :param release_name: Name of installation, which in Helm is called a release.
                        Note that the corresponding values filename will be:
                        /charts/{{release_name}}-values.yaml
    :param chart_name: Name of chart.
    :param params: Parameters to be used against the chart values templates.
    :return: 0 for success, non-zero for failure.
    """
    pass

