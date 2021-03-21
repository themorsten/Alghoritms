void Insertion_sort(int* A, const int size) {
	for (int i = 1; i < size; i++) {
		int k = i;
		while (k && A[k - 1] > A[k]) {
			swap(A[k - 1], A[k]);
			k--;
		}
	}
}
