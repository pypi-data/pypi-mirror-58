import tempfile
from pathlib import Path
from typing import TYPE_CHECKING

import pandas as pd

import forecastflow
from forecastflow.api.v3 import create_data_source
from forecastflow.exceptions import InvalidID
from forecastflow.firebase_api import cloud_firestore
from forecastflow.firebase_api.exceptions import NotFound

if TYPE_CHECKING:
    from forecastflow import DataSource, DataSourceLabel, Model, User


class Project:
    """
    ForecastFlow project class
    """

    def __init__(self, user: 'User', project_id: str):
        """
        Instantiate Project object with given project ID

        Args:
            user:
                Owner of project.

            project_id:
                Project ID you want to open.
        """
        self.user = user
        self.project_id = project_id
        self._data_sources = {}
        self._models = {}

        try:
            document = self._document
        except NotFound:
            raise InvalidID('Given Project ID is not found')

        self.name = document['name']

    @property
    def _document(self) -> dict:
        doc = cloud_firestore.get(f"users/{self.user.user_id}/projects/{self.project_id}",
                                  self.user.id_token)
        return doc['fields']

    def create_data_source(self, data: pd.DataFrame, name: str, label: 'DataSourceLabel',
                           description: str = '') -> 'DataSource':
        """
        Upload file to ForecastFlow and create data source.

        Args:
            data:
                Data to upload.

            name:
                Name of data source. File name is used if omitted.

            label:
                Label of data.

            description:
                Description of data source.

        Returns:
            New data source created.
        """
        if not name.endswith('.csv'):  # TODO: Currently file extension is needed. Store data type in database.
            name += '.csv'
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir = Path(temp_dir)
            temp_path = temp_dir / 'temp.csv'
            data.to_csv(temp_path)
            did = create_data_source(self.user.user_id, self.user.id_token, self.project_id,
                                     temp_path, name, description, label)
        self._data_sources[did] = forecastflow.DataSource(self, did)
        return self._data_sources[did]

    def get_data_source(self, data_source_id) -> 'DataSource':
        """
        Get data source with given data source id.

        Args:
            data_source_id:
                ID of data source you want to open.

        Returns:
            ForecastFlow data source object with given data source ID.
        """
        if data_source_id not in self._data_sources:
            d = forecastflow.DataSource(self, data_source_id)
            self._data_sources[data_source_id] = d
        return self._data_sources[data_source_id]

    def get_model(self, model_id) -> 'Model':
        """
        Get model with given model ID.

        Args:
            model_id:
                ID of model you want to open.

        Returns:
            ForecastFlow model object with given model ID.
        """
        if model_id not in self._models:
            self._models[model_id] = forecastflow.Model(self, model_id)
        return self._models[model_id]

    @property
    def pid(self) -> str:
        return self.project_id
