//exclude_bug.c
//return how many DWs disappeared at the specified magnet fields

//the format of data files must be
//	View_Overall# Iteration DAQ-X Pulse_Amp Field #DWs
//	and the first line of the files must be column names above

//the numbers of data files are all recgnized as real numbers, not integer 	
//Output is #ViewOverall that has bugs for results

#include <stdio.h>

int main(int argc, char** argv) {
	FILE *fp_in;
	char *InputFileName;
	
	double data[6];
	double VOA_now = 0.0;

	char dust[8][100];	//for non-substitution fscanf

	if (argc != 2) {
		printf("Usage: %s InputFileName \n", argv[0]);
		return 0;
	}
	InputFileName = argv[1];

	fp_in = fopen(InputFileName, "r");
	if (fp_in == NULL) {
		printf("Can't open file %s\n", InputFileName);
		return 0;
	}

	fscanf(fp_in, "%s %s %s %s %s %s %s %s\n", dust[0], dust[1], dust[2], dust[3], dust[4], dust[5], dust[6], dust[7]);

	while (fscanf(fp_in, "%lf %lf %lf %lf %lf %lf\n", &data[0], &data[1], &data[2], &data[3], &data[4], &data[5]) != EOF) {
		if ((data[0] + 0.1) < VOA_now) {
			printf("bug in ViewOverall %lf\n", VOA_now);
		}
		VOA_now = data[0];
	}

	fclose(fp_in);
}





