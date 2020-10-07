from pymongo import MongoClient
import datetime
import sys

from bson.objectid import ObjectId

global con
global db
global col

def connect_db():
	global con
	global db
	global col
	con = MongoClient('mongodb+srv://test:test@cluster0.kw4id.mongodb.net/nexus?retryWrites=true&w=majority')
	db = con.nexus
	col = db.memorecords


#icollection installation_companies
def get_memorecords():
	global col
	connect_db()
	memo_records_data_from_db = col.find({})
	return memo_records_data_from_db


def save_memorecords(memo_records):
	global col
	connect_db()
	col.insert(memo_records)
	return
