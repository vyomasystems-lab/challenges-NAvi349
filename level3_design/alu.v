module alu  (output reg [15:0] out, input [15:0] in1, input [15:0] in2, input addsub);

    always @(*) begin
        if (addsub == 0) 
            out = in1 - in2; // 10 means sub
        else 
            out = in1 + in2; // 01 - add
    end
endmodule