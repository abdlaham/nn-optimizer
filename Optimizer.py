
class Optimizer:
	'Optimzer class is responsible for training nn'
	
	def __init__(self, nn, controller):
		self.nn = nn
		self.controller = controller
	
	def optimize(self):
		
		self.controller.init(self.nn)
		
		while self.controller.notDone():
			#compute the needed parameters for optimization
			self.controller.compute()

			#update the weights of nn
			self.controller.update()
			
			