import subprocess

def copy(src, dest):
    run_cmd(['rsync','-r', src, dest])

def write_to(s, dest):
    with open(dest, 'w+') as f:
        f.write(s)

def run_cmd(cmds):
    try:
        subprocess.check_output(' '.join([str(x) for x in cmds]),
                   shell=True,
                  )
    except subprocess.CalledProcessError as e:
        print(e.cmd, e.output, e.stderr)
        raise Exception(f"Failed to execute {e.cmd}. output: {e.output}, error: {e.stderr}")
