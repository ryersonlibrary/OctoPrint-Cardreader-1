# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import evdev

class CardreaderPlugin(octoprint.plugin.EventHandlerPlugin):
	def __init__(self):
		self.isPrinting = None
	def on_after_startup(self):
		self.isPrinting = False
		devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
		for device in devices:
			self._logger.info(device.fn + "\t" + device.name + "\t" +  device.phys)

	def on_event(self, event, payload):
		if event == "PrinterStateChanged":
			if payload['state_id'] == 'PRINTING':
				if self.isPrinting == False:
					self._printer.pause_print()
					self.isPrinting = True
				else :
					self._printer.resume_print()
			if payload['state_string'] == 'OPERATIONAL':
				self.isPrinting = False
						
__plugin_name__ = "Cardreader Plugin"
__plugin_implementation__ = CardreaderPlugin()

