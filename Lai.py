import sublime, sublime_plugin
import random
import time

from datetime import datetime
from .id_number_util import identity

class LaiTimestampToDatetime(sublime_plugin.TextCommand):
	def run(self, edit):
		regions = self.view.sel()
		for region in regions:
			if not region.empty():
				# Get the selected text
				ts = int(self.view.substr(region))
				dt = datetime.fromtimestamp(ts)
				self.view.replace(edit, region, str(dt))

class LaiDatetimeToTimestamp(sublime_plugin.TextCommand):
	def run(self, edit):
		regions = self.view.sel()
		for region in regions:
			if not region.empty():
				# Get the selected text
				dt = self.view.substr(region)
				ts = time.mktime(datetime.strptime(dt, "%Y-%m-%d %H:%M:%S").timetuple())
				self.view.replace(edit, region, str(int(ts)))

class LaiExec(sublime_plugin.TextCommand):
	def run(self, edit):
		regions = self.view.sel()
		for region in regions:
			if not region.empty():
				# Get the selected text
				code = self.view.substr(region)
				result = eval(code)
				self.view.replace(edit, region, str(result))

class LaiGenUserCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		regions = self.view.sel()

		first_names = ["李", "王", "张", "刘"]
		last_names = ["建国", "海军", "强", "伟", "杰"]
		name = first_names[random.randint(0, 3)] + last_names[random.randint(0, 4)]
		number = identity.IdNumber.generate_id()

		idnum_obj = identity.IdNumber(number)

		data = [
			number,
			name,
			'1' + str(random.randint(1000000000, 9999999999)),
			idnum_obj.get_birthday(),
			idnum_obj.get_area_name(),
			'---',
			'性别：' + str('男' if idnum_obj.get_sex() == 1 else '女'),
			'年龄：' + str(idnum_obj.get_age())
		]

		self.insert(edit, regions, "\n".join(data))

	def insert(self, edit, regions, content):
		for region in regions:
			if region.empty():
				self.view.insert(edit, region.begin(), content)
			else:
				self.view.replace(edit, region, content)

