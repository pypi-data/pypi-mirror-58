from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.scrollview import ScrollView
from kivy.uix.progressbar import ProgressBar
from kivy.uix.slider import Slider
from functools import partial
from gui.DraggableScrollbar import *
from nsz.gui.GuiPath import *


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
								 RecycleBoxLayout):
	''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, GridLayout):
	''' Add selection support to the Label '''
	index = None
	selected = BooleanProperty(False)
	selectable = BooleanProperty(True)
	cols = 3

	def refresh_view_attrs(self, rv, index, data):
		''' Catch and handle the view changes '''
		self.index = index
		self.filename_text = data['0']
		self.filesize_text = data['1']
		return super(SelectableLabel, self).refresh_view_attrs(
			rv, index, data)

	def on_touch_down(self, touch):
		''' Add selection on touch down '''
		if super(SelectableLabel, self).on_touch_down(touch):
			return True
		if self.collide_point(*touch.pos) and self.selectable:
			return self.parent.select_with_touch(self.index, touch)

	def apply_selection(self, rv, index, is_selected):
		''' Respond to the selection of items in the view. '''
		if self.selected == is_selected:
			return
		self.selected = is_selected
		if is_selected:
			print("selection changed to {0}".format(rv.data[index]))
		else:
			print("selection removed for {0}".format(rv.data[index]))


class RV(RecycleView):
	def __init__(self, items, **kwargs):
		super(RV, self).__init__(**kwargs)
		self.refresh(items)
		
	def refresh(self, items):
		self.data = []
		for item in items:
			self.data.append({'0': item[0], '1': self.sizeof_fmt(item[1])})
			
	def sizeof_fmt(self, num, suffix='B'):
		for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
			if abs(num) < 1024.0:
				return "%3.1f %s%s" % (num, unit, suffix)
			num /= 1024.0
		return "%.1f%s%s" % (num, 'Yi', suffix)

class GameList(StackLayout):

	recycleView = None
	draggableScrollbar = None

	def __init__(self, **kwargs):
		Builder.load_file(getGuiPath('layout/GameList.kv'))
		super(GameList, self).__init__(**kwargs)
		self.recycleView = RV([])
		self.draggableScrollbar = DraggableScrollbar(self.recycleView)
		self.add_widget(self.draggableScrollbar)
		self.id = "gameList"

	def refresh(self, items):
		self.draggableScrollbar.slider.opacity = int(len(items)>20)
		self.recycleView.refresh(items)

	def scroll_change(self, recycleView, instance, value):
		recycleView.scroll_y = value

	def slider_change(self, s, instance, value):
		if value >= 0:
		#this to avoid 'maximum recursion depth exceeded' error
			s.value=value

if __name__ == '__main__':
	TestApp().run()
