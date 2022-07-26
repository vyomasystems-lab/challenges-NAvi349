module booth_top(output wire [15:0] out, output done, input clk, input [15:0] data_in, input start);

    

    wire ldA, clrA, sftA, ldQ, clrQ, sftQ, ldM, clrff, addsub;
    wire q0, qm1, dec, ldCnt;
    wire eqz;
    wire [15:0] A, M, Q;

    assign out = {{6{A[4]}}, A[4:0], Q[15:11]};

    booth_datapath bd0 ( clk, ldA, ldM, ldQ, clrA, clrQ, clrff, sftA, sftQ, addsub, dec, ldCnt, data_in, q0, qm1, eqz, A, M, Q);
    booth_controller bc0 ( ldA, clrA, sftA, ldQ, clrQ, sftQ, ldM, clrff, addsub, dec, ldCnt, done, clk, q0, qm1, eqz, start);

endmodule