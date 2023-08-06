#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : wheat/main.py
# Author            : Jimin Huang <huangjimin@whu.edu.cn>
# Date              : 13.02.2018
# Last Modified Date: 14.02.2018
# Last Modified By  : Jimin Huang <huangjimin@whu.edu.cn>
# -*- coding: utf-8 -*-
# File: wheat/main.py
# Author: Jimin Huang <huangjimin@whu.edu.cn>
# Date: 14.11.2017
import os
import pkg_resources
import subprocess

from sphinx import apidoc

from wheat.exceptions import InstallFailedException, ProjectGenerationError
from wheat.constant import PACKAGE_VERSION, CONF_RULES
from wheat.utils import (
    directories_to_create, files_to_generate, generate_match_rules,
    generate_other_requirements
)


def main():
    """Read inputs and generate projects
    """
    project_name = raw_input('Input your project name: ')
    service_name = raw_input('Input your service name: ')
    author_name = raw_input('Input your author name: ')
    output_dir = raw_input('Input your output dir: ')

    packages = PACKAGE_VERSION.keys()

    install_packages(packages)

    directories = directories_to_create(project_name)
    files = files_to_generate(project_name)
    match_rules = generate_match_rules(files)
    other_requirements = generate_other_requirements()

    create_directories(directories, output_dir)
    generate_files(
        files, output_dir, project_name, author_name, match_rules,
        other_requirements, service_name
    )
    generate_doc(project_name, author_name, output_dir)

    check_project(files, output_dir)


def install_packages(packages):
    """Install packages from pypi

    Args:
        packages: a list of `str`

    Raises:
        `InstallFailedException` raised when pip install package failed
    """
    subprocess.call([
        'python', '-m', 'pip', 'install', '--force-reinstall', 'pip==10.0.1'
    ])

    try:
        from pip._internal import main as pip_main
    except Exception:
        from pip import main as pip_main

    for package in packages:
        try:
            __import__(package)
        except ImportError:
            install_status = pip_main([
                'install', '-i',
                'http://pypi.kube.chancefocus.com/root/pypi/+simple/',
                '--trusted-host', 'pypi.kube.chancefocus.com',
                '-U', package
            ])

            if install_status != 0:
                raise InstallFailedException(package)


def create_directories(directories, output_dir):
    """Make directories

    Caution:
        Parent directory should in front of the directories,
        and child directory should in the rear.

    Args:
        directories: a list of str
        output_dir: a str as the output directory
    """
    for directory in directories:
        os.makedirs(os.path.join(output_dir, directory))


def generate_files(
    files, output_dir, project_name, author_name, match_rules,
    other_requirements, service_name
):
    """Generate files with given file path

    Args:
        files: a list of `str`
        output_dir: a `str` as the output directory
        project_name: a `str`
        author_name: a `str`
        match_rules: a dict as {str: str}
        other_requirements: a str
        service_name: a str
    """
    for f in files:
        template_name = match_rules[f]

        output_file = os.path.join(output_dir, f)

        class_name = ''.join(
            [word[0].upper() + word[1:] for word in project_name.split('_')]
        )
        chart_name = '-'.join(project_name.split('_'))

        with open(
            pkg_resources.resource_filename(
                'wheat.template',
                '{0}'.format(template_name)
            )
        ) as template:
            with open(output_file, 'w') as output:
                replace_rules = {
                    '{PROJECT_NAME}': project_name,
                    '{AUTHOR_NAME}': author_name,
                    '{FILE_NAME}': f,
                    '{CLASS_NAME}': class_name,
                    '{ENV_NAME}': project_name.upper(),
                    '{OTHER_REQUIREMENTS}': other_requirements,
                    '{SERVICE_NAME}': service_name,
                    '{CHART_NAME}': chart_name,
                }
                content = template.read()
                for key, value in replace_rules.iteritems():
                    content = content.replace(key, value)
                output.write(content)


def check_project(files, output_dir):
    """Check if project generated

    Args:
        files: a list of str
        output_dir: a str as the output directory

    Raises:
        ProjectGenerationError when files not generated as expected
    """
    for f in files:
        real_path = os.path.join(output_dir, f)
        if os.path.isfile(real_path):
            continue
        raise ProjectGenerationError(f)


def generate_doc(project_name, author_name, output_dir):
    """Generate doc by using `shpinx.apidoc`

    Args:
        project_name: a `str`
        author_name: a `str`
        output_dir: a `str` as the output directory
    """
    output_path = os.path.join(output_dir, project_name, 'doc')
    project_path = os.path.join(output_dir, project_name, project_name)

    apidoc.main(argv=[
        '', project_path,
        '-o', output_path,
        '-f',
        '-e',
        '-F',
        '-H', project_name,
        '-A', author_name,
        '-V', '0.1.0',
        '-R', 'Initialize'
    ])

    conf_file = os.path.join(output_path, 'conf.py')
    with open(conf_file, 'r') as conf:
        conf_content = conf.read()

    with open(conf_file, 'w') as output:
        for key, value in CONF_RULES.iteritems():
            conf_content = conf_content.replace(key, value)
        output.write(conf_content)
