import sublime, sublime_plugin
import random

from .id_number_util import identity

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
			idnum_obj.get_area_name()
		]

		self.insert(edit, regions, "\n".join(data))

	def insert(self, edit, regions, content):
		for region in regions:
			if region.empty():
				self.view.insert(edit, region.begin(), content)
			else:
				self.view.replace(edit, region, content)

