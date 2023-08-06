import logging
import time
from typing import TYPE_CHECKING

from forecastflow.enums import Status
from forecastflow.exceptions import InvalidID
from forecastflow.exceptions import OperationFailed
from forecastflow.firebase_api import cloud_firestore
from forecastflow.firebase_api.exceptions import NotFound

if TYPE_CHECKING:
    from forecastflow import Project, User

logger = logging.getLogger(__name__)


class DataSource:
    """
    ForecastFlow data source class
    """

    def __init__(self, project: 'Project', data_source_id: str):
        """
        Instantiate object with given data source ID

        Args:
            project:
                Project which data source belong to.

            data_source_id:
                ID of data source you want to open.
        """
        self.project = project
        self.data_source_id = data_source_id
        self.name = None
        self.status = None
        self.update()

    @property
    def _document(self) -> dict:
        doc = cloud_firestore.get(f"users/{self.user.user_id}"
                                  f"/projects/{self.project.project_id}"
                                  f"/dataSources/{self.data_source_id}",
                                  self.user.id_token)
        return doc['fields']

    @property
    def did(self) -> str:
        return self.data_source_id

    def update(self):
        """
        Update name, status
        """
        try:
            document = self._document
        except NotFound:
            raise InvalidID('Given Data Source ID is not found')

        self.name = document['name']

        if document['profile'].startswith(self.user.user_id):  # TODO: use status instead of profile in future
            self.status = Status.COMPLETED
        elif document['profile'] == '':
            self.status = Status.WAITING
        else:
            self.status = Status(document['profile'])

        logger.info(f"Profiling '{self.name}': {self.status.value}")

    @property
    def user(self) -> 'User':
        return self.project.user

    def wait_until_done(self):
        """
        Wait until ForecastFlow finish profiling.
        """
        while self.status != Status.COMPLETED \
                and self.status != Status.ERROR:
            self.update()
            time.sleep(5)

        if self.status == Status.ERROR:
            document = self._document
            error_info = document.get('errorInfo')
            if error_info is None:
                raise OperationFailed("Profiler quit with Error")
            else:
                raise OperationFailed(f"{error_info['message']}\n"
                                      f"error_log_id: {error_info['errorLogId']}")
