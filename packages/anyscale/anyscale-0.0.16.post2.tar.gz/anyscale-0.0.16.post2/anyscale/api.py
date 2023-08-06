import anyscale.util

def report(message):
    """Show a message in the Anyscale Dashboard."""
    import ray
    worker = ray.worker.get_global_worker()
    job_id = worker.current_job_id.hex()

    anyscale.util.send_json_request("session_report_command", {"job_id": job_id, "message": message}, post=True)

