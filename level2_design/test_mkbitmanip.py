# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from model_mkbitmanip import *

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

# Sample Test
@cocotb.test()
def run_test(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction

    # opening the file in read mode
    my_file = open("imem.txt", "r")
    
    # reading the file
    data = my_file.read()
    
    # replacing end splitting the text 
    # when newline ('\n') is seen.
    mem = data.split("\n")
    mem = [int("0x"+instr, 16) for instr in mem]

    my_file.close()  
      

    for inst in mem:
        mav_putvalue_src1 = 3
        mav_putvalue_src2 = 2
        mav_putvalue_src3 = 0

        
        mav_putvalue_instr = inst


        # expected output from the model
        expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

        # driving the input transaction
        dut.mav_putvalue_src1.value = mav_putvalue_src1
        dut.mav_putvalue_src2.value = mav_putvalue_src2
        dut.mav_putvalue_src3.value = mav_putvalue_src3
        dut.EN_mav_putvalue.value = 1
        dut.mav_putvalue_instr.value = mav_putvalue_instr

        yield Timer(1) 

        # obtaining the output
        dut_output = dut.mav_putvalue.value


        
        # comparison
        error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
        try :
            assert dut_output == expected_mav_putvalue
        except AssertionError:
            cocotb.log.info(f'INSTR={hex(inst)}')
            cocotb.log.info(f'SRC1={hex(mav_putvalue_src1)} SRC2={hex(mav_putvalue_src2)} SRC3={hex(mav_putvalue_src3)}')
            cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
            cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
            print(error_message)

