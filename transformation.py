#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Contains the base class for transformating one problem to another."""
import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Transformation:
    """Base class for a transformation."""

    @abc.abstractmethod
    def apply(self, problem):
        """Applythe transformation on a problem."""
        raise NotImplementedError()

    @abc.abstractmethod
    def revert(self, problem):
        """Revert the transformation on the problem's output."""
        raise NotImplementedError()
