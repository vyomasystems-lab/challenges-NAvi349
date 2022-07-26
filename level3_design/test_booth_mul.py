import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge



@cocotb.test()
async def test_seq_bug1(dut):
    """Test for booth radix-2 algorithm"""

    clock = Clock(dut.clk, 10, units="ns")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset will be provided by the first state of the DUT
   

    cocotb.log.info('#### CTB: Test Starts ######')
    cocotb.log.info('#### Initializing Data Input ######')
    dut.data_in.value = 0
    dut.start.value = 0
    
    await RisingEdge(dut.clk)   # wait for next clock edge after giving input
    cocotb.log.info('#### Initializing Start State ######')
    cocotb.log.info('start = {dut.start.value}')
    dut.start.value = 1

    await RisingEdge(dut.clk)
    cocotb.log.info('#### Multiplicand ######')
    cocotb.log.info(f'start = {dut.start.value}')

    dut.data_in.value = 0xFFF6  # -10

    await RisingEdge(dut.clk)
    cocotb.log.info('#### Multiplier ######')
    
    dut.data_in.value = 0xD  # 13    

    await RisingEdge(dut.clk)    
    await RisingEdge(dut.clk)    
    await RisingEdge(dut.clk)    
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)  
    await RisingEdge(dut.clk)    
    await RisingEdge(dut.clk)  
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)  
    await RisingEdge(dut.clk)  
    await RisingEdge(dut.clk)  
    
    #130ns
 
    dut._log.info(f'DUT = {dut.done.value}')


    #dut._log.info(f'expected_output = {detect_out} DUT = {dut.seq_seen.value}')        

    #assert detect_out==dut.seq_seen.value, "FSM failed for the input sequence = {seq}".format(seq = org_seq)