# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from square.http.auth.o_auth_2 import OAuth2


class V1TransactionsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""

    def __init__(self, config, call_back=None):
        super(V1TransactionsApi, self).__init__(config, call_back)

    def list_bank_accounts(self,
                           location_id):
        """Does a GET request to /v1/{location_id}/bank-accounts.

        Provides non-confidential details for all of a location's associated
        bank accounts. This endpoint does not provide full bank account
        numbers, and there is no way to obtain a full bank account number with
        the Connect API.

        Args:
            location_id (string): The ID of the location to list bank accounts
                for.

        Returns:
            list of V1BankAccount: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v1/{location_id}/bank-accounts'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': location_id
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def retrieve_bank_account(self,
                              location_id,
                              bank_account_id):
        """Does a GET request to /v1/{location_id}/bank-accounts/{bank_account_id}.

        Provides non-confidential details for a merchant's associated bank
        account. This endpoint does not provide full bank account numbers, and
        there is no way to obtain a full bank account number with the Connect
        API.

        Args:
            location_id (string): The ID of the bank account's associated
                location.
            bank_account_id (string): The bank account's Square-issued ID. You
                obtain this value from Settlement objects returned.

        Returns:
            V1BankAccount: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v1/{location_id}/bank-accounts/{bank_account_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': location_id,
            'bank_account_id': bank_account_id
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def list_orders(self,
                    location_id,
                    order=None,
                    limit=None,
                    batch_token=None):
        """Does a GET request to /v1/{location_id}/orders.

        Provides summary information for a merchant's online store orders.

        Args:
            location_id (string): The ID of the location to list online store
                orders for.
            order (SortOrder, optional): TThe order in which payments are
                listed in the response.
            limit (int, optional): The maximum number of payments to return in
                a single response. This value cannot exceed 200.
            batch_token (string, optional): A pagination cursor to retrieve
                the next set of results for your original query to the
                endpoint.

        Returns:
            list of V1Order: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v1/{location_id}/orders'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': location_id
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'order': order,
            'limit': limit,
            'batch_token': batch_token
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def retrieve_order(self,
                       location_id,
                       order_id):
        """Does a GET request to /v1/{location_id}/orders/{order_id}.

        Provides comprehensive information for a single online store order,
        including the order's history.

        Args:
            location_id (string): The ID of the order's associated location.
            order_id (string): The order's Square-issued ID. You obtain this
                value from Order objects returned by the List Orders endpoint

        Returns:
            V1Order: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v1/{location_id}/orders/{order_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': location_id,
            'order_id': order_id
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def update_order(self,
                     location_id,
                     order_id,
                     body):
        """Does a PUT request to /v1/{location_id}/orders/{order_id}.

        Updates the details of an online store order. Every update you perform
        on an order corresponds to one of three actions:

        Args:
            location_id (string): The ID of the order's associated location.
            order_id (string): The order's Square-issued ID. You obtain this
                value from Order objects returned by the List Orders endpoint
            body (V1UpdateOrderRequest): An object containing the fields to
                POST for the request.  See the corresponding object definition
                for field details.

        Returns:
            V1Order: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v1/{location_id}/orders/{order_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': location_id,
            'order_id': order_id
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def list_payments(self,
                      location_id,
                      order=None,
                      begin_time=None,
                      end_time=None,
                      limit=None,
                      batch_token=None,
                      include_partial=None):
        """Does a GET request to /v1/{location_id}/payments.

        Provides summary information for all payments taken for a given
        Square account during a date range. Date ranges cannot exceed 1 year
        in
        length. See Date ranges for details of inclusive and exclusive dates.
        *Note**: Details for payments processed with Square Point of Sale
        while
        in offline mode may not be transmitted to Square for up to 72 hours.
        Offline payments have a `created_at` value that reflects the time the
        payment was originally processed, not the time it was subsequently
        transmitted to Square. Consequently, the ListPayments endpoint might
        list an offline payment chronologically between online payments that
        were seen in a previous request.

        Args:
            location_id (string): The ID of the location to list payments for.
                If you specify me, this endpoint returns payments aggregated
                from all of the business's locations.
            order (SortOrder, optional): The order in which payments are
                listed in the response.
            begin_time (string, optional): The beginning of the requested
                reporting period, in ISO 8601 format. If this value is before
                January 1, 2013 (2013-01-01T00:00:00Z), this endpoint returns
                an error. Default value: The current time minus one year.
            end_time (string, optional): The end of the requested reporting
                period, in ISO 8601 format. If this value is more than one
                year greater than begin_time, this endpoint returns an error.
                Default value: The current time.
            limit (int, optional): The maximum number of payments to return in
                a single response. This value cannot exceed 200.
            batch_token (string, optional): A pagination cursor to retrieve
                the next set of results for your original query to the
                endpoint.
            include_partial (bool, optional): Indicates whether or not to
                include partial payments in the response. Partial payments
                will have the tenders collected so far, but the itemizations
                will be empty until the payment is completed.

        Returns:
            list of V1Payment: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v1/{location_id}/payments'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': location_id
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'order': order,
            'begin_time': begin_time,
            'end_time': end_time,
            'limit': limit,
            'batch_token': batch_token,
            'include_partial': include_partial
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def retrieve_payment(self,
                         location_id,
                         payment_id):
        """Does a GET request to /v1/{location_id}/payments/{payment_id}.

        Provides comprehensive information for a single payment.

        Args:
            location_id (string): The ID of the payment's associated
                location.
            payment_id (string): The Square-issued payment ID. payment_id
                comes from Payment objects returned by the List Payments
                endpoint, Settlement objects returned by the List Settlements
                endpoint, or Refund objects returned by the List Refunds
                endpoint.

        Returns:
            V1Payment: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v1/{location_id}/payments/{payment_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': location_id,
            'payment_id': payment_id
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def list_refunds(self,
                     location_id,
                     order=None,
                     begin_time=None,
                     end_time=None,
                     limit=None,
                     batch_token=None):
        """Does a GET request to /v1/{location_id}/refunds.

        Provides the details for all refunds initiated by a merchant or any of
        the merchant's mobile staff during a date range. Date ranges cannot
        exceed one year in length.

        Args:
            location_id (string): The ID of the location to list refunds for.
            order (SortOrder, optional): TThe order in which payments are
                listed in the response.
            begin_time (string, optional): The beginning of the requested
                reporting period, in ISO 8601 format. If this value is before
                January 1, 2013 (2013-01-01T00:00:00Z), this endpoint returns
                an error. Default value: The current time minus one year.
            end_time (string, optional): The end of the requested reporting
                period, in ISO 8601 format. If this value is more than one
                year greater than begin_time, this endpoint returns an error.
                Default value: The current time.
            limit (int, optional): The approximate number of refunds to return
                in a single response. Default: 100. Max: 200. Response may
                contain more results than the prescribed limit when refunds
                are made simultaneously to multiple tenders in a payment or
                when refunds are generated in an exchange to account for the
                value of returned goods.
            batch_token (string, optional): A pagination cursor to retrieve
                the next set of results for your original query to the
                endpoint.

        Returns:
            list of V1Refund: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v1/{location_id}/refunds'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': location_id
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'order': order,
            'begin_time': begin_time,
            'end_time': end_time,
            'limit': limit,
            'batch_token': batch_token
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def create_refund(self,
                      location_id,
                      body):
        """Does a POST request to /v1/{location_id}/refunds.

        Issues a refund for a previously processed payment. You must issue
        a refund within 60 days of the associated payment.
        You cannot issue a partial refund for a split tender payment. You
        must
        instead issue a full or partial refund for a particular tender, by
        providing the applicable tender id to the V1CreateRefund endpoint.
        Issuing a full refund for a split tender payment refunds all tenders
        associated with the payment.
        Issuing a refund for a card payment is not reversible. For
        development
        purposes, you can create fake cash payments in Square Point of Sale
        and
        refund them.

        Args:
            location_id (string): The ID of the original payment's associated
                location.
            body (V1CreateRefundRequest): An object containing the fields to
                POST for the request.  See the corresponding object definition
                for field details.

        Returns:
            V1Refund: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v1/{location_id}/refunds'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': location_id
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def list_settlements(self,
                         location_id,
                         order=None,
                         begin_time=None,
                         end_time=None,
                         limit=None,
                         status=None,
                         batch_token=None):
        """Does a GET request to /v1/{location_id}/settlements.

        Provides summary information for all deposits and withdrawals
        initiated by Square to a linked bank account during a date range.
        Date
        ranges cannot exceed one year in length.
        *Note**: the ListSettlements endpoint does not provide entry
        information.

        Args:
            location_id (string): The ID of the location to list settlements
                for.
            order (SortOrder, optional): TThe order in which payments are
                listed in the response.
            begin_time (string, optional): The beginning of the requested
                reporting period, in ISO 8601 format. If this value is before
                January 1, 2013 (2013-01-01T00:00:00Z), this endpoint returns
                an error. Default value: The current time minus one year.
            end_time (string, optional): The end of the requested reporting
                period, in ISO 8601 format. If this value is more than one
                year greater than begin_time, this endpoint returns an error.
                Default value: The current time.
            limit (int, optional): The maximum number of payments to return in
                a single response. This value cannot exceed 200.
            status (V1ListSettlementsRequestStatus, optional): Provide this
                parameter to retrieve only settlements with a particular
                status (SENT or FAILED).
            batch_token (string, optional): A pagination cursor to retrieve
                the next set of results for your original query to the
                endpoint.

        Returns:
            list of V1Settlement: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v1/{location_id}/settlements'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': location_id
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'order': order,
            'begin_time': begin_time,
            'end_time': end_time,
            'limit': limit,
            'status': status,
            'batch_token': batch_token
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def retrieve_settlement(self,
                            location_id,
                            settlement_id):
        """Does a GET request to /v1/{location_id}/settlements/{settlement_id}.

        Provides comprehensive information for a single settlement.
        The returned `Settlement` objects include an `entries` field that
        lists
        the transactions that contribute to the settlement total. Most
        settlement entries correspond to a payment payout, but settlement
        entries are also generated for less common events, like refunds,
        manual
        adjustments, or chargeback holds.
        Square initiates its regular deposits as indicated in the
        [Deposit Options with
        Square](https://squareup.com/help/us/en/article/3807)
        help article. Details for a regular deposit are usually not available
        from Connect API endpoints before 10 p.m. PST the same day.
        Square does not know when an initiated settlement **completes**, only
        whether it has failed. A completed settlement is typically reflected
        in
        a bank account within 3 business days, but in exceptional cases it
        may
        take longer.

        Args:
            location_id (string): The ID of the settlements's associated
                location.
            settlement_id (string): The settlement's Square-issued ID. You
                obtain this value from Settlement objects returned by the List
                Settlements endpoint.

        Returns:
            V1Settlement: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v1/{location_id}/settlements/{settlement_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'location_id': location_id,
            'settlement_id': settlement_id
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result
