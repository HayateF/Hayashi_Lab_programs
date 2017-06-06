// histogram.c
// make histograma after dis_magne.c

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
	double start_x, end_x, step_x;
	int histo_size;
	int *histogram;
	int i;

	char dust[8][100];	
	double data[4];

	FILE *fp_in, *fp_out;
	char *InputFileName;
	char OutputFileName[100];

	if (argc != 5) {
		printf("Usage: %s InputFileName start_x end_x step_x\n", argv[0]);
		return 0;
	}

	InputFileName = argv[1];
	if ( (fp_in = fopen(InputFileName, "r")) == NULL) {
		fprintf(stderr, "Can't open %s\n", InputFileName);
		return 0;
	}

	sprintf(OutputFileName, "%s.histogram", InputFileName);
	if ( (fp_out = fopen(OutputFileName, "w")) == NULL) {
		fprintf(stderr, "Can't open %s\n", OutputFileName);
		return 0;
	}
	fprintf(fp_out, "Field_Range/Oe Field_Center/Oe Count\n");

	start_x = atof(argv[2]);
	end_x = atof(argv[3]);
	step_x = atof(argv[4]);
	histo_size = (int)((end_x - start_x) / step_x) + 1;

	histogram = (int *)malloc(sizeof(int) * histo_size);
	printf("malloc success\n");

	fscanf(fp_in, "%s %s %s %s %s %s %s %s", dust[0], dust[1], dust[2], dust[3], dust[4], dust[5], dust[6], dust[7]);
	printf("first line read ok\n");
	while (fscanf(fp_in, "%lf %lf %lf %lf", &data[0], &data[1], &data[2], &data[3]) != EOF) {
		histogram[(int)((data[2] - start_x) / step_x)] += (int)data[3];
		printf("Now ViewOverall is %lf\n", data[0]);
		// (int) casts real number 1.7892 to integer 1
	}

	for (i = 0; i < histo_size; ++i) {
	if (histogram[i] < 0) histogram[i] = 0;
	fprintf(fp_out, "[%lf_%lf] %lf %d\n", start_x + i * step_x, start_x + (i+1) * step_x, start_x + (i + 0.5) * step_x, histogram[i]);
	}

	fclose(fp_in);
	fclose(fp_out);
	free(histogram);
}
