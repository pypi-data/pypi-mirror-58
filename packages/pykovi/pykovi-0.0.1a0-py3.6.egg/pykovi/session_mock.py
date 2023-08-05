import os
import awswrangler as aw


class SessionMock(aw.Session):
    @property
    def pandas(self) -> aw.Pandas:
        return super().pandas

    @pandas.setter
    def pandas(self, value: aw.Pandas):
        self._pandas = value

    @property
    def s3(self) -> aw.S3:
        return super().s3

    @s3.setter
    def s3(self, value: aw.S3):
        self._s3 = value

    @property
    def glue(self) -> aw.Glue:
        return super().glue

    @glue.setter
    def glue(self, value: aw.Glue):
        self._glue = value
