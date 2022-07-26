# 1011 Sequence Detector

This sequence detector will detect *overlapping non-sequences* of the pattern ```1010```.

## State Diagram

<!-- ![image](https://user-images.githubusercontent.com/66086031/181807213-096f0bdb-89e5-49d0-8422-bd8671787866.png) -->

```mermaid
%%{init: {'theme':'dark'}}%%
stateDiagram-v2
    IDLE --> SEQ_1 : 1
    IDLE --> IDLE : 0
    
   
   SEQ_1 --> SEQ_1 : 1
   SEQ_1 --> SEQ_10 : 0
   SEQ_10 --> SEQ_101 : 1
   SEQ_10 --> IDLE : 0
   SEQ_101 --> SEQ_1011 : 1
   SEQ_101 --> SEQ_10 : 0

   SEQ_1011 --> IDLE

```

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

- After a detect a `1011` sequence, we remove the subsequence.
- This facilitates the detection of overlapping non-sequences.

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

- If the input bit is `1`, in the **SEQ_1 state**, it should **remain** in the state.

```verilog
SEQ_1:
begin
if(inp_bit == 1)
    next_state = SEQ_1;  // this line changed
else
    next_state = SEQ_10;
```

```verilog
SEQ_101:
begin
if(inp_bit == 1)
    next_state = SEQ_1011; 
else
    next_state = SEQ_10; // this line changed
end
```

## Fixed Design

- Now, the DUT's output matches with the expected output.

![image](https://user-images.githubusercontent.com/66086031/180466632-027366cc-4fbe-4d43-8ea3-ec0520525595.png)

## Verification Strategy

- In the test plan, we basically fed a random pattern of `0`s and `1`s and stored them in a string.
- We then use a python function, detect the `1011` pattern in the string.
- Using this, we were able to verify the DUT's output.
- After we detect the pattern, we remove it from the string, so we can detect overlapping non-sequences.

## Verification Completeness

- The test pattern generation is run a few times to test all possible combination of input test vectors.
