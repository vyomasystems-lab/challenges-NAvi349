# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge


def subseq(bit, input_seq):

    """
    Finds the 1011 sub-sequence in the input sequence.
    If found it will until the last before bit
    Suppose 1010110 is detected, then the sequence now is 10
    This is help us to detect overlapping 1011 patterns
    """
    #print(input_seq)    

    if ('1011' in input_seq):
        pos = input_seq.find('1011')
        input_seq = input_seq[(pos+3):]
        #print("new str = " + input_seq)
        return [1, input_seq]
    else:
        return 0

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    input_seq = str()

    for times in range(0, 10):
        bit = random.randint(0, 1)


        
        input_seq = input_seq + str(bit)

        [detect_out, input_seq] = subseq(bit, input_seq)

        dut.inp_bit.value = bit

        await FallingEdge(dut.clk)

        dut._log.info(f'inp_bit = {dut.inp_bit.value} expected_output={detect_out} DUT = {dut.seq_seen.value}')


