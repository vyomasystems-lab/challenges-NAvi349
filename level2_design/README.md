# Bit Manipulation Co-Processor Verification

## Instruction Set Architecture

[Click to view](https://github.com/vyomasystems-lab/challenges-NAvi349/blob/master/level2_design/instructions.png)

## Verification Environment

- `model_mkbitmanip.py` - contains the python model of the processor.
- `Inst_Bin.pdf` - containts the instructions in the binary format.
- `imem.txt` - contains the instructions in the hexadecimal format.
- These instructions are created using the ISA.

```py
my_file = open("imem.txt", "r")

# reading the file
data = my_file.read()

# replacing end splitting the text 
# when newline ('\n') is seen.
mem = data.split("\n")

mem = [int("0x"+instr, 16) for instr in mem]

my_file.close()  
```

- We will feed this instruction to the DUT and the python model and compare the outputs.

```python
mav_putvalue_src1 = random.randint(0, 2**5)
mav_putvalue_src2 = random.randint(0, 2**5)
mav_putvalue_src3 = random.randint(0, 2**5)

mav_putvalue_instr = inst

# expected output from the model
expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)
```

- Whenever an instruction is executed, the name of the instruction is displayed.

## Test Scenario

![image](https://user-images.githubusercontent.com/66086031/180856013-37ba52fb-60b2-4eea-bf09-12d2ef4339a1.png)
![image](https://user-images.githubusercontent.com/66086031/181818636-3b987811-e71d-448d-944b-460337c5ed86.png)
![image](https://user-images.githubusercontent.com/66086031/181818726-ab3e9919-8445-4b3d-a529-cb705f4fbfaa.png)


- We can clearly see that the DUT output of the `ANDN` instruction does not match with the python model.

## Design Bug

### Bug Identification

- The `src2` is not negated.

```verilog
assign x__h39889 = mav_putvalue_src1 & mav_putvalue_src2 ;    
```

```verilog
// ANDN Instruction
assign field1__h109 =
      (mav_putvalue_instr[31:25] == 7'b0100000 &&
       x__h254 == 10'b1110110011) ?
        x__h39889 :
        IF_mav_putvalue_instr_BITS_31_TO_25_EQ_0b10000_ETC___d2273 ;  
```

### Bug Fix

- Create **new** wire and do the proper ANDN operation.
- Modifying `x__h39889` will affect `CMIX` instruction also.

```verilog
// This line added to negate src2 in ANDN to fix error
assign x__h39890 = mav_putvalue_src1 & (~mav_putvalue_src2) ;
```

- Use this in the ANDN instruction.

```verilog
  assign field1__h109 =
      (mav_putvalue_instr[31:25] == 7'b0100000 &&
       x__h254 == 10'b1110110011) ?
        x__h39890 :
        IF_mav_putvalue_instr_BITS_31_TO_25_EQ_0b10000_ETC___d2273 ;
```

<!-- ![image](https://user-images.githubusercontent.com/66086031/180934782-5a6aff44-ed01-4e25-b116-703b300589e5.png) -->

![image](https://user-images.githubusercontent.com/66086031/180934860-cabc21b4-183a-408a-852c-4a36fc58d792.png)

## Fixed Design

![image](https://user-images.githubusercontent.com/66086031/180934921-cba50843-d68d-4a96-8bb8-fbf5a84076ef.png)

## Verfication of other instructions

![image](https://user-images.githubusercontent.com/66086031/180935002-d19d9c03-4df2-45c2-af83-d64a0b07fb2b.png)

![image](https://user-images.githubusercontent.com/66086031/180935052-58fb180a-f4be-4871-a962-1b252d5f50f4.png)

![image](https://user-images.githubusercontent.com/66086031/180935106-bf997be4-0ca0-4810-b8af-a785cd350616.png)

## Verification Strategy

- Basically we create an instruction for each type in binary format.
- Then we convert it to hexadecimal format.
- We feed this hex data into the DUT and compare it with the python model.

## Verification Completeness

- Each instruction is tested seperately.
