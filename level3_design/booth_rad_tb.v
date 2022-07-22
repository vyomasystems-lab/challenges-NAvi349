module booth_rad_tb;

    // Inputs
    reg clk;
    reg [15:0] data_in;
    reg start;

    // Outputs
    wire done;

    booth_rad uut (
        .done(done),
        .clk(clk),
        .data_in(data_in),
        .start(start)
    );

    initial begin
        clk = 0;
        start = 0;
        data_in = 16'b0;

        #100

        #10
        start = 1; 
        
        #10
        data_in = 16'b1111111111110110; // -10

        #10
        data_in = 16'b0000000000001101; // 13

        #100
        $finish;

    
    
    end

    initial begin
        $dumpfile ("booth_rad.vcd");
        $dumpvars (0, booth_rad_tb);
        $monitor(done);
    end

    always begin
    
    #5 clk = ~clk;
    
    end

endmodule