import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.triggers import Timer


@cocotb.test()
async def test_seq_1(dut):
    """Test for booth radix-2 algorithm"""

    Multiplicand = random.randint(0, 2**4) 
    Multiplier = random.randint(0, 2**3)
    Result = Multiplicand * Multiplier

    await Timer(10, units="ns")

    clock = Clock(dut.clk, 10, units="ns")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset will be provided by the first state of the DUT 
    

    await RisingEdge(dut.clk)

    cocotb.log.info('#### CTB: Test Starts ######')
    #cocotb.log.info('#### Initializing Data Input ######')
    dut.data_in.value = 0
    dut.start.value = 0
    
    await RisingEdge(dut.clk)   # wait for next clock edge after giving input
    cocotb.log.info('#### Initializing Start State ######')
    cocotb.log.info(f'start = {dut.start.value}')
    dut.start.value = 1

    await RisingEdge(dut.clk)
    cocotb.log.info('#### Loading Multiplicand ######')
    cocotb.log.info(f'start = {dut.start.value}')
    dut.data_in.value = Multiplicand

    await RisingEdge(dut.clk)
    cocotb.log.info('#### Loading Multiplier ######')    
    dut.data_in.value = Multiplier 
 
        
    await Timer(100, units="ns")
    dut._log.info(f'DONE = {dut.done.value}')

    dut._log.info(f"Expected value = {Result} DUT value {int(hex(dut.out.value), 16)}")