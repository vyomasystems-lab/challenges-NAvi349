module counter (output reg [4:0] count, input dec, clk, ldCnt);

    always @(posedge clk) begin
        if (ldCnt)
            count <= 5'b00101;
            
        else if (count != 0) begin
            if (dec)
                count <= count - 1;
        end

        else
            count <= count;
        
    end

endmodule
//counter c0 (count, dec, clk, ldCnt);