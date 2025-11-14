from enum import Enum as PyEnum


class SourceEnum(str, PyEnum):

    OTODOM = "otodom"


class StatusEnum(str, PyEnum):

    QUEUED = "queued"
    RUNNING = "running"
    FAILED = "failed"
    ABORTED = "aborted"
    SUCCESS = "success"
