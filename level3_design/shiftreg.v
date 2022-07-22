/***
Module Name: 16-bit Shift Register
Description: Performs load, and right shift operation
***/

module shiftreg (output reg [15:0] data_out, input [15:0] data_in, input s_in, clk, ld, clr, sft);
// output, input1, signbit, clk, ld, clr, sft

    always @(posedge clk)   begin
        if (clr) 
            data_out <= 15'b0;
        else if (ld)
            data_out <= data_in;
        else if (sft)
            data_out <= {s_in, data_out[15:1]};
    end

endmodule