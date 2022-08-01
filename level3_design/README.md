# Radix - 2 Booth Multiplier

GitHub Link: [Click here](https://github.com/NAvi349/rad-2-booth)

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

![image](https://user-images.githubusercontent.com/66086031/182075813-d88ba85a-9380-4a6a-83c0-1ca91804af67.png)

![image](https://user-images.githubusercontent.com/66086031/182075916-b0891db5-ff3c-4be6-9303-0129d84f1d39.png)

## Verification Strategy

Multiply the multiplicand and the mulitplier and compare it with the DUT's output.

## Verification Completeness

The DUT has been test for both signed and unsigned integers.
