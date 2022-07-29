# MUX Verification

This MUX has 31 inputs and 5 select lines.

## Verification Environment

- Input - Drive all the inputs to one of the possible logic values. Here all the inputs with the value `1`.

```python
dut.inp0.value = 1
dut.inp1.value = 1
dut.inp2.value = 1
dut.inp3.value = 1
dut.inp4.value = 1
...
...
...
dut.inp27.value = 1
dut.inp28.value = 1
dut.inp29.value = 1
dut.inp30.value = 1
```

- Loop through the select lines

```python
for i in range(0, 31):
    dut.sel.value = i
```

- Check output

```python
assert dut.out.value == 01
```

- use ```try...except``` block to prevent program halt during AssertionError

```python
try:
    assert dut.out.value == 1, "MUX failed with select = {SEL}".format(SEL=dut.sel.value)
except AssertionError:
    dut._log.info("MUX failed with select = {SEL}".format(SEL=dut.sel.value))
    continue
```

## Test Scenario

- Without **try...except** block
  
![image](https://user-images.githubusercontent.com/66086031/180064990-242d8b32-2bdc-41c5-b43d-174dc762cdb8.png)

- With **try...except** block

![image](https://user-images.githubusercontent.com/66086031/180252261-2d36bf66-1cc6-45c0-8157-d877f01a503b.png)

> Output mismatch is observed for the following select values
>
> - 01100
> - 11110

## Design Bug

- There are two bugs in the design:
  - ```inp12``` is not routed to output for select value = ```01100```(12)
  - ```inp30``` is not assigned to output

### Source of the bug

```verilog
5'b01101: out = inp12;   // the select corresponding to inp12 is sel = 5'b01100
...
...
...
5'b11101: out = inp29;    // inp30 is not assigned to the output defaults to zero
```

### Correction

```verilog
5'b01100: out = inp12;   // the select corresponding to inp12 is sel = 5'b01100
...
...
...
5'b11101: out = inp29;  
5'b11110: out = inp30;
```

## Fixed Design

- After fixing the bugs, the verification is carried out again.
- Here the DUT output matches with the expected output from the python model.

![image](https://user-images.githubusercontent.com/66086031/180254497-96830231-e4cb-4b2e-9a2f-3cbd284753a8.png)

## Verification Strategy

- In this verification plan, we basically drove the all input ports to one of the possible values. Let's say ```x```.
- Then we route the inputs to the outputs by looping through the select values.
- If the output does not match the value ```x```, then either the input is **stuck-at** a value or the **select line** is **NOT** properly assigned.

## Is the Verification complete?

- If any of the inputs is stuck at ```01```, it would have gone unnoticed.
- For complete verification, all the input combinations must be given - ```00, 01, 10, 11```.
