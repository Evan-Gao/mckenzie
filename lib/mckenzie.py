# Example script for updating McKenzie from within a Python job

import requests, os

def update_mckenzie(progress, metric):

    try:
        job_id = os.environ['SLURM_JOB_ID']
        endpoint = os.environ['MCKENZIE_ENDPOINT']
        requests.post(
            'http://' + endpoint+'/hooks/update_job/',
            data={
                'jobid': job_id,
                'progress': progress,
                'metric': metric
            }
        )
    except Exception as e:
        print(e)