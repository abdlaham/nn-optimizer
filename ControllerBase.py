from abc import ABCMeta, abstractmethod

class ControllerBase:
	__metaclass__ = ABCMeta
	
	def init(self, nn):
		self.nn = nn
	
	@abstractmethod
	def compute(self, debug = False): pass
	
	@abstractmethod
	def update(self, debug = False): pass