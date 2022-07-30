import psycopg2
DATABASE_URL='postgres://cirkeiuyissbiu:d7f615f0364124da10bceecc52e92e075f81932be1be342c21ace660e24ff202@ec2-54-228-125-183.eu-west-1.compute.amazonaws.com:5432/d8b1hl94q822qg'
connection = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = connection.cursor()

def createTableUser():
	create_table_query = ''' CREATE TABLE users(
		id_user SERIAL PRIMARY KEY  NOT NULL,
		fb_id VARCHAR NOT NULL,
		state VARCHAR NOT NULL,
		query TEXT

	) '''
	cursor.execute(create_table_query)
	connection.commit()
	print('Table created successfully')

def dropTableUser():
	cursor.execute('DROP TABLE users')
	connection.commit()
	print('Table user deleted')


def alreadyInDb(fb_id):
	select_query = '''SELECT * FROM users WHERE fb_id = %s'''
	cursor.execute(select_query, (fb_id,))
	rslt = cursor.fetchone()
	if rslt is None:
		return False
	return True
# print(alreadyInDb('12'))

def insertUser(fb_id, state='START'):
	cursor.execute('INSERT INTO users(fb_id, state) VALUES (%s,%s)', (fb_id, state))
	connection.commit()
	print('user inserted')
# insertUser('123')

def getAllUser():
	cursor.execute('SELECT * FROM users')
	rslt = cursor.fetchall()
	return rslt

def getState(fb_id):
	cursor.execute('SELECT state FROM users WHERE fb_id = %s', (fb_id,))
	rslt = cursor.fetchall()
	if len(rslt) > 0:
		return rslt[0][0]
	else:
		# insertUser(fb_id)
		return 'START'
def getquery(fb_id):
	select_query = 'SELECT query FROM users WHERE fb_id = %s'
	cursor.execute(select_query, (fb_id,))
	rslt = cursor.fetchone()
	if len(rslt) > 0:
		return rslt[0]
	return None
def updateState(fb_id, state, query=''):
	if alreadyInDb(fb_id):
		if state == 'HOSPITAL':
			update_query = '''UPDATE users SET state = %s, query = %s WHERE fb_id = %s'''
			cursor.execute(update_query, (state,query, fb_id))
		else:
			update_query = '''UPDATE users SET state = %s WHERE fb_id = %s'''
			cursor.execute(update_query, (state, fb_id))
		connection.commit()
	else:
		insertUser(fb_id, state)
	print('State updated to', state)