import os

CONTAINER_DIR = '/usr/src/app'

def _get_docker_run(pwd, container_dir, image_name):
    return 'docker run --rm -i -v %s:%s -w %s %s /bin/bash -l -c ' % (pwd, container_dir, container_dir, image_name)

def _get_no_docker_run():
    return '/bin/bash -c '

def get_run_by_platform(platform, pwd, with_docker):
    if with_docker:
        if platform == 'js':
            return _get_docker_run(pwd, CONTAINER_DIR, 'skygeario/skygear-nodedev')
        if platform == 'android':
            return _get_docker_run(pwd, CONTAINER_DIR, 'skygeario/skygear-androiddev')
        raise Exception('%s not supported.' % (platform))
    else:
        return _get_no_docker_run()

def run_command(platform, pwd, cmd, with_docker):
    run = get_run_by_platform(platform, pwd, with_docker)
    line = run + '\"%s\"' % (cmd)
    print('Running: ' + line)
    os.system(line)
