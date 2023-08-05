import awswrangler as aw
import pandas as pd
import os
import boto3
import shutil
import logging


logger = logging.getLogger(__name__)


class S3Mock(aw.S3):
    def __init__(self, session: aw.Session, target_dir: str = os.getcwd() + "/.cache"):
        self._session = session
        self._base_path = target_dir
        if not os.path.exists(target_dir):
            os.makedirs(self.base_path)

    @property
    def base_path(self) -> str:
        return self._base_path

    def parse_path(self, s3_path: str) -> str:
        return s3_path.replace("s3://", self.base_path + "/")

    def write_dataframe(
        self,
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
        target_path = self.parse_path(path)
        target_folder = os.path.dirname(target_path)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        if file_format == "parquet":
            dataframe.to_parquet(
                target_path, compression=compression, partition_cols=partition_cols
            )
        if file_format == "csv":
            dataframe.to_csv(target_path)

    def read_dataframe(self, path: str, file_format: str = "parquet") -> pd.DataFrame:
        target_path = path.replace("s3://", self.base_path + "/")
        if file_format == "parquet":
            return pd.read_parquet(target_path)

    def write_file(self, input_file: str, output_path: str) -> None:
        s3_path = self.parse_path(output_path)
        logger.info("Publishing job to {0}.".format(s3_path))
        target_folder = os.path.dirname(s3_path)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        shutil.copy(input_file, s3_path)
