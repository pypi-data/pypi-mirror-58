import click
import os
import re
import importlib.util as iu
import glue_jobs
import awswrangler as aw

glue_jobs.disable_auto_execute()


@click.command("publish_jobs", context_settings={"ignore_unknown_options": True})
@click.option("--aws-access-key-id", type=click.STRING, envvar="AWS_ACCESS_KEY_ID")
@click.option(
    "--aws-secret-access-key", type=click.STRING, envvar="AWS_SECRET_ACCESS_KEY"
)
@click.option("--aws-session-token", type=click.STRING, envvar="AWS_SESSION_TOKEN")
@click.argument(
    "files",
    nargs=-1,
    type=click.Path(exists=True, file_okay=True, dir_okay=False, resolve_path=True),
)
def publish_jobs(aws_access_key_id, aws_secret_access_key, aws_session_token, files):
    for filename in [f for f in list(files) if f.endswith(".py")]:
        spec = iu.spec_from_file_location(os.path.basename(filename), filename)
        module = iu.module_from_spec(spec)
        spec.loader.exec_module(module)

    for glue_job_item in glue_jobs.declared_jobs:
        session = aw.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token,
        )
        glue_job_item.publish_job(session)


if __name__ == "__main__":
    publish_jobs()
