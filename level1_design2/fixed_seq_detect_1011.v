// See LICENSE.vyoma for more details
// Verilog module for Sequence detection: 1011

// This is the FIXED Version
module fixed_seq_detect_1011(seq_seen, inp_bit, reset, clk);

  output seq_seen;
  input inp_bit;
  input reset;
  input clk;

  parameter IDLE = 0,
            SEQ_1 = 1, 
            SEQ_10 = 2,
            SEQ_101 = 3,
            SEQ_1011 = 4;

  reg [2:0] current_state, next_state;

  // if the current state of the FSM has the sequence 1011, then the output is
  // high
  assign seq_seen = current_state == SEQ_1011 ? 1 : 0;

  // state transition
  always @(posedge clk)
  begin
    if(reset)
    begin
      current_state <= IDLE;
    end
    else
    begin
      current_state <= next_state;
    end
  end

  // state transition based on the input and current state
  always @(inp_bit or current_state)
  begin
    case(current_state)
      IDLE:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = IDLE;
      end
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;  // this line changed
        else
          next_state = SEQ_10;
      end
      SEQ_10:
      begin
        if(inp_bit == 1)
          next_state = SEQ_101;
        else
          next_state = IDLE; 
      end
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011; 
        else
          next_state = SEQ_10; // this line changed
      end
      SEQ_1011: // this will detect only overlapping non-sequences
      begin
        next_state = IDLE; 
      end
    endcase
  end
endmodule
