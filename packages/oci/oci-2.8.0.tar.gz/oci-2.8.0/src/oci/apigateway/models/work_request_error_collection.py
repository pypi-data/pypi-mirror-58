# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestErrorCollection(object):
    """
    Collection of work request errors.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestErrorCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this WorkRequestErrorCollection.
        :type items: list[WorkRequestError]

        """
        self.swagger_types = {
            'items': 'list[WorkRequestError]'
        }

        self.attribute_map = {
            'items': 'items'
        }

        self._items = None

    @property
    def items(self):
        """
        **[Required]** Gets the items of this WorkRequestErrorCollection.
        Work request errors.


        :return: The items of this WorkRequestErrorCollection.
        :rtype: list[WorkRequestError]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this WorkRequestErrorCollection.
        Work request errors.


        :param items: The items of this WorkRequestErrorCollection.
        :type: list[WorkRequestError]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
