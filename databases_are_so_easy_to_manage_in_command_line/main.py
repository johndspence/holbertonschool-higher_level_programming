#!/usr/bin/python

import sys
import models.py

if len(sys.argv) < 2:
	print 'Please enter an action'

if len(sys.argv) > 1:
	if sys.argv[1] not in ['create', 'print', 'insert', 'delete']:
		print 'Undefined action <first argument value>'
	else:
		print str(sys.argv[1])

if sys.argv[1] = 'create':
	create()

if sys.argv[1] = 'print':
	action_print()

if sys.argv[1] = 'delete':
	delete()

def create():
	try:
		School.create_table()
	except peewee.OperationalError:
		pass
	try:
		Batch.create_table()
	except peewee.OperationalError:
		pass
	try:
		User.create_table()
	except peewee.OperationalError:
		pass
	try:
		Student.create_table()
	except peewee.OperationalError:
		pass

def action_print():
	if len(sys.argv) != 3:
		return
	if sys.argv[2] = "school":
		print School
	if sys.argv[2] = "batch"
		print Batch
	if sys.argv[2] = "user"
		print User
	if sys.argv[2] = "student"
		print Student

def insert():
	if len(sys.argv) <= 2:
		return
	if sys.argv[2] = "school":
		print "New School: %s" % (School.create(name = sys.argv[3]))
		return

	if sys.argv[2] = 'batch':
		print "New Batch: %s" % (Batch.create(school_id = sys.argv[3],
		Batch.create(name = sys.argv[4]))
		return

	if sys.argv[2] = 'Student':
		print "New Student: %s"
			% (Student.create(batch_id = sys.argv[4],
			age = sys.argv[5],
			last_name = sys.argv[6],
			first_name = sys.argv[7])
		return

def delete():
	if id
		delete id
		print "Delete: <object to delete>"
	else print "Nothing to delete"
