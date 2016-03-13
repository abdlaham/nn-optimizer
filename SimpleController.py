from ControllerBase import ControllerBase

class SimpleController(ControllerBase):
	
	def __init__(self, learning_rate):
		self.learning_rate = learning_rate

	
	def compute(self, debug = False): pass
		
	def update(self, debug = False):
		self.nn.