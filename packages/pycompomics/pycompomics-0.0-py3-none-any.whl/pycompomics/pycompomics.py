import os
import yaml
from PySlurm.pyslurm import Slurm

searchgui_path   = '/home/xroucou_group/tools/compomics/SearchGUI-3.3.17/SearchGUI-3.3.17.jar'
parameters_cache = '/home/xroucou_group/tools/compomics/params_cache'
fasta_db         = '/home/sleblanc/op13_ref.fasta'

class SearchGUI:
    def __init__(self, mgf_dir, out_dir,
            searchgui_path=searchgui_path, fasta_db=fasta_db,
            parameters_cache=parameters_cache, ms_level='high'):
        self.searchgui_path   = os.path.abspath(searchgui_path)
        self.parameters_cache = os.path.abspath(parameters_cache)
        self.mgf_dir    = os.path.abspath(mgf_dir)
        self.out_dir    = os.path.abspath(out_dir)
        self.fasta_db   = os.path.abspath(fasta_db)
        self.report_dir = os.path.join(self.out_dir, 'reports')
        self.log_dir    = os.path.join(self.out_dir, 'logs')
        self.ms_level   = ms_level
        if not os.path.exists(self.report_dir):
            os.mkdir(self.report_dir)
        if not os.path.exists(self.report_dir):
            os.mkdir(self.report_dir)

    def run_search(self, ):
        # copy tools to temp dir
        commands = [
                'module add java/1.7.0_80 gcc/4.8.5',
                ]


        # SearchGUI params
        if self.search_params_path is None:
            self.set_search_params()

        # SearchGUI cmd
        search_cmd = self.get_search_cmd()

        s = Slurm()

        #s.run()


    def set_search_params(self, **kwargs):
        with open('/home/sleblanc/PyCompomics/searchgui_default_params.yml', 'r') as f:
            def_params = yaml.full_load(f)
        params = def_params['ms-common']
        for k in kwargs:
            params[k] = kwargs[k]
        params.update(def_params['ms-levels'][self.ms_level])

        if self.fasta_db is None:
            wd = os.getcwd()
            os.chdir(self.db_cache)
            cmd = 'java -cp {} eu.isas.searchgui.cmd.FastaCLI -in {} -decoy'.format(
                    self.searchgui_path, self.fasta_db)
            subprocess.Popen(cmd)
            os.chdir(wd)

        if self.search_params_path is None:
            pass

        params['out'] = self.out_dir
        params['db']  = self.fasta_db

        self.search_params_path = search_params_path

    def get_search_cmd(self, ):
        cmd = 'java -Xmx27G -cp {}'.format(self.searchgui_path)
        return cmd

class PeptideShaker:
    def __init__(self, ):
        pass
