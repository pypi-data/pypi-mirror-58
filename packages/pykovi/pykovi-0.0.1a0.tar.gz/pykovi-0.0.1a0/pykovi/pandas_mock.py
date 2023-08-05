import pandas as pd
import awswrangler as aw
from typing import Dict, Union, Iterable
import csv
import pykovi as pk


class PandasMock(aw.Pandas):
    def __init__(
        self,
        session: aw.Pandas,
        custom_targets: Dict[str, Union[pd.DataFrame, Iterable[pd.DataFrame]]] = {},
    ):
        super().__init__(session)
        self._custom_targets = custom_targets

    @property
    def custom_targets(self) -> Dict[str, Union[pd.DataFrame, Iterable[pd.DataFrame]]]:
        return self._custom_targets

    @custom_targets.setter
    def custom_targets(
        self, value: Dict[str, Union[pd.DataFrame, Iterable[pd.DataFrame]]]
    ) -> None:
        self._custom_targets = value

    def read_sql_athena(
        self, sql: str, database: str, s3_output: str = None, max_result_size=None
    ) -> Union[pd.DataFrame, Iterable[pd.DataFrame]]:
        custom_target = self.custom_targets.get("{0}:{1}".format(database, sql))
        if (custom_target is not None) & (s3_output is not None):
            self._session.s3.write_dataframe(custom_target, s3_output)
        return (
            custom_target
            if custom_target is not None
            else super().read_sql_athena(
                sql, database, s3_output=s3_output, max_result_size=max_result_size
            )
        )
