# coding: utf-8

"""
    NeoLoad API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class TestDefinition(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'author': 'str',
        'termination_reason': 'str',
        'lg_count': 'int',
        'project': 'str',
        'scenario': 'str',
        'status': 'str',
        'quality_status': 'str',
        'start_date': 'int',
        'end_date': 'int',
        'duration': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'author': 'author',
        'termination_reason': 'terminationReason',
        'lg_count': 'lgCount',
        'project': 'project',
        'scenario': 'scenario',
        'status': 'status',
        'quality_status': 'qualityStatus',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'duration': 'duration'
    }

    def __init__(self, id=None, name=None, description=None, author=None, termination_reason=None, lg_count=None, project=None, scenario=None, status=None, quality_status=None, start_date=None, end_date=None, duration=None, local_vars_configuration=None):  # noqa: E501
        """TestDefinition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._description = None
        self._author = None
        self._termination_reason = None
        self._lg_count = None
        self._project = None
        self._scenario = None
        self._status = None
        self._quality_status = None
        self._start_date = None
        self._end_date = None
        self._duration = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if author is not None:
            self.author = author
        if termination_reason is not None:
            self.termination_reason = termination_reason
        if lg_count is not None:
            self.lg_count = lg_count
        if project is not None:
            self.project = project
        if scenario is not None:
            self.scenario = scenario
        if status is not None:
            self.status = status
        if quality_status is not None:
            self.quality_status = quality_status
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if duration is not None:
            self.duration = duration

    @property
    def id(self):
        """Gets the id of this TestDefinition.  # noqa: E501

        Unique identifier of the test result.  # noqa: E501

        :return: The id of this TestDefinition.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestDefinition.

        Unique identifier of the test result.  # noqa: E501

        :param id: The id of this TestDefinition.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this TestDefinition.  # noqa: E501

        Name of the test result.  # noqa: E501

        :return: The name of this TestDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TestDefinition.

        Name of the test result.  # noqa: E501

        :param name: The name of this TestDefinition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this TestDefinition.  # noqa: E501

        Description of the test result.  # noqa: E501

        :return: The description of this TestDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TestDefinition.

        Description of the test result.  # noqa: E501

        :param description: The description of this TestDefinition.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def author(self):
        """Gets the author of this TestDefinition.  # noqa: E501

        First and Last name of the person who launched the test.  # noqa: E501

        :return: The author of this TestDefinition.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this TestDefinition.

        First and Last name of the person who launched the test.  # noqa: E501

        :param author: The author of this TestDefinition.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def termination_reason(self):
        """Gets the termination_reason of this TestDefinition.  # noqa: E501

        Reason that caused the test to end.  # noqa: E501

        :return: The termination_reason of this TestDefinition.  # noqa: E501
        :rtype: str
        """
        return self._termination_reason

    @termination_reason.setter
    def termination_reason(self, termination_reason):
        """Sets the termination_reason of this TestDefinition.

        Reason that caused the test to end.  # noqa: E501

        :param termination_reason: The termination_reason of this TestDefinition.  # noqa: E501
        :type: str
        """
        allowed_values = ["CANCELLED", "FAILED_TO_START", "POLICY", "VARIABLE", "MANUAL", "LG_AVAILABILITY", "LICENSE", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and termination_reason not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `termination_reason` ({0}), must be one of {1}"  # noqa: E501
                .format(termination_reason, allowed_values)
            )

        self._termination_reason = termination_reason

    @property
    def lg_count(self):
        """Gets the lg_count of this TestDefinition.  # noqa: E501

        Total number of Load Generators used in the test result.  # noqa: E501

        :return: The lg_count of this TestDefinition.  # noqa: E501
        :rtype: int
        """
        return self._lg_count

    @lg_count.setter
    def lg_count(self, lg_count):
        """Sets the lg_count of this TestDefinition.

        Total number of Load Generators used in the test result.  # noqa: E501

        :param lg_count: The lg_count of this TestDefinition.  # noqa: E501
        :type: int
        """

        self._lg_count = lg_count

    @property
    def project(self):
        """Gets the project of this TestDefinition.  # noqa: E501

        Name of the project.  # noqa: E501

        :return: The project of this TestDefinition.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this TestDefinition.

        Name of the project.  # noqa: E501

        :param project: The project of this TestDefinition.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def scenario(self):
        """Gets the scenario of this TestDefinition.  # noqa: E501

        Name of the scenario.  # noqa: E501

        :return: The scenario of this TestDefinition.  # noqa: E501
        :rtype: str
        """
        return self._scenario

    @scenario.setter
    def scenario(self, scenario):
        """Sets the scenario of this TestDefinition.

        Name of the scenario.  # noqa: E501

        :param scenario: The scenario of this TestDefinition.  # noqa: E501
        :type: str
        """

        self._scenario = scenario

    @property
    def status(self):
        """Gets the status of this TestDefinition.  # noqa: E501

        Status of the test result.  # noqa: E501

        :return: The status of this TestDefinition.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TestDefinition.

        Status of the test result.  # noqa: E501

        :param status: The status of this TestDefinition.  # noqa: E501
        :type: str
        """
        allowed_values = ["INIT", "STARTING", "RUNNING", "TERMINATED", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def quality_status(self):
        """Gets the quality_status of this TestDefinition.  # noqa: E501

        Quality status of the test result.  # noqa: E501

        :return: The quality_status of this TestDefinition.  # noqa: E501
        :rtype: str
        """
        return self._quality_status

    @quality_status.setter
    def quality_status(self, quality_status):
        """Sets the quality_status of this TestDefinition.

        Quality status of the test result.  # noqa: E501

        :param quality_status: The quality_status of this TestDefinition.  # noqa: E501
        :type: str
        """
        allowed_values = ["PASSED", "FAILED", "COMPUTING", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and quality_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `quality_status` ({0}), must be one of {1}"  # noqa: E501
                .format(quality_status, allowed_values)
            )

        self._quality_status = quality_status

    @property
    def start_date(self):
        """Gets the start_date of this TestDefinition.  # noqa: E501

        Timestamp when the test started.  # noqa: E501

        :return: The start_date of this TestDefinition.  # noqa: E501
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this TestDefinition.

        Timestamp when the test started.  # noqa: E501

        :param start_date: The start_date of this TestDefinition.  # noqa: E501
        :type: int
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this TestDefinition.  # noqa: E501

        Timestamp when the test ended.  # noqa: E501

        :return: The end_date of this TestDefinition.  # noqa: E501
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this TestDefinition.

        Timestamp when the test ended.  # noqa: E501

        :param end_date: The end_date of this TestDefinition.  # noqa: E501
        :type: int
        """

        self._end_date = end_date

    @property
    def duration(self):
        """Gets the duration of this TestDefinition.  # noqa: E501

        Test duration in seconds.  # noqa: E501

        :return: The duration of this TestDefinition.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TestDefinition.

        Test duration in seconds.  # noqa: E501

        :param duration: The duration of this TestDefinition.  # noqa: E501
        :type: int
        """

        self._duration = duration

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TestDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TestDefinition):
            return True

        return self.to_dict() != other.to_dict()