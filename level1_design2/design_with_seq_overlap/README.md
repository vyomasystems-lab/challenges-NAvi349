# This folder contains the design which will work for overlapping valid-sequences

<!-- ![image](https://user-images.githubusercontent.com/66086031/180295189-930832ff-3515-42e5-ac15-293d220d49b3.png)
![image](https://user-images.githubusercontent.com/66086031/180295250-f755067b-1af8-4f6b-8966-f58b0546a8c2.png)
![image](https://user-images.githubusercontent.com/66086031/180295434-3f43ca5b-75a9-4fd1-b9e1-6a03751be15b.png)
![image](https://user-images.githubusercontent.com/66086031/180295545-e4fa6348-67bb-40e3-88ea-58f619b23030.png) -->

![image](https://user-images.githubusercontent.com/66086031/180470867-8c2025d1-1a31-4178-a57c-8189526b9e6c.png)

## Python Model

- Whenever, we detect a valid `1011` pattern, we remove it from the input string, except the last `1`.
- This `1` will possibly become the beginning of the next `1011` pattern.

```python
def format_seq(input_seq):

    if ('1011' in input_seq):
        pos = input_seq.find('1011')
        input_seq = input_seq[(pos+3):]  #delete till the last but one. So that it will become part of the next sequence
            
    return input_seq    
```

## Verilog Modifications

```verilog
SEQ_1011: // this will detect overlapping sequences
begin
if(inp_bit == 1)
    next_state = SEQ_1; // if 1 goto SEQ_1 else goto SEQ_10
else
    next_state = SEQ_10;
end
```

## State Diagram

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

    SEQ_1011 --> SEQ_1 : 1
    SEQ_1011 --> SEQ_10 : 0

```

