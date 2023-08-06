from __future__ import absolute_import

import argparse
import logging
import os
import signal

from chainerui import _version
from chainerui.database import db
from chainerui.logging import logger
from chainerui.logging import set_loglevel
from chainerui.models.project import Project
from chainerui.server import create_app
from chainerui.utils import db_revision


def _check_db_revision():
    if not db_revision.check_current_db_revision():
        command = '\'chainerui db upgrade\''
        if db_revision.current_db_revision() is None:
            command = 'both \'chainerui db create\' and ' + command
        print('The current DB schema version is not supported.')
        print('Please run {} command before.'.format(command))
        return False
    return True


def _show_banner_debug(app, listener):
    # Such banner should be shown after running process of the server is
    # completed, but Flask has not supported to inject function after the
    # server started.
    from werkzeug.serving import is_running_from_reloader
    if is_running_from_reloader():
        # On debug mode, the banner is shown every reloaded.
        # run_simple set reloader type as 'stat' on default
        logger.info(' * Restarning with stat')
        # level warning is followed by werkzeug implementation
        logger.warning(' * Debugger is active!')
        from werkzeug.debug import get_pin_and_cookie_name
        pin, _ = get_pin_and_cookie_name(app)
        if pin is not None:
            logger.info(' * Debugger PIN: {:s}'.format(pin))
        return
    else:
        logger.info(' * Environment: {}'.format(app.config['ENV']))
        logger.info(' * Debug mode: on')
        logger.info(' * Running on http://{}/ (Press CTRL+C to quit)'.format(
            listener))


def server_handler(args):
    """server_handler."""
    if not db.setup(url=args.db, echo=args.db_echo):
        return
    if not _check_db_revision():
        return

    app = create_app()
    listener = '{:s}:{:d}'.format(args.host, args.port)
    if args.debug:
        logging.getLogger('werkzeug').disabled = True
        set_loglevel(logging.DEBUG)
        app.config['ENV'] = 'development'
        app.debug = True

        _show_banner_debug(app, listener)
        from werkzeug.serving import run_simple
        run_simple(
            args.host, args.port, app, use_reloader=True, use_debugger=True,
            threaded=True)
    else:
        app.config['ENV'] = 'production'
        import gevent
        from gevent.pywsgi import WSGIServer
        http_server = WSGIServer(listener, application=app, log=None)

        def stop_server():
            if http_server.started:
                http_server.stop()

        gevent.signal(signal.SIGTERM, stop_server)
        gevent.signal(signal.SIGINT, stop_server)
        logger.info(' * Environment: {}'.format(app.config['ENV']))
        logger.info(' * Running on http://{}/ (Press CTRL+C to quit)'.format(
            listener))

        try:
            http_server.serve_forever()
        except (KeyboardInterrupt, SystemExit):
            stop_server()


def db_handler(args):
    """db_handler."""

    if args.type == 'create':
        if args.db is None:
            db.init_db()
        return

    if not db.setup(url=args.db, echo=args.db_echo):
        return

    if args.type == 'status':
        current_rev = db_revision.current_db_revision()
        print('The current DB schema version:', current_rev)

    if args.type == 'upgrade':
        db.upgrade()

    if args.type == 'revision':
        db_revision.new_revision()

    if args.type == 'drop':
        if args.db is not None:
            db.downgrade()
        db.remove_db()


def project_create_handler(args):
    """project_create_handler."""
    if not db.setup(url=args.db, echo=args.db_echo):
        return
    if not _check_db_revision():
        return

    project_path = os.path.abspath(args.project_dir)
    project_name = args.project_name

    project = db.session.query(Project).\
        filter_by(path_name=project_path).first()

    if project is None:
        project = Project.create(project_path, project_name)
    else:
        print("Path '{}' has already registered.".format(project.path_name))


def create_parser():
    parser = argparse.ArgumentParser(description='chainerui command')
    parser.add_argument(
        '--version', '-v', action='version', version=_version.__version__)
    parser.add_argument(
        '--db', help='database resource address',
        default=os.getenv('CHAINERUI_DB_URL', default=None))
    parser.add_argument(
        '--db-echo', help='enable database enginge logging',
        action='store_true')
    subparsers = parser.add_subparsers()

    # chainerui server
    parser_server = subparsers.add_parser(
        'server', help='see `chainerui server -h`')
    parser_server.add_argument(
        '-H', '--host', required=False, help='host', default='localhost')
    parser_server.add_argument(
        '-p', '--port', required=False, type=int, help='port', default=5000)
    parser_server.add_argument(
        '-d', '--debug', action='store_true', help='debug')
    parser_server.set_defaults(
        handler=server_handler)

    # chainerui db
    parser_db = subparsers.add_parser(
        'db', help='see `chainerui db -h`')
    parser_db.add_argument(
        'type', choices=['create', 'drop', 'status', 'upgrade', 'revision'])
    parser_db.set_defaults(
        handler=db_handler)

    # chainerui project
    parser_project = subparsers.add_parser(
        'project', help='see `chainerui project -h`')
    parser_project_sub = parser_project.add_subparsers()

    # chainerui project create
    parser_project_create = parser_project_sub.add_parser(
        'create', help='see `chainerui project create -h`')
    parser_project_create.add_argument(
        '-d', '--project-dir', required=True, type=str, help='project-dir')
    parser_project_create.add_argument(
        '-n', '--project-name', type=str, help='project-name', default=None)
    parser_project_create.set_defaults(
        handler=project_create_handler)

    return parser


def main():
    """main."""
    parser = create_parser()
    args = parser.parse_args()

    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
