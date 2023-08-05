import awswrangler as aw
from functools import wraps
import pandas as pd
import boto3
from types import MethodType
from typing import Any, Dict
import pyarrow.parquet as pq
from pykovi.glue_jobs import GlueJobItem
import s3fs


default_session: aw.Session = None


def get_default_session() -> aw.Session:
    return default_session or aw.Session()


def set_default_session(session: aw.Session) -> None:
    global default_session
    default_session = session


def write_dataframe(
    self: aw.S3,
    dataframe: pd.DataFrame,
    path: str,
    file_format: str = "parquet",
    database=None,
    table=None,
    partition_cols=None,
    preserve_index=True,
    mode="append",
    compression=None,
    procs_cpu_bound=None,
    procs_io_bound=None,
    cast_columns=None,
    extra_args=None,
    inplace=True,
) -> None:
    """Writes a pandas dataframe to the specified s3 path.
    
    Arguments:
        self {aw.S3} -- The target awswrangler s3 object.
        dataframe {pd.DataFrame} -- The dataframe object to write.
        path {str} -- The destiny s3 filepath.
    
    Keyword Arguments:
        file_format {str} -- Format to save the table [csv|parquet] (default: {"parquet"})
        database {[type]} -- [description] (default: {None})
        table {[type]} -- [description] (default: {None})
        partition_cols {[type]} -- [description] (default: {None})
        preserve_index {bool} -- [description] (default: {True})
        mode {str} -- [description] (default: {"append"})
        compression {[type]} -- [description] (default: {None})
        procs_cpu_bound {[type]} -- [description] (default: {None})
        procs_io_bound {[type]} -- [description] (default: {None})
        cast_columns {[type]} -- [description] (default: {None})
        extra_args {[type]} -- [description] (default: {None})
        inplace {bool} -- [description] (default: {True})
    
    Returns:
        None -- [description]
    """
    current_session: aw.Session = self._session
    current_session.pandas.to_s3(
        dataframe,
        path,
        file_format,
        database=database,
        table=table,
        partition_cols=partition_cols,
        preserve_index=preserve_index,
        mode=mode,
        compression=compression,
        procs_cpu_bound=procs_cpu_bound,
        procs_io_bound=procs_io_bound,
        cast_columns=cast_columns,
        extra_args=extra_args,
        inplace=inplace,
    )


def read_dataframe(
    aw_s3: aw.S3, path: str, file_format: str = "parquet"
) -> pd.DataFrame:
    """Reads dataframe from a given s3 path.
    
    Arguments:
        aw_s3 {aw.S3} -- [description]
        path {str} -- [description]
    
    Keyword Arguments:
        file_format {str} -- [description] (default: {"parquet"})
    
    Returns:
        pd.DataFrame -- [description]
    """
    session: aw.Session = aw_s3._session
    fs = s3fs.S3FileSystem(
        key=session.aws_access_key_id,
        secret=session.aws_secret_access_key,
        token=session.aws_session_token,
    )
    if file_format == "parquet":
        return pq.ParquetDataset(path, filesystem=fs).read_pandas().to_pandas()


def start_job_run(
    aw_glue: aw.Glue,
    job_name: str,
    job_args: Dict[str, Any] = {},
    job_parameters: Dict[str, Any] = {},
) -> Dict[str, str]:
    """Executes a glue job
    
    Arguments:
        aw_glue {aw.Glue} -- [description]
        job_name {str} -- [description]
    
    Keyword Arguments:
        job_args {Dict[str, Any]} -- [description] (default: {{}})
        job_parameters {Dict[str, Any]} -- [description] (default: {{}})
    
    Returns:
        Dict[str, str] -- [description]
    """
    session: aw.Session = aw_glue._session
    glue_client = boto3.Session(
        aws_access_key_id=session.aws_access_key_id,
        aws_secret_access_key=session.aws_secret_access_key,
        aws_session_token=session.aws_session_token,
    ).client("glue")
    return glue_client.start_job_run(
        JobName=job_name, Arguments=job_parameters, **job_args
    )


def split_s3_path(s3_path):
    path_parts = s3_path.replace("s3://", "").split("/")
    bucket = path_parts.pop(0)
    key = "/".join(path_parts)
    return bucket, key


def write_file(aws3: aw.S3, input_file: str, output_path: str) -> None:
    bucket, key = split_s3_path(output_path)
    session: aw.Session = aws3._session
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=session.aws_access_key_id,
        aws_secret_access_key=session.aws_secret_access_key,
        aws_session_token=session.aws_session_token,
    )
    s3_client.upload_file(input_file, bucket, key)


def create_job(aw_glue: aw.Glue, glue_job_item: GlueJobItem):
    session = aw_glue._session
    glue_client = boto3.client(
        "glue",
        aws_access_key_id=session.aws_access_key_id,
        aws_secret_access_key=session.aws_secret_access_key,
        aws_session_token=session.aws_session_token,
        region_name=glue_job_item._region,
    )
    return glue_client.create_job(
        Name=glue_job_item._name,
        Description=glue_job_item._description,
        Role=glue_job_item._role,
        ExecutionProperty=glue_job_item._execution_property,
        Command=glue_job_item._command,
        DefaultArguments=glue_job_item._default_arguments,
        Connections=glue_job_item._connections,
        MaxRetries=glue_job_item._max_retries,
        Timeout=glue_job_item._timeout,
        MaxCapacity=glue_job_item._max_capacity,
        SecurityConfiguration=glue_job_item._security_configuration,
        Tags=glue_job_item._tags,
        NotificationProperty=glue_job_item._notification_property,
        GlueVersion=glue_job_item._glue_version,
        NumberOfWorkers=glue_job_item._number_of_workers,
        WorkerType=glue_job_item._worker_type,
    )


aw.S3.write_dataframe = write_dataframe
aw.S3.read_dataframe = read_dataframe
aw.S3.write_file = write_file
aw.Glue.create_job = create_job
aw.Glue.start_job_run = start_job_run
