import sys
import pytest

import shakedown


def out(msg):
    '''Emit an informational message on test progress during test runs'''
    print(msg, file=sys.stderr)

    # I'd much rather the latter, but it is super confusing intermingled with
    # shakedown output.

    ## pytest is awful; hack around its inability to provide a sanely
    ## configurable logging environment
    #current_time = datetime.datetime.now()
    #frames = inspect.getouterframes(inspect.currentframe())
    #try:
    #    parent = frames[1]
    #finally:
    #    del frames
    #try:
    #    parent_filename = parent[1]
    #finally:
    #    del parent
    #name = inspect.getmodulename(parent_filename)
    #out = "{current_time} {name} {msg}\n".format(current_time=current_time,
    #                                             name=name,
    #                                             msg=msg)
    #sys.stderr.write(out)


def gc_frameworks():
    '''Reclaims private agent disk space consumed by Mesos but not yet garbage collected'''
    for host in shakedown.get_private_agents():
        shakedown.run_command(host, "sudo rm -rf /var/lib/mesos/slave/slaves/*/frameworks/*")

dcos_1_9_or_higher = pytest.mark.skipif('shakedown.dcos_version_less_than("1.9")',
                                        reason="Feature only supported in DC/OS 1.9 and up")
dcos_1_10_or_higher = pytest.mark.skipif('shakedown.dcos_version_less_than("1.10")',
                                         reason="Feature only supported in DC/OS 1.10 and up")
