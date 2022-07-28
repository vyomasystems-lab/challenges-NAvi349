# 1011 Sequence Detector

This sequence detector will detect *overlapping non-sequences* of the pattern ```1010```.

## Verification Environment

### Input test pattern generation

- We generate a random pattern of 0s and 1s and store it in a string.
- We pass this string to the python model.

```py
for times in range(0, 30):
    bit = random.randint(0, 1)
    org_seq = org_seq + str(bit)    # full input_sequence
    
    input_seq = input_seq + str(bit) # input sequence after removing detected sequences
    

    detect_out = subseq(bit, input_seq)  # detect sequence 1011
    input_seq = format_seq(input_seq)

    dut.inp_bit.value = bit  # input bit

    await FallingEdge(dut.clk)   # wait for next clock edge after giving input
     
```

- We compare the output of the DUT with the output of the python model.

```python
    assert detect_out == dut.seq_seen.value, "FSM failed for the input sequence = {seq}".format(seq = org_seq)
```

### Python Model to detect 1011 Sequence

- This function (model) returns `1` whenever `1011` pattern is detected.

```python
def subseq(bit, input_seq):

    """
    Finds the 1011 sub-sequence in the input sequence.
    Suppose 1010110 is detected, then the sequence now is 0
    """
    #print(input_seq)    

    if ('1011' in input_seq):
        return 1
    else:
        return 0
```

- After a detect a `1011` sequence, we remove *except the last bit*.
- So, this facilitates the detection of overlapping non-sequences.
- This `1` bit can be the beginning of the next valid sequence.

```python
def format_seq(input_seq):
    
    if ('1011' in input_seq):
        pos = input_seq.find('1011')
        input_seq = input_seq[(pos+4):]  # remove the valid sequence after it is detected       
    
    return input_seq
```

## Test Scenario

- Here, we can see that the DUT succesfully detects `1011` pattern.
- **But**, it is not able to identify `1011` if it is preceded by `1`.

![image](https://user-images.githubusercontent.com/66086031/180468040-63e96875-d569-4d37-a462-117dd348e9b4.png)

## Design Bug

### State Diagram

### Bug Identification

```verilog
SEQ_1:
begin
if(inp_bit == 1)
    next_state = IDLE; // should stay in SEQ_1
else
    next_state = SEQ_10;
```

```verilog
SEQ_101:
begin
if(inp_bit == 1)
    next_state = SEQ_1011; 
else
    next_state = IDLE; // should go to SEQ_10
```

### Fixed Version


## Fixed Design

![image](https://user-images.githubusercontent.com/66086031/180466632-027366cc-4fbe-4d43-8ea3-ec0520525595.png)

## Verification Strategy

## Verification Completeness





