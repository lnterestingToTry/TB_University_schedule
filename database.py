import mysql.connector

class Database:
	def __init__(self):
		self.connection = mysql.connector.connect(
			  host="localhost",
			  user="root",
			  password="",
			  database="pnu_scheduletestdb"
			)
		self.cursor = self.connection.cursor()
		print("db_initialized")

	def add_user(self, user_id):
		sql = "INSERT INTO users (user_id) VALUES (%s)"
		val = (user_id,)
		self.cursor.execute(sql, val)
		self.connection.commit()


	def user_exists(self, user_id):
		self.cursor.execute("SELECT user_id FROM users WHERE user_id = %s", (user_id,))
		result = self.cursor.fetchall()
		print(len(result))
		return bool(len(result))


	def group_select(self, faculty_id):
		data = self.select('groups_', ['group_id', 'name'], 'faculty_id', faculty_id)
		return data


	def academics_select(self):
		data = self.select('academics', ['first_name', 'second_name', 'middle_name', 'academic_id'], 'is_active', '1')
		return data


	def faculty_select(self):
		sql = f"SELECT faculty_id, name FROM faculty"

		self.cursor.execute(sql)
		result = self.cursor.fetchall()

		return result


	def group_update(self, user_id, group_id):
		sql = f"UPDATE users SET group_id = {group_id} WHERE user_id = {user_id}"

		self.cursor.execute(sql)
		self.connection.commit()


	def select_group_by_user(self, user_id):
		data = self.select('users', ['group_id'], 'user_id', user_id)
		return data


	def select_academic_by_user(self, user_id):
		data = self.select('users', ['academic'], 'user_id', user_id)
		return data


	def academic_update(self, user_id, academic_id):
		sql = f"UPDATE users SET academic_id = {academic_id} WHERE user_id = {user_id}"

		self.cursor.execute(sql)
		self.connection.commit()

	def academic_exists(self, academic_id):
		self.cursor.execute("SELECT academic_id FROM users WHERE user_id = %s", (user_id,))
		result = self.cursor.fetchall()
		print(len(result))
		return bool(len(result))


	def today_select_group(self, group_id):
		sql = f'''SELECT academics.first_name, academics.second_name, groups_.name, audiences.name, disciplines.name, timestamps_.start_date, timestamps_.end_date, timestamps_.date_
					FROM schedule
					inner JOIN academics ON schedule.academic_id = academics.academic_id
					inner JOIN groups_ ON schedule.group_id = groups_.group_id
					inner JOIN audiences ON schedule.audience_id = audiences.audience_id
					inner JOIN disciplines ON schedule.discipline_id = disciplines.discipline_id
					inner JOIN timestamps_ ON schedule.timestamp_id = timestamps_.timestamp_id
					WHERE DATE(date_) = CURDATE();

					'''

		self.cursor.execute(sql)
		result = self.cursor.fetchall()

		return result


	def insert(self, table, fields, values):
	    field_line = ", ".join(fields)
	    val = ", ".join(["%s"] * len(values))

	    sql = f"INSERT INTO {table} ({field_line}) VALUES ({val})"

	    self.cursor.execute(sql, values)
	    self.connection.commit()


	def select(self, table, fields, where_field, where_value):
		select_line = ""
		for field in fields:
			select_line = ", ".join(fields)

		sql = f"SELECT {select_line} FROM {table} WHERE {where_field} = %s"
		val = (where_value,)

		self.cursor.execute(sql, val)
		result = self.cursor.fetchall()

		return(result)


	def update(self, table, fields, values, where_field, where_value): #fields= [] values = [];  len(fields) = len(values)
		set_line = ""
		#index = 0
		for field, value in zip(fields, values):
			set_line += f"{field} = '{value}', "

		set_line = set_line.rstrip(", ")


		print(set_line)
		#print(where_value)

		sql = f"UPDATE {table} SET {set_line} WHERE {where_field} = {where_value}"
		print(sql)
		self.cursor.execute(sql)
		self.connection.commit()