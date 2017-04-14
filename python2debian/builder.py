import glob
import os
import shutil
import subprocess
import time

from jinja2 import FileSystemLoader, Environment


TEMPLATES_PATH = os.path.join(os.path.dirname(__file__), 'templates')


def render_template(template_name, **kwargs):
    env = Environment(loader=FileSystemLoader(TEMPLATES_PATH))
    return env.get_template(template_name).render(**kwargs)


def create_file_from_template(filename, template, **kwargs):
    with open(filename, 'w') as f:
        f.write(render_template(template, **kwargs))


def create_debian_files(debian_folder, **kwargs):
    for filename in ['control', 'changelog', 'compat', 'rules']:
        create_file_from_template(os.path.join(debian_folder, filename),
                                  '{}.j2'.format(filename), **kwargs)

    os.chmod(os.path.join(debian_folder, 'rules'), 0o0755)


def create_setup_file(debian_folder, **kwargs):
    create_file_from_template(os.path.join(debian_folder, 'setup.py'), 'setup.py.j2', **kwargs)


def add_file(src_filename, dst_filename):
    if os.path.exists(src_filename):
        shutil.copyfile(src_filename, dst_filename)


def prepare_package(build_folder, **kwargs):
    kwargs['package_date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')


    debian_folder = os.path.join(build_folder, 'debian')
    if not os.path.exists(debian_folder):
        os.makedirs(debian_folder)

    create_debian_files(debian_folder, **kwargs)

    if kwargs.get('python_package'):
        create_setup_file(build_folder, **kwargs)

    for hook in ['preinst', 'postinst', 'prerm', 'postrm']:
        hook_filename = kwargs.get(hook)
        if hook_filename:
            add_file(hook_filename, os.path.join(debian_folder, hook))


def create_package(build_folder, install_folder):
    os.chdir(build_folder)

    env = os.environ.copy()
    env['DH_VIRTUALENV_INSTALL_ROOT'] = install_folder

    subprocess.call(['dpkg-buildpackage', '-us', '-uc'], env=env)


def move_packages(binary_folder):
    for debian_file in glob.glob('/*.deb'):
        dst_filename = os.path.join(binary_folder, os.path.basename(debian_file))
        if os.path.exists(dst_filename):
            os.remove(dst_filename)
        shutil.move(debian_file, binary_folder)


def build(build_folder, binary_folder, install_folder, **kwargs):
    prepare_package(build_folder, **kwargs)
    create_package(build_folder, install_folder)
    move_packages(binary_folder)
