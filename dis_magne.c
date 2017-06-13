//dis_magne.c
//return how many DWs disappeared at the specified magnet fields

//the format of data files must be
//	View_Overall# Iteration DAQ-X Pulse_Amp Field #DWs
//	and the first line of the files must be column names above

//the numbers of data files are all recgnized as real numbers, not integer 	
//OutPutFile will be "InputFileName + .out"

#include <stdio.h>

int main(int argc, char** argv) {
	FILE *fp_in, *fp_out;
	char *InputFileName;
	char OutputFileName[100];
	
//	int skip_lines = 11;	//how many lines(iteration) you skip at each View_Overall
	int skip_lines;
	double DWs_previous;
	double data_current[6], data_previous[6];

	char dust[8][100];	//for non-substitution fscanf

	int i;

	if (argc != 3) {
		printf("Usage: %s InputFileName skip_lines\n", argv[0]);
		return 0;
	}
	InputFileName = argv[1];
	sprintf(OutputFileName, "%s.output", InputFileName);
	skip_lines = atoi(argv[2]);

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
	fscanf(fp_in, "%lf %lf %lf %lf %lf %lf\n", &data_previous[0], &data_previous[1], &data_previous[2], &data_previous[3], &data_previous[4], &data_previous[5]);


	while (1) {
		for (i = 0; i < skip_lines - 1; ++i) {
			fscanf(fp_in, "%lf %lf %lf %lf %lf %lf\n", &data_previous[0], &data_previous[1], &data_previous[2], &data_previous[3], &data_previous[4], &data_previous[5]);
		}
		//Note that the last iteration of each ViewOverall is Max Field

		while (1) {
			if (fscanf(fp_in, "%lf %lf %lf %lf %lf %lf\n", &data_previous[0], &data_previous[1], &data_previous[2], &data_previous[3], &data_previous[4], &data_previous[5]) == EOF) {
				printf("You have a mistake in skip_lines or file format.");
				return 0;
			}

			if (fscanf(fp_in, "%lf %lf %lf %lf %lf %lf\n", &data_current[0], &data_current[1], &data_current[2], &data_current[3], &data_current[4], &data_current[5]) == EOF) {
				goto ending;
			}

			if (data_current[0] > (data_previous[0] + 0.1)) break;	//Next ViewOverall

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





