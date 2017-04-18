import argparse

from python2debian.builder import build


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--build-dir', help='Build folder', default='/build')
    parser.add_argument('--packages-dir', help='Packages folder', default='/packages')
    parser.add_argument('--install-dir', help='Installation folder', default='/opt')
    parser.add_argument('--source-dir', help='Source folder')
    parser.add_argument('--package-name', help='Package name')
    parser.add_argument('--package-version', help='Package version')
    parser.add_argument('--package-desc', help='Package description', default='My Debian Package')
    parser.add_argument('--package-author', help='Package author', default='Root <root@localhost>')
    parser.add_argument('--python-version', help='Python version', default='python2.7')
    parser.add_argument('--python-bin', help='Python binary', default='/usr/bin/python2.7')
    parser.add_argument('--python-package', help='Python package')
    parser.add_argument('--preinst', help='Debian package preinst')
    parser.add_argument('--postinst', help='Debian package postinst')
    parser.add_argument('--prerm', help='Debian package prerm')
    parser.add_argument('--postrm', help='Debian package postrm')
    parser.add_argument('--file', help='Add file to package', action='append')
    args = parser.parse_args()

    if not args.package_name:
        raise Exception('You must provide a package name')

    if not args.package_version:
        raise Exception('You must provide a package version')

    build(args.build_dir, args.packages_dir, args.install_dir, args.source_dir,
          package_name=args.package_name,
          package_description=args.package_desc or args.package_name,
          package_version=args.package_version,
          package_author=args.package_author,
          python_version=args.python_version,
          python_bin=args.python_bin,
          python_package=args.python_package,
          preinst=args.preinst,
          postinst=args.postinst,
          prerm=args.prerm,
          postrm=args.postrm,
          files=args.file)


if __name__ == '__main__':
    main()
