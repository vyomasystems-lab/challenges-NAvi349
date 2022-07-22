/****
Module Name: Parallel Input Parallel Output Register
Description: This a register with parallel load and parallel output
****/


module pipo (output reg [15:0] data_out, input [15:0] data_in, input clk, load);
// output, data_in
    always @(posedge clk) begin
        if (load) data_out <= data_in;
    end
endmodule
