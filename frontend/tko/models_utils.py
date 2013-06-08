"""
Simple utility wrappers around the TKO models
"""

from autotest.frontend.tko.models import Job, Test, Machine


def job_get_by_tag(tag):
    '''
    Return a job based on its tag
    '''
    try:
        job = Job.objects.get(tag=tag)
    except Job.DoesNotExist:
        return None
    return job


def job_get_idx_by_tag(tag):
    '''
    Return the job id based on the job tag
    '''
    job = job_get_by_tag(tag)
    if job is None:
        return None
    return job.job_idx


def job_delete_by_tag(tag):
    '''
    Deletes a job entry based on its tag
    '''
    Job.objects.get(tag=tag).delete()
    return job_get_by_tag(tag) is None


def jobs_get_by_tag_range(jobid_range):
    '''
    Return jobs based on range of job ids
    '''
    job_list = []
    for job_index in jobid_range:
        tag_pattern = "%s-" % job_index
        jobs = Job.objects.filter(tag__startswith=tag_pattern)
        job_list += jobs
    return job_list


def tests_get_by_job_idx(job_idx):
    '''
    Returns all tests based on its job idx
    '''
    return Test.objects.filter(job=job_idx)


def test_get_by_idx(test_idx):
    '''
    Returns a test based on its index or None
    '''
    try:
        test = Test.objects.get(pk=test_idx)
    except Test.DoesNotExist:
        return None
    return test


def test_delete_by_idx(test_idx):
    '''
    Delete test based on its idx
    '''
    Test.objects.get(pk=test_idx).delete()
    return test_get_by_idx(test_idx) is None


def machine_get_by_hostname(hostname):
    '''
    Returns a machine based on its hostname or None
    '''
    try:
        machine = Machine.objects.get(hostname=hostname)
    except Machine.DoesNotExist:
        return None
    return machine


def machine_get_idx_by_hostname(hostname):
    '''
    Return the job id based on the job tag
    '''
    machine = machine_get_by_hostname(hostname)
    if machine is None:
        return None
    return machine.machine_idx


def machine_create(hostname, machine_group=None, owner=None):
    '''
    Creates a new machine being silent if it already exists
    '''
    try:
        machine = Machine.objects.get(hostname__exact=hostname)
    except Machine.DoesNotExist:
        machine = Machine.objects.create(hostname=hostname)

    if machine_group is not None:
        machine.machine_group = machine_group

    if owner is not None:
        machine.owner = owner

    return machine
