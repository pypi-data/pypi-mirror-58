#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0
import logging

from ocean_utils.agreements.service_agreement import ServiceAgreement
from ocean_utils.agreements.service_types import ServiceTypes

logger = logging.getLogger(__name__)


class AssetExecutor:
    """Class representing the call to the brizo executre endpoint."""

    @staticmethod
    def execute(agreement_id, compute_ddo, consumer_account, brizo, index):
        """

        :param agreement_id:
        :param consumer_account:
        :param index:
        :return:
        """
        compute_service = ServiceAgreement.from_ddo(ServiceTypes.CLOUD_COMPUTE, compute_ddo)
        return brizo.execute_service(
            agreement_id, compute_service.service_endpoint, consumer_account
        )
