#!/usr/bin/env python
# -*- coding: utf-8  -*-

class StorageExistedError(Exception):

	def __init__(self, location):
		self.location = location

class StorageNotFoundError(Exception):
	'''
	Storage不存在异常
	'''
	def __init__(self, location):
		self.location = location

class UnmatchExtensionError(Exception):
	'''
	未匹配的扩展异常
	'''
	def __init__(self, extname):
		self.extname = extname

class ForeignRelationExistedError(Exception):

	def __init__(self, location):
		self.location = location

class ArgumentAbsenceError(Exception):
	'''
	参数不存在异常
	'''
	def __init__(self, argname):
		self.argname = argname

class ArgumentTypeError(Exception):
	'''
	参数数据类型错误异常
	'''
	def __init__(self, argname):
		self.argname = argname
