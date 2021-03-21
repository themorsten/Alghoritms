void Selection_sort(int* A, const int size) {
	for (int i = 0; i < size-1; i++) {
		int min = i;
		for (int j=i+1; j < size - 1; j++) {
			if (A[min] > A[j]) min = j;
		}
		swap(A[min], A[i]);
	}
}
