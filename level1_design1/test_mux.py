# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2 where we test a single input"""

    cocotb.log.info('##### CTB: Develop your test here ########')

    input_port = str(dut.inp)+str(dut.sel.value)

    dut.inp12.value = 1;

    assert dut.out.value == dut.inp12.value, "MUX failed with input = {inp12}, select = {SEL}".format(
            inp12=dut.inp12.value, SEL=dut.sel.value)

    
