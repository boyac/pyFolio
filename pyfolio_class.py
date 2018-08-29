# -*- coding: utf-8 -*-
# @Author: Boya Chiou
# @Date:   2018-08-23 16:50:08
# @Last Modified by:   Boya Chiou
# @Last Modified time: 2018-08-29 11:31:14

class Performance(object):
	"""docstring for Performance"""
	def __init__(self, benchr=0, benchw=0, benchtotal=0, portr=0, portw=0):
		super(Performance, self).__init__()
		self.benchr = benchr
		self.benchw = benchw
		self.benchtotal = benchtotal
		self.portr = portr
		self.portw = portw


	def allocation_effect(self):
		# positive contribution: OW in sector OP index, UW in sector UP index
		self.sector = (self.portw-self.benchw)*(self.benchr-self.benchtotal)
		return self.sector


	def selection_effect(self):
		# positive contribution: OP benchmark sector
		self.selection = self.portw*(self.portr-self.benchr)
		return self.selection


	def interaction_effect(self):
		# positive contribution: OW in port OP sector, UW in port UP sector
		self.interaction = (self.portw-self.benchw)*(self.portr-self.benchr)
		return self.interaction


	def active_effect(self):
		self.active = self.allocation_effect()+self.selection_effect()+self.interaction_effect() 
		return "{:.2%}".format(active)

	def PME():
		"Public Market Equivalent (PME)"
		#ticker, trade_dt, quantity, unit_cost, cost_basis, start_yr, dt, adj_cost, ticker_return
		#index_close, index_st_close, share_ytd, index_ytd, cum_invst, cum_tic_return
		pass



if __name__ == "__main__":
	#Benchmark S&P500
	#Bechmark segment S&P500 Tech
	#Benchmark return 9%
	#Benchmark weight 7%
	#Benchmark tech return 8%
	#Benchmark tech weight 15%
	#Total benchmark return 7%
	p = Performance(benchr=0.09, benchw=0.07, benchtotal=0.07, portr=0.08, portw=0.15)
	"""
	benchr=0.09
	benchw=0.07
	portr=0.08
	portw=0.15
	benchtotal=0.07
	"""
	print p.allocation_effect()
	print p.selection_effect()
	print p.interaction_effect()
	print p.active_effect()
