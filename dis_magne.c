//dis_magne.c
//return how many DWs disappeared at the specified magnet fields

//the format of data files must be
//	View_Overall# Iteration DAQ-X Pulse_Amp Field #DWs
//	and the first line of the files must be column names above

//the numbers of data files are all recgnized as real numbers, not integer 	
//OutPutFile will be "InputFileName + .out"

//***Note***
//You must modify the first line of data file, like
//	"View Overall#" to "View_Overall#"

#include <stdio.h>

int main(int argc, char** argv) {
	FILE *fp_in, *fp_out;
	char *InputFileName;
	char OutputFileName[100];
	
	int skip_lines = 11;	//how many lines(iteration) you skip at each View_Overall
	double iteration_current = 0;
	double DWs_previous;
	double data_current[6], data_previous[6];

	char dust[8][100];	//for non-substitution fscanf

	int i;

	printf("flag 5\n");
	
	if (argc != 2) {
		printf("Usage: %s InputFileName\n", argv[0]);
		return 0;
	}
	InputFileName = argv[1];
	printf("flag 7\n");
	sprintf(OutputFileName, "%s.output", InputFileName);

	printf("flag 9\n");
	fp_in = fopen(InputFileName, "r");
	if (fp_in == NULL) {
		printf("Can't open file %s\n", InputFileName);
		return 0;
	}
	fp_out = fopen(OutputFileName, "w");
	if (fp_out == NULL) {
		printf("Can't open file %s\n", OutputFileName);
		return 0;
	}
	fprintf(fp_out, "View_Overall#	Disappearing_DAQ-X / V	Disappearing_Magnetic_Field / Oe	#Disappearing_DWs\n");

	fscanf(fp_in, "%s %s %s %s %s %s %s %s\n", dust[0], dust[1], dust[2], dust[3], dust[4], dust[5], dust[6], dust[7]);
	printf("first line of %s is %s %s %s %s %s %s\n", argv[1], dust[0], dust[1], dust[2], dust[3], dust[4], dust[5]);
	fscanf(fp_in, "%lf %lf %lf %lf %lf %lf\n", &data_previous[0], &data_previous[1], &data_previous[2], &data_previous[3], &data_previous[4], &data_previous[5]);
	//%*s means that you read the data in %s format, but you don't substitute the data in a variable.

	printf("flag 10\n");

	while (1) {
		for (i = 0; i < skip_lines - 1; ++i) {
			fscanf(fp_in, "%lf %lf %lf %lf %lf %lf\n", &data_previous[0], &data_previous[1], &data_previous[2], &data_previous[3], &data_previous[4], &data_previous[5]);
		}
		printf("flag 20\n");

		while (1) {
			if (fscanf(fp_in, "%lf %lf %lf %lf %lf %lf\n", &data_previous[0], &data_previous[1], &data_previous[2], &data_previous[3], &data_previous[4], &data_previous[5]) == EOF) {
				goto ending;
			}
			printf("data_previous is %lf %lf %lf %lf %lf %lf\n", data_previous[0], data_previous[1], data_previous[2], data_previous[3], data_previous[4], data_previous[5]);

			if (fscanf(fp_in, "%lf %lf %lf %lf %lf %lf\n", &data_current[0], &data_current[1], &data_current[2], &data_current[3], &data_current[4], &data_current[5]) == EOF) {
				printf("You have a mistake in skip_lines or file format.");
				return 0;
			}
			printf("data_current is %lf %lf %lf %lf %lf %lf\n", data_current[0], data_current[1], data_current[2], data_current[3], data_current[4], data_current[5]);

			printf("flag 30\n");
			printf("current ViewOverall is %lf, current Iteration is %lf\n", data_current[0], data_current[1]);

			if (iteration_current > data_current[1]) {
				iteration_current = 0.0;
				break;
			} else {
				iteration_current = data_current[1];
			}
			if ((int)data_previous[1] == skip_lines - 1) {
				DWs_previous = data_current[5];
			} else {
				fprintf(fp_out, "%lf %lf %lf %lf\n", data_current[0], data_previous[2], data_previous[4], DWs_previous - data_current[5]);
				DWs_previous = data_current[5];
			}
		}

	}

	ending:
	fclose(fp_in);
	fclose(fp_out);
}





