module booth_datapath ( input clk, ldA, ldM, ldQ, clrA, clrQ, clrff, sftA, sftQ, addsub, dec, ldCnt, input [15:0] data_in, output q0, qm1, eqz);

    wire [15:0] A, M, Q, Z;
    wire [4:0] count;

    assign eqz = ~|count;
    assign q0 = Q[0];

    alu a0 (Z, A, M, addsub);

    // output, input
    dff d0 (qm1, Q[0], clk, clrff);

    // output, input1, signbit, clk, ld, clr, sft
    shiftreg Areg (A, Z, A[15], clk, ldA, clrA, sftA);
    shiftreg Qreg (Q, data_in, A[0], clk, ldQ, clrQ, sftQ);

    // output, data_in
    pipo mreg (M, data_in, clk, ldM);

    // output, input
    counter c0 (count, dec, clk, ldCnt);

endmodule



