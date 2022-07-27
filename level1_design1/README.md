# MUX Verification

## Verification Environment

- Input - Drive all the inputs to one of the possible logic values. Here all the inputs with the value ```01```.

```python
dut.inp0.value = 01
dut.inp1.value = 01
dut.inp2.value = 01
dut.inp3.value = 01
dut.inp4.value = 01
dut.inp5.value = 01
dut.inp6.value = 01
...
...
...
dut.inp27.value = 01
dut.inp28.value = 01
dut.inp29.value = 01
dut.inp30.value = 01
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

- use ```try..except``` block to prevent program halt during AssertionError

```python
try:
    assert dut.out.value == 1, "MUX failed with select = {SEL}".format(SEL=dut.sel.value)
except AssertionError:
    dut._log.info("MUX failed with select = {SEL}".format(SEL=dut.sel.value))
    continue
```

## Test Scenario

- Without **try..except** block
  
![image](https://user-images.githubusercontent.com/66086031/180064990-242d8b32-2bdc-41c5-b43d-174dc762cdb8.png)

- With **try..except** block

![image](https://user-images.githubusercontent.com/66086031/180252261-2d36bf66-1cc6-45c0-8157-d877f01a503b.png)

> Output mismatch is observed for the following select values
>
> - 01100
> - 11110

## Design Bug

## Fixed Design

- After fixing the bugs, the verification is carried out again.
- Here the DUT Output matches with the expected output from the python model.

![image](https://user-images.githubusercontent.com/66086031/180254497-96830231-e4cb-4b2e-9a2f-3cbd284753a8.png)

## Verification Strategy

- In this verification plan, we basically drove the all input ports to one of the possible values. Let's say ```x```.
- Then we route the inputs to the outputs by looping thorugh the select values.
- If the output does not match the value ```x```, then either the input is **stuck-at** a value or the **select line** is **NOT** properly assigned.

## Is the Verification complete?

- Here we use try..except block to simulate all the inputs.
- We print the error when there is a functional mismatch.


