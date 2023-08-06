from collections import OrderedDict
from typing import TYPE_CHECKING

import forecastflow
from forecastflow.api.v3 import create_prediction
from forecastflow.exceptions import InvalidID
from forecastflow.firebase_api import cloud_firestore
from forecastflow.firebase_api.exceptions import NotFound

if TYPE_CHECKING:
    from forecastflow import DataSource, Prediction, Project, User


class Model:
    """
    ForecastFlow model object
    """

    def __init__(self, project: 'Project', model_id: str):
        """
        Instantiate object with given model ID.

        Args:
            project:
                Project which model belong to.

            model_id:
                ID of model you want to open.
        """
        self.project = project
        self.model_id = model_id
        self._predictions = {}

        try:
            document = self._document
        except NotFound:
            raise InvalidID('Given Mode ID is not found')
        self.name = document['name']
        self.status = document['status']

    def create_prediction(self, data_source: 'DataSource',
                          name: str, description: str = '') -> 'Prediction':
        """
        Create prediction with data_source.

        Args:
            data_source:
                Data to predict with.

            name:
                Name of predict.

            description:
                Description of predict.

        Returns:
            ForecastFlow prediction object which predicts with given data.
        """
        data_source.wait_until_done()
        prediction_id = create_prediction(self.project.user.id_token, name, description,
                                          self.project.project_id, data_source.data_source_id, self.model_id)
        self._predictions[prediction_id] = forecastflow.Prediction(self, prediction_id)
        return self._predictions[prediction_id]

    @property
    def _document(self) -> dict:
        """
        Returns:
            A document of this model on database
        """
        doc = cloud_firestore.get(f'users/{self.user.user_id}/projects/{self.project.project_id}'
                                  f'/models/{self.model_id}', self.user.id_token)
        return doc['fields']

    def get_prediction(self, prediction_id: str) -> 'Prediction':
        """
        Get prediction object with given ID.

        Args:
            prediction_id:
                ID of predict you want.
        Returns:
            ForecastFlow predict object with given ID.
        """
        if prediction_id not in self._predictions:
            self._predictions[prediction_id] = forecastflow.Prediction(self, prediction_id)
        return self._predictions[prediction_id]

    @property
    def mid(self) -> str:
        return self.model_id

    @property
    def prediction_schema(self) -> OrderedDict:
        """
        Returns:
            OrderedDict which maps column name to type string like 'float'.

        Notes:
            You want to use forecastflow.util.parse_type if you need native Python type.
        """
        schema_json = self._document['predictionSchema']  # [{key: type}, ...]
        schema = OrderedDict()
        for column in schema_json:
            key = list(column.keys())[0]
            type_ = column[key]
            schema[key] = type_
        return schema

    @property
    def user(self) -> 'User':
        return self.project.user
