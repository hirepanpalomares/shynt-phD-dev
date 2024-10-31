#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 1024
#define MAX_INFO_LENGTH 506161
#define MAX_NUM_VALUES 5


// Function to split a CSV line into parts (index, value, and info)
void split_line(char* line, double* jin, double* jout, int count) {
    char* token = strtok(line, ",");  // Get the index
    int g = atoi(token);
    token = strtok(NULL, ","); // drop the energy cid
    token = strtok(NULL, ","); // drop the energy sid
    
    token = strtok(NULL, ",");
    jin[count] = atof(token);

    token = strtok(NULL, ",");
    jout[count] = atof(token);

    token = strtok(NULL, ","); // drop the last value

}

int main() {
    FILE* file = fopen("4r-J.csv", "r");
    if (file == NULL) {
        perror("Error opening file");
        return EXIT_FAILURE;
    }

    char line[MAX_LINE_LENGTH];
    int max_elements = 506161;  // Number of elements you want to handle

    double* jin = malloc(max_elements * sizeof(double));
    double* jout = malloc(max_elements * sizeof(double));


    // Skip the header line
    fgets(line, sizeof(line), file);

    int count = 0;
    // Read each line of the CSV file
    while (fgets(line, sizeof(line), file)) {
        line[strcspn(line, "\n")] = '\0';  // Remove the newline character

        // Split the line into numeric values and store them
        split_line(line, jin, jout, count);
        printf("Index = %i, Jin = %f, Jout = %f \n", count, jin[count], jout[count]);

        count++;
    }

    fclose(file);

    // Print the vector elements and their numeric values
    for (int i = 0; i < count; i++) {
    }

    free(jin);
    free(jout);
    return 0;
}