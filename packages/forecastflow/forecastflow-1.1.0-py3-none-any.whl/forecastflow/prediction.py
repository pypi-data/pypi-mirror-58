import logging
import time
from typing import TYPE_CHECKING

import pandas as pd
from io import BytesIO

from forecastflow.enums import Status
from forecastflow.exceptions import InvalidID
from forecastflow.exceptions import OperationFailed
from forecastflow.firebase_api import cloud_firestore, storage
from forecastflow.firebase_api.exceptions import NotFound

if TYPE_CHECKING:
    from forecastflow import Model, Project, User

logger = logging.getLogger(__name__)


class Prediction:
    """
    ForecastFlow prediction object
    """

    def __init__(self, model: 'Model', prediction_id: str):
        """
        Instantiate object with given prediction ID.

        Args:
            model:
                Model which makes this predict.

            prediction_id:
                ID of prediction you want to open.
        """
        self.model = model
        self.prediction_id = prediction_id
        self.name = None
        self.status = None
        self.update()

    @property
    def _document(self):
        doc = cloud_firestore.get(f'users/{self.user.user_id}/projects/{self.project.project_id}'
                                  f'/predicts/{self.prediction_id}',
                                  self.user.id_token)
        return doc['fields']

    def get_result(self) -> pd.DataFrame:
        """
        Download the result from ForecastFlow.

        Returns:
            result with primary key and predicted values.
        """
        self.wait_until_done()
        f = BytesIO()
        storage.download(f"{self.user.user_id}/predict/{self.prediction_id}/predict_proba.csv",
                         f, self.user.id_token)
        f.seek(0)
        result = pd.read_csv(f)
        return result

    @property
    def project(self) -> 'Project':
        return self.model.project

    @property
    def rid(self) -> str:
        return self.prediction_id

    def update(self):
        """
        update name, status
        """
        try:
            document = self._document
        except NotFound:
            raise InvalidID('Given Prediction ID is not found')

        if document['mid'] != self.model.model_id:
            raise InvalidID('Given Prediction ID is not for this model')

        self.name = document['name']
        self.status = Status(document['status'])

        logger.info(f"Prediction '{self.name}': {self.status.value}")

    @property
    def user(self) -> 'User':
        return self.model.project.user

    def wait_until_done(self):
        """
        Wait until ForecastFlow finish prediction.
        """
        while self.status != Status.COMPLETED \
                and self.status != Status.ERROR:
            self.update()
            time.sleep(5)

        if self.status == Status.ERROR:
            document = self._document
            error_info = document.get('errorInfo')
            if error_info is None:
                raise OperationFailed("Predictor quit with Error")
            else:
                raise OperationFailed(f"{error_info['message']}\n"
                                      f"error_log_id: {error_info['errorLogId']}")
