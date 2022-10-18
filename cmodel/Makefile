GCC=gcc

HEADER=gmp.h xfft_v9_1_bitacc_cmodel.h

XIL_EXAMPLE_SRC=run_bitacc_cmodel.c 
XIL_EXAMPLE=run_fft_example

REAL_SIG_SRC=real_sig_test.c
REAL_SIG=run_real_sig

xfft_out.txt: $(REAL_SIG) ysig.txt
	LD_LIBRARY_PATH=$$LD_LIBRARY_PATH:. ./$(REAL_SIG)


ysig.txt: xil_gen_sig.py
	python $<

$(REAL_SIG): $(HEADER) $(REAL_SIG_SRC)
	g++ -std=c++11 -I. -L. -lgmp -Wl,-rpath,. $(REAL_SIG_SRC) -o $@ -lIp_xfft_v9_1_bitacc_cmodel

Xil_test: $(XIL_EXAMPLE) 
	LD_LIBRARY_PATH=$$LD_LIBRARY_PATH:. ./$(XIL_EXAMPLE)
	touch $@

$(XIL_EXAMPLE): $(HEADER) $(XIL_EXAMPLE_SRC)
	g++ -std=c++11 -I. -L. -lgmp -Wl,-rpath,. $(XIL_EXAMPLE_SRC) -o $@ -lIp_xfft_v9_1_bitacc_cmodel

clean:
	-rm $(XIL_EXAMPLE)
	-rm $(REAL_SIG)
	-rm Xil_test
	-rm Real_sig
	-rm xfft_out.txt
