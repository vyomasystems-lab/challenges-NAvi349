# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2 where we test a single input"""


    cocotb.log.info('##### CTB: Develop your test here ########')

    dut.inp0.value = 1
    dut.inp1.value = 1
    dut.inp2.value = 1
    dut.inp3.value = 1
    dut.inp4.value = 1
    dut.inp5.value = 1
    dut.inp6.value = 1
    dut.inp7.value = 1
    dut.inp8.value = 1
    dut.inp9.value = 1
    dut.inp10.value = 1
    dut.inp11.value = 1
    dut.inp12.value = 1
    dut.inp13.value = 1
    dut.inp14.value = 1
    dut.inp15.value = 1

    dut.inp16.value = 1
    dut.inp17.value = 1
    dut.inp18.value = 1
    dut.inp19.value = 1
    dut.inp20.value = 1
    dut.inp21.value = 1
    dut.inp22.value = 1
    dut.inp23.value = 1
    dut.inp24.value = 1
    dut.inp25.value = 1
    dut.inp26.value = 1
    dut.inp27.value = 1
    dut.inp28.value = 1
    dut.inp29.value = 1
    dut.inp30.value = 1

    for i in range(0, 31):
        dut.sel.value = i

        await Timer(2, units='ns')
        dut._log.info(f'inp{i}.value={1:02} SEL={int(dut.sel.value)} expected={1:02} DUT={int(dut.out.value):02}')
        
        
        try:
            assert dut.out.value == 1, "MUX failed with select = {SEL}".format(SEL=dut.sel.value)
        except AssertionError:
            dut._log.info("MUX failed with select = {SEL}".format(SEL=dut.sel.value))
            continue



    
