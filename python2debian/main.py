import argparse

from python2debian.builder import build


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--build-dir', help='Build folder', default='/build')
    parser.add_argument('--packages-dir', help='Packages folder', default='/packages')
    parser.add_argument('--install-dir', help='Installation folder', default='/opt')
    parser.add_argument('--package-name', help='Package name')
    parser.add_argument('--package-desc', help='Package description')
    parser.add_argument('--package-version', help='Package version')
    parser.add_argument('--package-author', help='Package author', default='Root <root@localhost>')
    parser.add_argument('--python-version', help='Python version', default='python2.7')
    parser.add_argument('--python-package', help='Python package')
    args = parser.parse_args()

    build(args.build_dir, args.packages_dir, args.install_dir,
          package_name=args.package_name,
          package_description=args.package_desc or args.package_name,
          package_version=args.package_version,
          package_author=args.package_author,
          python_version=args.python_version,
          python_package=args.python_package)


if __name__ == '__main__':
    main()
