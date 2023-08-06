import os
import re
import sys
import subprocess

slurm_home = '/nfs3_ib/ip32-ib/home/'

tmpl = """\
#!/bin/bash

{header}

{script}
"""


class Slurm:
    def __init__(self, job_name, script_dir, out_dir, slurm_kwargs=None):
        self.job_name     = job_name
        self.script_dir   = re.sub('/home/', slurm_home, script_dir)
        self.out_dir      = re.sub('/home/', slurm_home, out_dir)
        self.slurm_kwargs = {
                'account':'rrg-xroucou',
                'time':'01:00:00',
                'ntasks':1,
                'mem-per-cpu':'4G',
                }
        if slurm_kwargs is not None:
            self.slurm_kwargs.update(slurm_kwargs)

    def run(self, commands, input_file=None):
        sh_path = self.write_sh_script(commands, input_file)
        args = ['sbatch', '-D', self.out_dir, sh_path]

        print(args)
        res = subprocess.check_output(args).strip()
        print(res, file=sys.stderr)

    def write_sh_script(self, commands, input_file=None):
        header = []
        for k in self.slurm_kwargs:
            header.append('#SBATCH --{}={}'.format(k, self.slurm_kwargs[k]))
        if input_file is not None:
            commands = [c.replace('input_file', input_file) for c in commands]
        commands = [re.sub(' /home/', ' ' + slurm_home, c) for c in commands]
        script = tmpl.format(
                header = '\n'.join(header),
                script = '\n'.join(commands),
                )
        fname  = '{}.sh'.format(self.job_name)
        fpath  = os.path.join(self.script_dir, fname)
        with open(fpath, 'w') as f:
            f.write(script)
        return fpath
