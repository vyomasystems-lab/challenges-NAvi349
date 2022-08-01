# Radix - 2 Booth Multiplier

Booth Multiplication is an efficient algorithm for multiplication of signed and unsigned integers. It has comparatively reduced number of clock cycles.

## State Diagram

![image](https://user-images.githubusercontent.com/66086031/179691408-73a11fab-e464-417a-b7f9-8de632db0bb1.png)

## Waveform

![image](https://user-images.githubusercontent.com/66086031/182066823-e114d219-204d-42d4-86ca-45da77920385.png)

## Verification Environment

- Generate random inputs 4-bit.

```python
Multiplicand = random.randint(-2**4, (2**4)-1) 
Multiplier = random.randint(-2**4, (2**4)-1)
Result = Multiplicand * Multiplier
```

- Load the multiplicand and multiplier.

```python
await RisingEdge(dut.clk)

dut.data_in.value = Multiplicand

await RisingEdge(dut.clk)

dut.data_in.value = Multiplier    
```

- Compare the output of the DUT and the expected output.

```python
await Timer(120, units="ns")
out = dut.out.value.signed_integer
dut._log.info(f"Expected value = {Result}, DUT value {out}")
assert Result == dut.out.value.signed_integer, f"Expected value{Result} does not match the DUT value{out}"
```

## Test Scenario

![image](https://user-images.githubusercontent.com/66086031/180978310-e033f975-e7f8-4fc7-8574-701fcfce8985.png)

![image](https://user-images.githubusercontent.com/66086031/180978447-f53dc5ba-f114-4b6b-817c-b4cf5e25130a.png)

## Verification Strategy

Multiply the multiplicand and the mulitplier and compare it with the DUt's output.

## Verification Completeness

The DUT has been test for both signed and unsigned integers.
