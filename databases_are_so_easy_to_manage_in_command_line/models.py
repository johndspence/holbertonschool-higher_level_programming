import peewee

my_models_db = peewee.SqliteDatabase("my_models.db",
	pragmas=(('foreign_keys', True),))

class BaseModel(peewee.Model):

	class Meta:
		database = my_models_db
		order_by = ('id',)

class School(BaseModel):
	name = peewee.CharField(128, null = false)
	def __str__(self):
		return "School: %s (%d)" % (self.name, self.id)

class Batch(BaseModel):
	name = peewee.CharField(128, null = false)
	school = peewee.ForeignKeyField(School,
		related_name="batches", on_delete="CASCADE")
	def __str__(self):
		return "Batch: %s (%d)" % (self.name, self.id)

class User(BaseModel):
	first_name = peewee.CharField(128, default="")
	last_name = peewee.CharField(128, null=false)
	age = peewee.IntegerField(null=false)
	def __str(self):
		return "User: %s %s (%d)" % (self.first_name, self.last_name, self.id)

class Student(User):
	batch = peewee.ForeignKeyField(Batch,
		relate_name="students" on_delete="CASCADE")
	def __str(self):
		return "Student: %s %s (%d) part of the batch: %s"
		% (Student.first_name, Student.last_name, self.id, Batch.batch)
