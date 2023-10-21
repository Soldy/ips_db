import unittest
import sys
import os
import pytest
import directory as d
import mariadblib as m
import hnyconfig as config


def test_init():
    m.initMigrationTable()
def test_createTable():
    m.buildTable()
def test_createFunction():
    m.buildFunction()
def test_createView():
    m.buildView()
def test_destroy():
    m.destroy()
