module booth_rad(output done, input clk, input [15:0] data_in, input start);

    wire ldA, clrA, sftA, ldQ, clrQ, sftQ, ldM, clrff, addsub;
    wire q0, qm1, dec, ldCnt;
    wire eqz;


    booth_datapath bd0 ( clk, ldA, ldM, ldQ, clrA, clrQ, clrff, sftA, sftQ, addsub, dec, ldCnt, data_in, q0, qm1, eqz);
    booth_controller bc0 ( ldA, clrA, sftA, ldQ, clrQ, sftQ, ldM, clrff, addsub, dec, ldCnt, done, clk, q0, qm1, eqz, start);

endmodule