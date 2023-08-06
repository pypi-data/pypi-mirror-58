import logging
from typing import TYPE_CHECKING

import pandas as pd

from forecastflow.tabpy_support.prep_type import PrepType

if TYPE_CHECKING:
    from forecastflow import User


logger = logging.getLogger(__name__)


def make_prediction_schema(user: 'User', project_id: str, model_id: str):
    """
    Make schema for Tableau Prep's get_output_schema function for prediction

    Args:
        user:
            ForecastFlow User object

        project_id:
            ForecastFlow Project ID

        model_id:
            ForecastFlow Model ID

    Returns:
        A function which returns a schema for Tableau Prep.
    """

    def _get_prediction_schema():
        model = user.get_project(project_id) \
            .get_model(model_id)
        schema_dict = model.prediction_schema.copy()

        for key in schema_dict:
            type_str = schema_dict[key]
            if type_str == 'float':
                prep_type = PrepType.DECIMAL
            elif type_str == 'int':
                prep_type = PrepType.INT
            elif type_str == 'str':
                prep_type = PrepType.STR
            elif type_str == 'bool':
                prep_type = PrepType.BOOL
            else:
                raise ValueError(f"Unsupported type '{type_str}'.")
            schema_dict[key] = [prep_type.value]

        prep_schema = pd.DataFrame(schema_dict)
        logger.info(f'prediction schema:\n{prep_schema}')
        return prep_schema

    return _get_prediction_schema
