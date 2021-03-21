#include <iostream>
using namespace std;

void SiftDown(int*, int,int);
void Heapify(int*, int);
int ExctractMax(int*, int);
void HeapSort(int*, int);

int main() {
	int size = 15;
	int* c = new int[size];
	for (int i = 0; i < size; i++) {
		c[i] = rand() % 10;
		cout << c[i] << " ";
	}cout << "\n";

	HeapSort(c, size);
	for (int i = 0; i < size; i++) cout << c[i] << " ";
	delete[]c;
	return 0;
}

void SiftDown(int* A, int i, int size) {
	while (2 * i + 1 < size) {
		int j = i;
		if (A[j] < A[2 * i + 1]) j = 2 * i + 1;
		if (2 * i + 2 < size && A[j] < A[2 * i + 2]) j = 2 * i + 2;
		if (j == i)break;
		else {
			swap(A[i], A[j]);
			i = j;
		}
	}
}

void Heapify(int* A, int size) {
	for (int i = size - 1; i >= 0; i--) {
		SiftDown(A, i, size);
	}
}

int ExctractMax(int* A, int size) {
	int max = A[0];
	if (size) {
		size--;
		A[0] = A[size];
		SiftDown(A, 0, size);
	}
	return max;
}

void HeapSort(int* A, int size) {
	Heapify(A, size);
	for (int i = size - 1; i >= 0; i--) {
		A[i] = ExctractMax(A, i);
	}
}
