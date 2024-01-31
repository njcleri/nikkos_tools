import numpy as np

class CloudySlurm:
    def __init__(self) -> None:
        self.slurm = []
        
    def set_parameter(self, parameter):
        self.model.append(parameter)
    
    def delete_parameter(self, parameter):
        self.model = [item for item in self.model if item not in parameter]
        
    def set_export(self, export='NONE'):
        self.set_parameter(f'#SBATCH --export={export}')
    
    def set_user_env(self, user_env='L'):
        self.set_parameter(f'#SBATCH --get-user-env={user_env}')
        
    def set_job_name(self, job_name):
        self.job_name = job_name
        self.set_parameter(f'#SBATCH --job-name={job_name}')
        
    def set_time(self, time):
        self.set_parameter(f'#SBATCH --time=={time}')
        
    def set_ntasks(self, ntasks):
        self.set_parameter(f'#SBATCH --ntasks=={ntasks}')
        
    def set_ntasks_per_node(self, ntasks_per_node):
        self.set_parameter(f'#SBATCH --ntasks-per-node=={ntasks_per_node}')
        
    def set_mem(self, mem):
        self.set_parameter(f'#SBATCH --mem={mem}')
        
    def set_output(self, output):
        self.set_parameter(f'#SBATCH --output={output}.%j')
        
    def set_executable_line(self, executable_line):
        self.set_parameter(f'{executable_line}')
    
    def set_cloudy_executable_line(self, cloudy_executable, cloudy_input):
        self.set_parameter(f'{cloudy_executable} {cloudy_input}')
        

    def build_default_model(self, job_name='test_job', time='01:00:00', ntasks=1, ntasks_per_node=1, mem='2560M', output='test_job', cloudy_executable='run_cloudy', cloudy_input='test'):
        self.model = []
        self.set_parameter(f'#!/bin/bash')
        self.set_parameter(f'##ENVIRONMENT SETTINGS; CHANGE WITH CAUTION')
        self.set_export()
        self.set_user_env()
        self.set_parameter(f'##NECESSARY JOB SPECIFICATIONS')
        self.set_job_name(job_name)
        self.set_time(time)
        self.set_ntasks(ntasks)
        self.set_ntasks_per_node(ntasks_per_node)
        self.set_mem(mem)
        self.set_output(output)
        if type(cloudy_input) != list:
            self.set_cloudy_executable_line(cloudy_executable, cloudy_input)
            return
        for infile in cloudy_input:
            self.set_cloudy_executable_line(cloudy_executable, infile)
            
    def make_slurm(self, path='.', name=None):
        if not name:
            np.savetxt(f'{path}/{self.job_name}.slurm', self.model, fmt='%s')
            return
        np.savetxt(f'{path}/{name}.slurm', self.model, fmt='%s')
    