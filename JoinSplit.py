import sublime, sublime_plugin
import re

def my_join(text, separador, trim=False):
	if trim == False:
		return re.sub(r"\n", separador, text)
	else:
		text = re.sub(r"\s*\n\s*", separador, text)
		return re.sub(r"^\s*|\s*$", "", text)

def my_split(text, separador):
	return '\n'.join(text.split(separador))

class LgSplitselCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Separador", "", self.on_input, None, None)

	def on_input(self, command):
		separador = str(command) 
		view_active = self.window.active_view()
		edit = view_active.begin_edit()

		for i, region in enumerate(view_active.sel()):
			view_active.replace(edit, region, '\n'.join(view_active.substr(region).split(separador)))

		view_active.end_edit(edit)

class LgJoinselCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Separador", "", self.on_input, None, None)

	def on_input(self, command):
		separador = str(command) 
		view_active = self.window.active_view()
		edit = view_active.begin_edit()

		for i, region in enumerate(view_active.sel()):
			view_active.replace(edit, region, my_join(view_active.substr(region), separador, False))

		view_active.end_edit(edit)

class LgJoinseltrimCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Separador", "", self.on_input, None, None)

	def on_input(self, command):
		separador = str(command) 
		view_active = self.window.active_view()
		edit = view_active.begin_edit()

		for i, region in enumerate(view_active.sel()):
			view_active.replace(edit, region, my_join(view_active.substr(region), separador, True))

		view_active.end_edit(edit)

class LgRemoverespacosCommand(sublime_plugin.WindowCommand):
	def run(self):
		view_active = self.window.active_view()
		edit = view_active.begin_edit()

		for i, region in enumerate(view_active.sel()):
			view_active.replace(edit, region, re.sub('([ \t])[ \t]{1,}', '\\1', view_active.substr(region)))

		view_active.end_edit(edit)

class LgRemoverquebrasCommand(sublime_plugin.WindowCommand):
	def run(self):
		view_active = self.window.active_view()
		edit = view_active.begin_edit()

		for i, region in enumerate(view_active.sel()):
			view_active.replace(edit, region, re.sub('((\n|\r\n))(\n|\r\n){1,}', '\\1', view_active.substr(region)))

		view_active.end_edit(edit)

class LgRemoverrepetidosCommand(sublime_plugin.WindowCommand):
	def run(self):
		view_active = self.window.active_view()
		edit = view_active.begin_edit()

		for i, region in enumerate(view_active.sel()):
			linhas = view_active.substr(region).split('\n')
			unicos = []
			for linha in linhas:
				linha = re.sub(r"^\s*|\s*$", "", linha)
				if unicos.count(linha) == 0:
					unicos.append(linha)

			view_active.replace(edit, region, '\n'.join(unicos))

		view_active.end_edit(edit)

class LgAgruparcountCommand(sublime_plugin.WindowCommand):
	def run(self):
		view_active = self.window.active_view()
		edit = view_active.begin_edit()

		for i, region in enumerate(view_active.sel()):
			unicos = []
			todos = []
			linhas = view_active.substr(region).split('\n')
			for linha in linhas:
				linha = re.sub(r"^\s*|\s*$", "", linha)
				todos.append(linha)
				if unicos.count(linha) == 0:
					unicos.append(linha)

			resultado = ''
			for idx, linha in enumerate(unicos):
				resultado += "[%d] %s" % (todos.count(linha), linha)
				if len(unicos) != idx + 1:
					resultado += '\n'

			view_active.replace(edit, region, resultado)

		view_active.end_edit(edit)
