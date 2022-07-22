module dff (output reg q, input d, clk, clr);
    
    always @(posedge clk) begin
        if (clr) 
            q <= 0;
        else 
            q <= d;
    end
    
endmodule